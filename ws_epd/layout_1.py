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

# TODO: Fonts and icons taken from local ws_epd folders. Allow for absolute paths as well

class Layout_1:
    def __init__(self):
        self.width   = 128 # epd2in13.EPD_WIDTH
        self.height  = 250 # epd2in13.EPD_HEIGHT
        self.ch1     =  16 # component height 1
        self.ch2     =  26 # component height 2
        self.ch3     =  32 # component height 3
        self.sh1     =   3 # separator height 1

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
        self.water   = 890
        self.gas     = 2.64
        self.elec    = 12.3

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

        self.c3   = Component(self.ch2, self.ch2, font_size=20, image='tap-water1.jpg')
        self.c3.set_position(0, self.row_1_y)
#        self.c3.draw_borders()

        self.c4   = Component(56, self.ch2, font_size=18)
        self.c4.set_position(32, self.row_1_y)
        self.c4.set_text(str(self.water))

        self.u1   = Component(40, self.ch2, font_size=16)
        self.u1.set_position(88, self.row_1_y)
        self.u1.set_text("Lit", 0, align=0)

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.c5   = Component(self.ch2, self.ch2, font_size=20, image='gas_32x32.png')
        self.c5.set_position(0, self.row_2_y)

        self.c6   = Component(56, self.ch2, font_size=18)
        self.c6.set_position(32, self.row_2_y)
        self.c6.set_text(str(self.gas))

        self.u2   = Component(40, self.ch2, font_size=16)
        self.u2.set_position(88, self.row_2_y)
        self.u2.set_text("m" + u'\u00B3', 0, align=0)

        self.separator3 = Separator(self.width, self.sh1)
        self.separator3.set_position(0, self.sep_3_y)

        self.c7   = Component(self.ch2, self.ch2, font_size=20, image='plug1.png')
        self.c7.set_position(0, self.row_3_y)

        self.c8   = Component(56, self.ch2, font_size=18)
        self.c8.set_position(32, self.row_3_y)
        self.c8.set_text("1.345")

        self.u3   = Component(40, self.ch2, font_size=16)
        self.u3.set_position(88, self.row_3_y)
        self.u3.set_text("kWh", 0, align=0)

        self.separator4 = Separator(self.width, self.sh1, bg_color=255)
        self.separator4.set_position(0, self.sep_4_y)

        self.c77   = Component(self.ch2, self.ch2, font_size=20, image='power_32x32.png')
        self.c77.set_position(0, self.row_4_y)
#        self.c77.draw_borders()

        self.c88   = Component(56, self.ch2, font_size=18)
        self.c88.set_position(32, self.row_4_y)
        self.c88.set_text("12.678")

        self.u4   = Component(40, self.ch2, font_size=16)
        self.u4.set_position(88, self.row_4_y)
        self.u4.set_text("kWh", 0, align=0)
        # --------------------------------------------------

        self.separator5 = Separator(self.width, 3, bg_color=0)
        self.separator5.set_position(0, self.sep_5_y)

        self.c9   = Component(128, 6, font_size=6, bg_color=0)
        self.c9.set_position(0, self.row_5_y)

        self.c10   = Component(128, 18, font_size=16)
        self.c10.set_position(0, self.row_5_y + 6)
        self.c10.set_text("C10, TBD", x=12)
        self.c10.draw_borders()

        self.c11   = Component(self.ch3, self.ch3, iw=self.ch3-8, ih=self.ch3-8, image='fan_200.png')
        self.c11.set_position(0, self.row_5_y + 6 + self.ch2)

        self.c12   = Component(self.ch3, self.ch3, iw=self.ch3-8, ih=self.ch3-8, image='fan_200.png')
        self.c12.set_position(32, self.row_5_y + 6 + self.ch2, r=180)

#        self.c13   = Component(self.ch2, self.ch2, 20, image='icons/power.png')
        self.c13   = Component(self.ch3, self.ch3, iw=self.ch3-4, ih=self.ch3-4, image='iaq-house.png')
        self.c13.set_position(64, self.row_5_y + 6 + self.ch2)
        self.c13.draw_borders()

        self.c14   = Component(self.ch3, self.ch3, iw=self.ch3-8, ih=self.ch3-8, font_size=20, image='emeter_32x32.png')
        self.c14.set_position(96, self.row_5_y + 6 + self.ch2)
#        self.c14.draw_borders()

#----
        self.c16     = Component(self.ch3, self.ch3, font_size=24)
        self.c16.set_text(u'\u20AC', x=0, align=1) # Euro
#        self.c16     = Component(self.ch3, self.ch3, iw=self.ch3-4, ih=self.ch3-4, image='euro-512.png')
        self.c16.set_position(0, self.row_6_y + 6 + self.ch3)

        self.c17   = Component(self.ch3, self.ch3, font='weathericons-regular-webfont.ttf', font_size=20)
        self.c17.set_position(32, self.row_6_y + 6 + self.ch3)
        self.c17.set_text(u'\uF055', x=0, align=1)

        self.c18   = Component(self.ch3, self.ch3, font='weathericons-regular-webfont.ttf', font_size=23)
        self.c18.set_position(64, self.row_6_y + 6 + self.ch3)
        self.c18.set_text(u'\uF079', x=0, align=1)

        self.c19   = Component(self.ch3, self.ch3, font='weathericons-regular-webfont.ttf', font_size=23)
        self.c19.set_position(96, self.row_6_y + 6 + self.ch3)
        self.c19.set_text(u'\uF07A', x=0, align=1)


#----
        # Add components to the layout
#        self.epd.add([self.c1, self.c2, self.separator1])
        self.epd.add([self.c1, self.c2])
        self.epd.add([self.c3, self.c4, self.u1, self.separator2, self.c5, self.c6, self.u2, self.separator3])
        self.epd.add([self.c7, self.c8, self.u3, self.separator4, self.c77, self.c88, self.u4])
        self.epd.add([self.separator5, self.c10, self.c11, self.c12, self.c13, self.c14])
        self.epd.add([self.c16, self.c17, self.c18, self.c19])

        self.epd.show()

    def inc_water(self, increase):
        self.water += increase
        self.c4.set_text(str(self.water))

    def inc_gas(self, increase):
        self.gas += increase
        self.c6.set_text(str(self.gas))

    def clear_all(self):
        self.water = 0
        self.c4.set_text(str(self.water))
        self.gas = 0
        self.c6.set_text(str(self.gas))
        self.epd.update()


if __name__ == '__main__':

    L1 = Layout_1()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.epd.update_1b1()
#        L1.epd.update()

    L1.epd.refresh()
    L1.clear_all()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.epd.update()
#        L1.epd.update_1b1()

    raw_input()

#    for k,v in icons_list.iteritems():
#        print k, hex(ord(v)) #, unichr(ord(v))
