# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
#from epd_mockup import EPD_MOCKUP

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

font_weather_icons = ImageFont.truetype('fonts/weathericons-regular-webfont.ttf', 35)
#draw.text((30,330),icons_list[str(icon)],font=font_weather_icons,fill=255)

class Component(object):

    def __init__(self, width, height, font_size, bg_color = 255, image = None):
        self.bg        = 255 if bg_color == 255 else 0   # 0 - black, 255 - white
        self.fg        = 0   if bg_color == 255 else 255
        # x point (size and position) must be the multiple of 8 or the last 3 bits will be ignored
        self.w         = width & 0xF8
        if width & 0x03 != 0: print "Width is not multiple of 8. Trimmed to", self.w
        self.h         = height
#        if width >= 128: self.w = 122
#        self.fsize     = font_size
        # position in EPD, to be set when building layout --------------------------------------
        self.x         = 0 #
        self.y         = 0 #
        self.rot       = 0 # Rotate the image when set in the frame memory (0, 90, 180, 270)
        # -------------------------------------------------------------------------------------
        if image != None:
            self.image = Image.open(image)
            self.image = self.image.resize((26,26), Image.ANTIALIAS)
        else:
            self.image = Image.new('1', (width, height), bg_color)

        self.draw      = ImageDraw.Draw(self.image)
        self.font      = ImageFont.truetype('fonts/arial.ttf', font_size)
#        self.font      = ImageFont.truetype('fonts/weathericons-regular-webfont.ttf', font_size)
        self.aleft     = 0
        self.acenter   = 1
        self.aright    = 2
        self.align     = self.aright

        self.invalid   = True # To redraw when True
        self.borders   = False # TODO
        
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
        self.invalid = True

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
                ty = self.h/2-(h/2)               
            elif align == self.aleft:
                tx = x
                ty = self.h/2-(h/2)            
            elif align == self.acenter:
                tx = self.w/2-(w/2)
                ty = self.h/2-(h/2)
            
            self.draw.text((tx, ty), text, font = self.font, fill = self.fg)
#            self.draw.text((tx, ty),icons_list[u'chancerain'],font=self.font,fill=self.fg)
            
        else:
            self.draw.text((x, y), text, font = self.font, fill = self.fg)
        self.invalid = True


    def clear(self):
        self.draw.rectangle((0, 0, self.w-1, self.h-1), fill=self.bg)
        self.invalid = True



class Separator(Component):
    def __init__(self, width, height, y=0, x=0, font_size=3, bg_color = 255, image = None):
        super(Separator, self).__init__(width, height, font_size, bg_color, image)
        self.draw.line((32,height/2,48,height/2), fill=self.fg)
