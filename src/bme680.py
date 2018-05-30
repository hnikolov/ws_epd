# -*- coding: utf-8 -*-
import time
from PIL import ImageFont
from epd import EPD
from component import Component, Separator

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
#degC = 0xF03C
#deg = 0xF042
#thermo = 0xF055
#thermo_out = 0xF053
#thermo_in = 0xF054
#fire = 0xF0c7
#earthquake = 0xF0C6
#barometer = 0xF079
#humidity = 0xF07A

class Layout_1:
    def __init__(self):
        self.width   = 128 # epd2in13.EPD_WIDTH
        self.height  = 250 # epd2in13.EPD_HEIGHT
        self.ch1     =  15 # component height 1
        self.ch2     =  24 # component height 2
        self.ch3     =  32 # component height 3
        self.sh1     =   7 # separator height 1

        # Offsets
        self.sep_1_y = self.ch1 # after (date and time)
        self.row_1_y = self.sep_1_y + self.sh1
        self.sep_2_y = self.row_1_y + self.ch2
        self.row_2_y = self.sep_2_y + self.sh1
        self.sep_3_y = self.row_2_y + self.ch2
        self.row_3_y = self.sep_3_y + self.sh1
        self.sep_4_y = self.row_3_y + self.ch2
        self.row_4_y = self.sep_4_y + self.sh1
        self.sep_5_y = self.row_4_y + self.ch2
        self.row_5_y = self.sep_5_y + self.sh1
        self.sep_6_y = self.row_5_y + self.ch2
        self.row_6_y = self.sep_6_y + self.sh1

        # Random values for test
        self.temperature = 23.45
        self.pressure    = 1013.6
        self.humidity    = 46.78
        self.air_quality = 92.14 

        # E-Paper Display instance
        self.epd = EPD(False)
        self.epd.refresh()
#        self.epd.clear()

        # Build the layout
        self.c1   = Component(80, self.ch1, font_size=13, bg_color=0)
        self.c1.set_position(0, 0)
        self.c1.set_text(time.strftime('%d-%b-%y'), x=10)

        self.c2   = Component(48, self.ch1, font_size=13, bg_color=255)
        self.c2.set_position(80, 0)
        self.c2.set_text(time.strftime('%H:%M'), x=4)
#        self.c2.draw_borders()
    # ----------------
        self.separator1 = Separator(self.width, self.sh1, bg_color=255)
        self.separator1.set_position(0, self.sep_1_y)

        self.ti   = Component(self.ch2, self.ch2, font='fonts/weathericons-regular-webfont.ttf', font_size=20)
        self.ti.set_position(0, self.row_1_y)
        self.ti.set_text(u'\uF055', x=0, align=1) # Temperature
        
        self.tv   = Component(64, self.ch2, font_size=18)
        self.tv.set_position(24, self.row_1_y)
        self.tv.set_text(str(self.temperature))

        self.tu   = Component(40, self.ch2, font='fonts/weathericons-regular-webfont.ttf', font_size=24)
        self.tu.set_position(88, self.row_1_y)
        self.tu.set_text(u'\uF03C', x=0, align=0)

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.pi   = Component(self.ch2, self.ch2, font='fonts/weathericons-regular-webfont.ttf', font_size=20)
        self.pi.set_position(0, self.row_2_y)
        self.pi.set_text(u'\uF079', x=0, align=1) # Pressure

        self.pv   = Component(64, self.ch2, font_size=18)
        self.pv.set_position(24, self.row_2_y)
        self.pv.set_text(str(self.pressure))

        self.pu   = Component(40, self.ch2, font_size=16)
        self.pu.set_position(88, self.row_2_y)
        self.pu.set_text("hPa", 0, align=0) 

        self.separator3 = Separator(self.width, self.sh1)
        self.separator3.set_position(0, self.sep_3_y)

        self.hi   = Component(self.ch2, self.ch2, font='fonts/weathericons-regular-webfont.ttf', font_size=20)
        self.hi.set_position(0, self.row_3_y)
        self.hi.set_text(u'\uF07A', x=0, align=1) # Humidity

        self.hv   = Component(64, self.ch2, font_size=18)
        self.hv.set_position(24, self.row_3_y)
        self.hv.set_text(str(self.humidity))

        self.hu   = Component(40, self.ch2, font_size=16)
        self.hu.set_position(88, self.row_3_y)
        self.hu.set_text("RH", x=0, align=0)

        self.separator4 = Separator(self.width, self.sh1, bg_color=255)
        self.separator4.set_position(0, self.sep_4_y)

        self.qi   = Component(self.ch2, self.ch2, iw=self.ch2, ih=self.ch2, image='icons/iaq-house.png')
        self.qi.set_position(0, self.row_4_y)
#        self.qi.draw_borders()

        self.qv   = Component(56, self.ch2, font_size=18)
        self.qv.set_position(32, self.row_4_y)
        self.qv.set_text(str(self.air_quality))

        self.qu   = Component(40, self.ch2, font_size=16)
        self.qu.set_position(88, self.row_4_y)
        self.qu.set_text("%", x=0, align=0)

        self.separator5 = Separator(self.width, 3, bg_color=0)
        self.separator5.set_position(0, self.sep_5_y)

        # --------------------------------------------------

        self.c11   = Component(56, 56, iw=56, ih=56, image='icons/fan_200.png')
        self.c11.set_position(0, self.row_5_y + self.ch2)

        self.c12   = Component(56, 56, iw=56, ih=56, image='icons/fan_200.png')
        self.c12.set_position(64, self.row_5_y + self.ch2, r=180)

#----
        # Add components to the layout
#        self.epd.add([self.c1, self.c2, self.separator1])
        self.epd.add([self.c1, self.c2])
        self.epd.add([self.ti, self.tv, self.tu, self.separator2, self.pi, self.pv, self.pu, self.separator3])
        self.epd.add([self.hi, self.hv, self.hu, self.separator4, self.qi, self.qv, self.qu])
        self.epd.add([self.separator5, self.c11, self.c12])

        self.epd.show()

    def inc_temperature(self, increase):
        self.temperature += increase
        self.tv.set_text(str(self.temperature))

    def inc_humidity(self, increase):
        self.humidity += increase
        self.hv.set_text(str(self.humidity))

    def inc_pressure(self, increase):
        self.pressure += increase
        # TODO: set if value changed
        self.pv.set_text(str(round(self.pressure, 1)))

    def inc_air_quality(self, increase):
        self.air_quality += increase
        self.qv.set_text(str(self.air_quality))


if __name__ == '__main__':

    L1 = Layout_1()

    for i in range(10):
        L1.inc_temperature(.38)
        L1.inc_pressure(0.06)
        L1.epd.update_1b1()

    L1.epd.refresh()

    for i in range(10):
        L1.inc_temperature(.38)
        L1.inc_pressure(0.06)
        L1.inc_humidity(.25)
        L1.inc_air_quality(-0.31)
        L1.epd.update()

    raw_input()
