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

font_weather_icons = ImageFont.truetype('fonts/weathericons-regular-webfont.ttf', 35)
#draw.text((30,330),icons_list[str(icon)],font=font_weather_icons,fill=255)

at_once = True

class Layout_1:
    def __init__(self):
        self.width   = 128 # epd2in13.EPD_WIDTH
        self.height  = 250 # epd2in13.EPD_HEIGHT
        self.ch1     =  15 # component height 1
        self.ch2     =  26 # component height 2
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

        # Random values for test
        self.water   = 890
        self.gas     = 2.64
        self.elec    = 12.3

        # E-Paper Display instance
        self.epd = EPD(False)
        self.epd.refresh()
#        self.epd.clear()

        # Build the layout
        self.c1   = Component(80, self.ch1, 13, bg_color=0)
        self.c1.set_position(0, 0)
        self.c1.set_text(time.strftime('%d-%b-%y'), 10)

        self.c2   = Component(48, self.ch1, 13, bg_color=255)
        self.c2.set_position(80, 0)
        self.c2.set_text(time.strftime('%H:%M'), 4)
        self.c2.draw_borders()
    # ----------------
        self.separator1 = Separator(self.width, self.sh1, bg_color=255)
        self.separator1.set_position(0, self.sep_1_y)

        self.c3   = Component(self.ch2, self.ch2, 20, image='icons/tap-water1.jpg')
        self.c3.set_position(0, self.row_1_y)
        self.c3.draw_borders()

        self.c4   = Component(88, self.ch2, 18)
        self.c4.set_position(32, self.row_1_y)
        self.c4.set_text(str(self.water) + " L")
#        self.c4.draw_borders()

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.c5   = Component(self.ch2, self.ch2, 20, image='icons/gas_32x32.png')
        self.c5.set_position(0, self.row_2_y)

#        self.c6   = Component(89, self.ch2, 18, bg_color=0)
        self.c6   = Component(89, self.ch2, 18)
        self.c6.set_position(32, self.row_2_y)
        self.c6.set_text(str(self.gas) + " m3")
#        self.c6.draw_borders()

#        self.separator3 = Separator(self.width, 3, 3, bg_color=0)
        self.separator3 = Separator(self.width, self.sh1)
        self.separator3.set_position(0, self.sep_3_y)

        self.c7   = Component(self.ch2, self.ch2, 20, image='icons/plug1.png')
        self.c7.set_position(0, self.row_3_y)
        self.c7.draw_borders()

        self.c8   = Component(96, self.ch2, 18)
        self.c8.set_position(32, self.row_3_y)
        self.c8.set_text("12.3 kWh", 5)
        self.c8.draw_borders()

    # --------------------------------------------------
        self.separator4 = Separator(self.width, self.sh1, bg_color=255)
        self.separator4.set_position(0, self.sep_4_y)

        self.c9   = Component(128, 6, 6, bg_color=0)
        self.c9.set_position(0, self.row_4_y)

        self.c10   = Component(128, 18, 16)
        self.c10.set_position(0, self.row_4_y + 6)
        self.c10.set_text("C10, TBD", x=12)
        self.c10.draw_borders()

#        self.c11   = Component(self.ch2, self.ch2, 20, image='icons/power.png')
        self.c11   = Component(self.ch2, self.ch2, 20, image='icons/iaq-house.png')
        self.c11.set_position(0, self.row_4_y + 6 + self.ch2)
        self.c11.draw_borders()

        self.c12   = Component(self.ch2, self.ch2, 20, image='icons/emeter_32x32.png')
        self.c12.set_position(40, self.row_4_y + 6 + self.ch2)
        self.c12.draw_borders()

#        self.c13     = Component(32, self.ch2, 20, image='icons/thermometer2_32x32.png')
        self.c13     = Component(self.ch2, self.ch2, 20, image='icons/euro-512.png')
        self.c13.set_position(80, self.row_4_y + 6 + self.ch2, 90)

        # Add components to the layout
        self.epd.add([self.c1, self.c2, self.separator1])
        self.epd.add([self.c3, self.c4, self.separator2, self.c5, self.c6, self.separator3])
        self.epd.add([self.c7, self.c8, self.separator4, self.c9, self.c10, self.c11, self.c12, self.c13])

#        self.epd.update()
        self.epd.show()

    def inc_water(self, increase):
        self.water += increase
        self.c4.set_text(str(self.water) + " L")

    def inc_gas(self, increase):
        self.gas += increase
        self.c6.set_text(str(self.gas) + " m3", align=1)

    def clear_all(self):
        self.water = 0
        self.c4.clear()
        self.c4.set_text(str(self.water) + " L")
        self.gas = 0
        self.c6.clear()
        self.c6.set_text(str(self.gas) + " m3")
        self.epd.update()


if __name__ == '__main__':

    L1 = Layout_1()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.epd.update_1b1()
#        L1.epd.update()

    L1.epd.refresh()
#    L1.epd.clear()
    L1.clear_all()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.epd.update()
#        L1.epd.update_1b1()

    raw_input()

#    for k,v in icons_list.iteritems():
#        print k, hex(ord(v)) #, unichr(ord(v))
