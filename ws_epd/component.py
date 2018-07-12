# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

icons_list={u'chancerain':u'',u'chancesleet':u'','chancesnow':u'','chancetstorms':u'','clear':u'','flurries':u'','fog':u'','hazy':u'','mostlycloudy':u'','mostlysunny':u'','partlycloudy':u'','partlysunny':u'','sleet':u'','rain':u'','sunny':u'','tstorms':u'','cloudy':u''}
#flurries        u'\uf01b'
#mostlysunny     u'\uf00c'
#mostlycloudy    u'\uf031'
#partlycloudy    u'\uf002'
#partlysunny     u'\uf002'
#clear           u'\uf00d'
#sunny           u'\uf00d'
#cloudy          u'\uf031'
#hazy            u'\uf0b6'
#chancesnow      u'\uf00a'
#sleet           u'\uf0b2'
#tstorms         u'\uf033'
#fog             u'\uf014'
#rain            u'\uf008'
#chancesleet     u'\uf0b2'
#chancerain      u'\uf00d'
#chancetstorms   u'\uf01e'
# Cyrillic arial starts at 0x03
# supperscript of '3' u'\u00B3'
# subscript of '2' u'\u2083'

import os.path
path_prefix = os.path.dirname(__file__)
#print path_prefix 

# font_weather_icons = ImageFont.truetype(path_prefix + '/fonts/' + 'weathericons-regular-webfont.ttf', 35)
#draw.text((30,330),icons_list[str(icon)],font=font_weather_icons,fill=255)

# TODO: Magic constants
# TODO: Fonts and icons taken from local ws_epd folders. Allow for absolute paths as well
# TODO: Date and time as a separate component?

class Component(object):

#    def __init__(self, width, height, font_size, bg_color = 255, image = None):
    def __init__(self, width, height, bg_color = 255,          \
                       iw = 24,       ih = 24,  image = None,  \
                       font = 'arial.ttf', font_size = 14):

        self.set_color(bg_color)

        self.set_width(width)
        self.set_height(height)

        # position in EPD, to be set when building layout --------------------------------------
        self.x         = 0 #
        self.y         = 0 #
        self.rot       = 0 # Rotate the image when set in the frame memory (0, 90, 180, 270)
        # -------------------------------------------------------------------------------------

        self.set_image(iw, ih, image) # TODO/Note: rot=90, image must be square
#        self.image = Image.new('1', (width, height), bg_color)
#        if image != None:
#            im = Image.open(image)
#            im = im.resize((self.w,self.w), Image.ANTIALIAS)
#            self.image.paste(im, ((width-self.w)/2, (self.h-self.w)/2))

        self.draw      = ImageDraw.Draw(self.image)
        self.font      = ImageFont.truetype(path_prefix + '/fonts/' + font, font_size)
#        self.font      = ImageFont.truetype(path_prefix + '/fonts/' + 'arial.ttf', font_size)
#        self.font      = ImageFont.truetype(path_prefix + '/fonts/' + 'weathericons-regular-webfont.ttf', font_size)
        self.aleft     = 0
        self.acenter   = 1
        self.aright    = 2
        self.align     = self.aright

        self.invalid   = 2 # To redraw in every frame memory
        self.borders   = False # TODO

    def set_color(self, bg_color):
        self.bg        = 255 if bg_color == 255 else 0   # 0 - black, 255 - white
        self.fg        = 0   if bg_color == 255 else 255
        
    def color_invert(self):
        self.bg        = 255 if self.bg ==   0 else 0   # 0 - black, 255 - white
        self.fg        = 0   if self.bg == 255 else 255
        self.invalid   = 2
        
    def set_width(self, width):
        # x point (size and position) must be the multiple of 8 or the last 3 bits will be ignored
        self.w         = width & 0xF8
        if width & 0x03 != 0: print "Width is not multiple of 8. Trimmed to", self.w
        if width > 128:
            "Width is > 128. Set to 128"
            self.w = 128

    def set_height(self, height):
        if height > 250: "Height is > 250. Set to 250"
        self.h = height if height <= 250 else 250

    def set_image(self, width, height, image):
        self.image = Image.new('1', (self.w, self.h), self.bg)
        if image != None:
            im = Image.open(path_prefix + '/icons/' + image)
            im = im.resize((width,height), Image.ANTIALIAS)
            # center image within component
            self.image.paste(im, ((self.w-width)/2, (self.h-height)/2))

    def set_position(self, x, y, r=0):
        # x point (size and position) must be the multiple of 8 or the last 3 bits will be ignored
        self.x = x & 0xF8
        if  self.x & 0x03 != 0: print "X-position is not multiple of 8. Trimmed to", self.x
        self.y   = y
        if self.h + self.y > 250: print "Y-position and height > 250"
        self.rot = r


    def draw_borders(self):
        w = self.w if self.x + self.w < 122 else 122 - self.x
        self.draw.line((0,   0,        w-1, 0       ), fill=self.fg)
        self.draw.line((0,   0,        0,   self.h-1), fill=self.fg)
        self.draw.line((0,   self.h-1, w-1, self.h-1), fill=self.fg)
        self.draw.line((w-1, self.h-1, w-1, 0       ), fill=self.fg)
        self.invalid = 2

    # TODO: 1 line or more
    def set_text(self, text, x=5, y=None, align=None):
        if align == None: align = self.align
        self.clear()
        if y == None: # Vertical center
            tx, ty = (0,0)
            w, h = self.draw.textsize(text, self.font)
            if align == self.aright:
                o = x if self.x + self.w < 122 else self.x + self.w - 122 + x
                tx = self.w - o - w
                ty = ((self.h - h) >> 1)-1
            elif align == self.aleft:
                tx = x
                ty = ((self.h - h) >> 1)-1
            elif align == self.acenter:
                tx = self.w/2-(w/2)
                ty = ((self.h - h) >> 1)-1

            self.draw.text((tx, ty), text, font = self.font, fill = self.fg)
#            self.draw.text((tx, ty),icons_list[u'chancerain'],font=self.font,fill=self.fg)

        else:
            self.draw.text((x, y), text, font = self.font, fill = self.fg)
        self.invalid = 2


    def clear(self):
        self.draw.rectangle((0, 0, self.w-1, self.h-1), fill=self.bg)
        self.invalid = 2


class Separator(Component):
    def __init__(self, width, height, bg_color = 255, x1=32, x2=48, image = None):
        super(Separator, self).__init__(width, height, font_size=3, bg_color=bg_color, image=image)
        self.draw.line((x1, height/2, x2, height/2), fill=self.fg)


# Currently, 24 bars graph in 122 pixels, 5 pixels per bar, including separation
class BarGraph(Component):
    def __init__(self, width, height, bg_color = 255, image = None):
        super(BarGraph, self).__init__(width, height, font_size=3, bg_color=bg_color, image=image)
        
        self.nbars = 24
        self.bars  = [0 for _ in range(self.nbars)]
        self.draw_lines()
    
    def draw_lines(self):
        self.draw.line((0, self.h/2, self.w, self.h/2), fill=self.fg) # Middle
        self.draw.line((0, self.h-1, self.w, self.h-1), fill=self.fg) # Bottom
    
    def clear_bars(self):
        self.bars    = [0 for _ in range(self.nbars)]
        self.invalid = 2
        
    def set_bar(self, position, value):
        if position > self.nbars-1:
            print "Wrong position:", position, "Set to 0"
            position = 0
            
        if value > self.h:
            print "Value too large:", value, "Set to", self.h
            value = self.h
            
        self.bars[position] = value
        self.update()
        
    def update(self):
        self.clear()
        self.draw_lines()
        for i, h in enumerate(self.bars):
            offset = 2 + (5 * i)
            self.draw.rectangle((offset, self.h-h-1, offset+2, self.h-1), fill=self.fg)
        self.invalid = 2