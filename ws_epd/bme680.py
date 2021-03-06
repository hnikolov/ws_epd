# -*- coding: utf-8 -*-
import time
from layout import Layout
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
# TODO: Date and time as a separate component?

class BME680(Layout):
    def __init__(self):
        super(BME680, self).__init__()

        self.ch1     =  20 # component height 1
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
        self.sdate       = time.strftime('%d-%b')
        self.stime       = time.strftime('%H:%M')


        # Build the layout
        self.cdate   = Component(72, self.ch1, font_size=18, bg_color=0)
        self.cdate.set_position(0, 0)
        self.cdate.set_text(self.sdate, align=1)

        self.ctime   = Component(56, self.ch1, font_size=18, bg_color=255)
        self.ctime.set_position(72, 0)
        self.ctime.set_text(self.stime, x=3)
#        self.ctime.draw_borders()

        # --------------------------------------------------

        self.separator1 = Separator(self.width, self.sh1, bg_color=255)
        self.separator1.set_position(0, self.sep_1_y)

        self.ti   = Component(self.ch2, self.ch2, font='weathericons-regular-webfont.ttf', font_size=20)
        self.ti.set_position(0, self.row_1_y)
        self.ti.set_text(u'\uF055', x=0, align=1) # Temperature

        self.tv   = Component(64, self.ch2, font_size=18)
        self.tv.set_position(24, self.row_1_y)
        self.tv.set_text(str(self.temperature))

        self.tu   = Component(40, self.ch2, font='weathericons-regular-webfont.ttf', font_size=24)
        self.tu.set_position(88, self.row_1_y)
        self.tu.set_text(u'\uF03C', x=0, align=0)

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.pi   = Component(self.ch2, self.ch2, font='weathericons-regular-webfont.ttf', font_size=20)
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

        self.hi   = Component(self.ch2, self.ch2, font='weathericons-regular-webfont.ttf', font_size=20)
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

        self.qi   = Component(self.ch2, self.ch2, iw=self.ch2, ih=self.ch2, image='iaq-house.png')
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

        self.c11   = Component(56, 56, iw=56, ih=56, image='fan_200.png')
        self.c11.set_position(0, self.row_5_y + self.ch2)

        self.c12   = Component(56, 56, iw=56, ih=56, image='fan_200.png')
        self.c12.set_position(64, self.row_5_y + self.ch2, r=180)

        #-- Add components to the layout --
#        self.add([self.cdate, self.ctime, self.separator1])
        self.add([self.cdate, self.ctime])
        self.add([self.ti, self.tv, self.tu, self.separator2, self.pi, self.pv, self.pu, self.separator3])
        self.add([self.hi, self.hv, self.hu, self.separator4, self.qi, self.qv, self.qu])
        self.add([self.separator5, self.c11, self.c12])


    # Note: inc_() used for testing, to be removed
    def inc_temperature(self, increase):
        self.temperature += increase
        self.tv.set_text("{0:.2f}".format(self.temperature))

    def inc_pressure(self, increase):
        self.pressure += increase
        # TODO: set if value changed
        self.pv.set_text("{0:.1f}".format(self.pressure))

    def inc_humidity(self, increase):
        self.humidity += increase
        self.hv.set_text("{0:.2f}".format(self.humidity))

    def inc_air_quality(self, increase):
        self.air_quality += increase
        self.qv.set_text("{0:.2f}".format(self.air_quality))
    # -----------------------------------------

    def set_temperature(self, value):
        if self.temperature != value:
            self.temperature = value
            self.tv.set_text("{0:.2f}".format(self.temperature))

    def set_pressure(self, value):
        if self.pressure != value:
            self.pressure = value
            self.pv.set_text("{0:.1f}".format(self.pressure))

    def set_humidity(self, value):
        if self.humidity != value:
            self.humidity = value
            self.hv.set_text("{0:.2f}".format(self.humidity))

    def set_air_quality(self, value):
        if self.air_quality != value:
            self.air_quality = value
            self.qv.set_text("{0:.2f}".format(self.air_quality))

    def set_date_time(self):
        tdate = time.strftime('%d-%b')
        ttime = time.strftime('%H:%M')

        if self.sdate != tdate:
            self.sdate = tdate
            self.cdate.set_text(self.sdate, x=10)

        if self.stime != ttime:
            self.stime = ttime
            self.ctime.set_text(self.stime, x=4)


if __name__ == '__main__':

    from epd import EPD

    # Display layout instance
    L1 = BME680()

    # E-Paper Display instance
    epd = EPD(True, L1)

    for i in range(5):
        L1.inc_temperature(.38)
        L1.inc_pressure(0.06)
        L1.set_date_time()
        epd.update()

    for i in range(5):
        L1.inc_temperature(.38)
        L1.inc_pressure(0.06)
        L1.inc_humidity(.25)
        L1.inc_air_quality(-0.31)
        L1.set_date_time()
        epd.update()

    raw_input()
