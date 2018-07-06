import time
import Tkinter
from PIL import Image, ImageTk

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
#        self.root.overrideredirect(True) # No title bar, no resizing, no possibilities of managing the window
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

    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)