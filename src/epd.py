#import epd2in13

import time
import Tkinter
from PIL import ImageTk
from PIL import Image, ImageOps

def button_click_exit_mainloop (event):
    event.widget.quit() # this will cause mainloop() to unblock.

class EPD_2in13_MOCK:
    def __init__(self):

        self.w = 122 # Usable resolution
        self.h = 250

        self.lut_partial_update = []
        self.lut_full_update    = []

        self.image = Image.new('1', (self.w, self.h), 255)

        # The mock-up part
        self.root = Tkinter.Tk()
        self.root.bind("<Button>", button_click_exit_mainloop) # unblock mainloop()
        self.root.geometry('%dx%d' % (self.w, self.h))
        self.tkpi        = ImageTk.PhotoImage(self.image)
        self.label_image = Tkinter.Label(self.root, image=self.tkpi)

    def init(self, dummy_lut):
        pass


    def set_frame_memory(self, image, x, y):
        self.image.paste(image, (x, y))

    # TODO: Not clear how this function works on the real display and how to be used
    def clear_frame_memory(self, color):
        """ color is 1-byte, 1 bit per pixel, e.g., 0xFF (8 bits white)
            Currently supported color: 0x00 and 0xFF
        """
        if color != 0 and color != 255:
            print "In set_frame-memory(): Color not supported:", color
            return
        self.image = Image.new('1', (self.w, self.h), color)


    def display_frame(self):
        self.tkpi        = ImageTk.PhotoImage(self.image)
        self.label_image = Tkinter.Label(self.root, image=self.tkpi)
        self.label_image.place(x=0,y=0,width=self.image.size[0],height=self.image.size[1])

        self.root.update()
        time.sleep(0.5)


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
    def __init__(self, Waveshare = True):
        if Waveshare == True:
            self.epd = epd2in13.EPD()
            self.epd.init(self.epd.lut_partial_update) # or epd.lut_full_update
            self.image_white = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)
            self.image_black = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT),   0)
            self.image_frame = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)  # 255: clear the frame
            self.image_invrt = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT),   0)
        else:
            self.epd = EPD_2in13_MOCK()
            self.epd.init(self.epd.lut_partial_update) # or epd.lut_full_update
            self.image_white = Image.new('1', (128, 250), 255)
            self.image_black = Image.new('1', (128, 250),   0)
            self.image_frame = Image.new('1', (128, 250), 255)  # 255: clear the frame
            self.image_invrt = Image.new('1', (128, 250),   0)

        self.components  = []


    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )


    def show(self):
        for c in self.components:
            self.image_frame.paste(c.image, (c.x, c.y))
            c.invalid = False

        self.epd.set_frame_memory(self.image_frame, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_frame, 0, 0)


    def refresh(self):
        for c in self.components:
            self.image_frame.paste(c.image.rotate(c.rot), (c.x, c.y))

        self.image_invrt = self.image_frame.convert('L')
        self.image_invrt = ImageOps.invert(self.image_invrt)
        self.image_invrt = self.image_invrt.convert('1')

        self.epd.set_frame_memory(self.image_invrt, 0, 0)
        self.epd.display_frame()

        self.epd.set_frame_memory(self.image_frame, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_frame, 0, 0)


    def clear(self):
        self.epd.set_frame_memory(self.image_white, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_white, 0, 0)
#        self.epd.display_frame()


    def update(self):
#        for c in self.components:
#            if c.invalid == True:
#                self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
#        self.epd.display_frame()
        for c in self.components:
            if c.invalid == True:
#                self.epd.set_frame_memory(c.image, c.x, c.y)
                self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
                c.invalid = False
        self.epd.display_frame()


    # TODO: works but to be removed
    def update_1b1(self):
        for c in self.components:
            if c.invalid == True:
                self.update_component(c)
                c.invalid = False

    # TODO: works but to be removed
    def update_component(self, c):
        self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
        self.epd.display_frame()
        self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
#        self.epd.display_frame()
