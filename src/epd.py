#import epd2in13

# Interfaces to be implemented for mock
# init()
# reset() ?
# sleep() ?
# set_frame_memory(image, x, y)
# clear_frame_memory(color) # color is 1-byte, 1 bit per pixel, e.g., 0xFF (8 bits white)
# display_frame()


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
    def __init__(self):
        self.epd = epd2in13.EPD()
        self.epd.init(self.epd.lut_partial_update) # or epd.lut_full_update
        self.image_white = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)
        self.image_black = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 0)  
        self.clear_frame = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)  # 255: clear the frame
        self.components  = []

    def update_component(self, c):
        # TODO: Do we need to call rotate 2 times?
        self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
        self.epd.display_frame()
        self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y)
#        self.epd.display_frame()
        c.invalid = False

    def update(self):
        # TODO: Can we set the frame first (all components) and then display?
        # TODO: Prepare an image with the whole layout. e.g., for complete epd update
        for c in self.components:
            if c.invalid == True:
                self.update_component(c)

    def update_all(self):                                                  
#        for c in self.components:                                          
#            if c.invalid == True:                                          
#                self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y) 
#        self.epd.display_frame()                                           
        for c in self.components:                                          
            if c.invalid == True:                                          
                self.epd.set_frame_memory(c.image.rotate(c.rot), c.x, c.y) 
                self.invalid = False                                       
        self.epd.display_frame()
                
    def clear_all(self):
        self.epd.set_frame_memory(self.image_black, 0, 0)
        self.epd.display_frame()
        self.epd.set_frame_memory(self.image_white, 0, 0)
        self.epd.display_frame()
#       self.epd.clear_frame_memory(0x00)
#       self.epd.display_frame()
#       self.epd.clear_frame_memory(0x00)
#       self.epd.display_frame()
#       self.epd.clear_frame_memory(0xFF)
#       self.epd.display_frame()
#       self.epd.clear_frame_memory(0xFF)
##       self.epd.display_frame()
    
    def clear(self, deep=False):
        if deep == True:
            self.epd.init(self.epd.lut_full_update)
# TODO
#            self.epd.clear_frame_memory(0xFF)
#            self.epd.set_frame_memory(self.clear_white, 0, 0)
#            self.epd.display_frame()
#            self.epd.init(self.epd.lut_partial_update)
#        else:
            self.epd.set_frame_memory(self.clear_white, 0, 0)
            self.epd.display_frame()
            self.epd.set_frame_memory(self.clear_white, 0, 0)
            self.epd.display_frame()
            self.epd.init(self.epd.lut_partial_update)

    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )

# ========================================================================            
## This is a small script to demonstrate using Tk to show PIL Image objects.
 # The advantage of this over using Image.show() is that it will reuse the
 # same window, so you can show multiple images without opening a new
 # window for each image.
 # 
 # This is used as a mock-up of e-paper display to quickly develop/test display layouts
 ##
 
import os, sys
import time
import Tkinter
from PIL import Image, ImageTk, ImageOps

def button_click_exit_mainloop (event):
    event.widget.quit() # this will cause mainloop() to unblock.
    
class EPD_MOCKUP(object):
    def __init__(self, w, h):
        
        self.image_white = Image.new('1', (w, h), 255) # 'RGBA' for color images
        self.image_black = Image.new('1', (w, h),   0)  
        self.image_frame = Image.new('1', (w, h), 255)
        self.image_invrt = Image.new('1', (w, h),   0)
        self.image       = self.image_white
        
        self.components  = []        

        # The mock-up part
        self.root = Tkinter.Tk()
        self.root.bind("<Button>", button_click_exit_mainloop) # unblock mainloop()
        self.root.geometry('%dx%d' % (w, h))        
        self.tkpi        = ImageTk.PhotoImage(self.image)
        self.label_image = Tkinter.Label(self.root, image=self.tkpi)

                
    def clear(self, deep=None):
        self.image = self.image_white
        self.epd_update()
        time.sleep(1)


    def add(self, component):
        if isinstance(component, (list,)): 
            self.components.extend( component )
        else:
            self.components.append( component )  

    # TODO: Should be renamed to display_fame()        
    def epd_update(self):
        # Mock-up
        self.tkpi        = ImageTk.PhotoImage(self.image)
        self.label_image = Tkinter.Label(self.root, image=self.tkpi)
        self.label_image.place(x=0,y=0,width=self.image.size[0],height=self.image.size[1])
        
        self.root.update()
        time.sleep(0.3)


   # TODO: keep only update_all after test with the real display
    def update(self, at_once = False):
        if at_once == True:
             self.update_all()
        else:        
            for c in self.components:                                                                                    
                if c.invalid == True:  
                    self.image.paste(c.image.rotate(c.rot), (c.x, c.y))                                                                                      
                    c.invalid = False
                    self.epd_update()
                
    def update_all(self):                                                                                                
        for c in self.components:                                                                                    
            if c.invalid == True:  
                self.image_frame.paste(c.image.rotate(c.rot), (c.x, c.y))                                                                                      
                c.invalid = False

        self.image = self.image_frame                
        self.epd_update()                

            
    def refresh(self):
        self.image_invrt = self.image_frame.convert('L')
        self.image_invrt = ImageOps.invert(self.image_invrt)
        self.image_invrt = self.image_invrt.convert('1')
        self.image = self.image_invrt
        self.epd_update()
        time.sleep(0.3)
        self.image = self.image_frame
        self.epd_update()
        time.sleep(0.3)
    
    # TODO: Not so many updates needed
    def refresh_1(self):
        self.image = self.image_black
        self.epd_update()
#        time.sleep(0.3)
        self.image = self.image_white
        self.epd_update()
#        time.sleep(0.3)
        self.image = self.image_black
        self.epd_update()
#        time.sleep(0.3)
        self.image = self.image_frame
        self.epd_update()
#        time.sleep(0.3)

        
    # TODO: To be removed         
    def run_all(self):
        dirlist = os.listdir('.')
        y = 0
        for f in dirlist:
            try:
                image = Image.open(f)
                image = image.resize((32,32), Image.ANTIALIAS)
                self.image.paste(image, (0, y))
                #y += 32
                self.root.title(f)
                
                self.epd_update()
                self.root.mainloop() # wait until user clicks the window
                
            except Exception, e:
                # This is used to skip anything not an image.
                # Image.open will generate an exception if it cannot open a file.
                # Warning, this will hide other errors as well.
                print e
                pass
                
                
if __name__ == "__main__":
    epd = EPD_MOCKUP(122, 250)
    epd.clear()
    epd.run_all()