from PIL import Image, ImageDraw

import time

##
 # For partial update:
 # there are 2 memory areas embedded in the e-paper display
 # and once the display is refreshed, the memory area will be auto-toggled,
 # i.e. the next action of SetFrameMemory will set the other memory area
 # therefore you have to set the frame memory twice.
 ##

class EPD:
    """ Waveshare 2.13 inch e-paper screen with partial update support
        w = 128, h = 250; usable resolution: 122 x 250
        x point (size and position) must be the multiple of 8 or the last 3 bits will be ignored
        self.image_frame = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)  # 255: clear the frame
    """
    def __init__(self, Waveshare = True, Layout = None):
        if Waveshare == True:
            import epd2in13
            self.epd = epd2in13.EPD()
        else:
            import epd2in13_mock
            self.epd = epd2in13_mock.EPD_2in13_MOCK()

        self.image_frame = Image.new('1', (128, 250), 255)  # 255: clear the frame
        self.components  = []

        if Layout != None:
            self.add(Layout.components)

        # display and switch to partial update mode
        self.display_image_full_update()


    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )


    def get_image_frame(self):
        if len(self.components) != 0:       
            for c in self.components:
                self.image_frame.paste(c.image, (c.x, c.y))
                c.invalid = 0
            
        return self.epd.get_frame_buffer(self.image_frame) # Do we need to use epd.get_frame_buffer()?


    def display(self, image, fmode = False):
        if fmode == True: self.epd.clear_frame_memory(0xFF)
        self.epd.set_frame_memory(image, 0, 0)
        self.epd.display_frame()
        if fmode != True: time.sleep(2) # Do we need this?
        
        
    def display_image_full_update(self):
        self.epd.init(self.epd.lut_full_update)       
        self.show(fmode = True)
        self.epd.init(self.epd.lut_partial_update)


    def show(self, fmode = False):
        image_frame = self.get_image_frame()
        self.display(image_frame, fmode = fmode)
        self.display(image_frame, fmode = fmode)


    def update(self):
        # OK to update only 1 memory buffer per iteration (reduced update latency)
        # Since c.invalid starts from 2 and is decremented during update,
        # the other memory buffer will be updated during the next update iteration.
        for c in self.components:
            if c.invalid != 0:
                self.epd.set_frame_memory(c.image, c.x, c.y)
                c.invalid -= 1
        self.epd.display_frame()

        # TODO landscape: self.epd.set_frame_memory(c.image.transpose(Image.ROTATE_270), c.x, c.y)
     