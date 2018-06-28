from PIL import Image, ImageOps

import time

##
 # there are 2 memory areas embedded in the e-paper display
 # and once the display is refreshed, the memory area will be auto-toggled,
 # i.e. the next action of SetFrameMemory will set the other memory area
 # therefore you have to set the frame memory twice.
 ##

class EPD:
    """ Waveshare 2.13 inch e-paper screen with partial update support
        w = 128, h = 250; usable resolution: 122 x 250
        x point (size and position) must be the multiple of 8 or the last 3 bits will be ignored
    """
    def __init__(self, Waveshare = True, Layout = None):
        if Waveshare == True:
            import epd2in13
            self.epd = epd2in13.EPD()
            self.epd.init(self.epd.lut_partial_update) # or epd.lut_full_update
            self.image_white = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)
            self.image_black = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT),   0)
            self.image_frame = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)  # 255: clear the frame
            self.image_invrt = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT),   0)
        else:
            import epd2in13_mock
            self.epd = epd2in13_mock.EPD_2in13_MOCK()
            self.epd.init(self.epd.lut_partial_update) # or epd.lut_full_update
            self.image_white = Image.new('1', (128, 250), 255)
            self.image_black = Image.new('1', (128, 250),   0)
            self.image_frame = Image.new('1', (128, 250), 255)  # 255: clear the frame
            self.image_invrt = Image.new('1', (128, 250),   0)

        self.components = []

        self.clear()
#        self.refresh()

        if Layout != None:
            self.add(Layout.components)
            self.show()


    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )


    def show(self):
        if len(self.components) == 0: return
        for c in self.components:
            self.image_frame.paste(c.image, (c.x, c.y))
            c.invalid = 0

        self.epd.set_frame_memory(self.image_frame, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_frame, 0, 0)


    def refresh(self):
        self.epd.init(self.epd.lut_full_update)
        self.epd.display_frame()
        self.epd.init(self.epd.lut_partial_update)
#        self.show() # Not needed


    def refresh_NOT_OK(self):
        for c in self.components:
            self.image_frame.paste(c.image.rotate(c.rot), (c.x, c.y))
            c.invalid = 0

        self.image_invrt = self.image_frame.convert('L')
        self.image_invrt = ImageOps.invert(self.image_invrt)
        self.image_invrt = self.image_invrt.convert('1')

        self.epd.set_frame_memory(self.image_invrt, 0, 0)
        self.epd.display_frame()

        self.epd.set_frame_memory(self.image_frame, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_frame, 0, 0)


    # Almost the same as refresh()?
    def clear(self):
        self.epd.init(self.epd.lut_full_update)
#        self.epd.clear_frame_memory(0xFF) # TODO
        self.epd.set_frame_memory(self.image_white, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_white, 0, 0)
        self.epd.init(self.epd.lut_partial_update)
        self.show()


    def update(self):
        # OK to update only 1 memory buffer per iteration (reduced update latency)
        # Since c.invalid starts from 2 and is decremented during update,
        # the other memory buffer will be updated during the next update iteration.
        for c in self.components:
            if c.invalid != 0:
#                self.epd.set_frame_memory(c.image, c.x, c.y)
                self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
                c.invalid -= 1
        self.epd.display_frame()
