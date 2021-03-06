# -*- coding: utf-8 -*-
import time
from layout import Layout
from component import Component, Separator, BarGraph

class Layout_2(Layout):
    def __init__(self):
        super(Layout_2, self).__init__()

        self.ch1     = 18 # component height 1
        self.ch2     = 24 # component height 2
        self.sh1     =  3 # separator height 1
        self.bar     = 16

        # Offsets
        self.sep_1_y = self.ch1 # after (date and time)
        self.row_1_y = self.sep_1_y + self.sh1 + 2
        self.sep_2_y = self.row_1_y + self.ch2
        self.row_2_y = self.sep_2_y + self.sh1
        self.sep_3_y = self.row_2_y + self.ch2
        self.row_3_y = self.sep_3_y + self.sh1
        self.sep_4_y = self.row_3_y + self.ch2
        self.row_4_y = self.sep_4_y + self.sh1
        self.sep_5_y = self.row_4_y + self.ch2
        self.row_5_y = self.sep_5_y + self.sh1 + self.bar + 1
        self.sep_6_y = self.row_5_y + self.ch2
        self.row_6_y = self.sep_6_y + self.sh1 - 1
        self.sep_7_y = self.row_6_y + self.ch2 - 1
        self.row_7_y = self.sep_7_y + self.sh1
        self.sep_8_y = self.row_7_y + self.ch2 - 1
        self.row_8_y = self.sep_8_y + self.sh1 - 1

#        self.sdate           = time.strftime('%d-%b-%y')
        self.sdate           = time.strftime('%d-%b')
        self.stime           = time.strftime('%H:%M')

        # Random values for test
        self.water           = 0
        self.gas             = 0.0
        self.electricity     = 0
        self.day_electricity = 0.0

        self.eur_water       = 0.0
        self.eur_gas         = 0.0
        self.eur_electricity = 1.0
        self.eur_total       = self.eur_water + self.eur_gas + self.eur_electricity

        # Build the layout
        self.cdate   = Component(72, self.ch1, font_size=18, bg_color=0)
        self.cdate.set_position(0, 0)
        self.cdate.set_text(self.sdate, align=1)

        self.ctime   = Component(64, self.ch1, font_size=17, bg_color=255)
        self.ctime.set_position(72, 0)
        self.ctime.set_text(self.stime, x=5)
#        self.ctime.draw_borders()
        # ----------------
        self.separator1 = Separator(self.width, self.sh1, bg_color=255)
        self.separator1.set_position(0, self.sep_1_y)

        self.wi   = Component(self.ch2, self.ch2, font_size=20, image='tap-water1.jpg')
        self.wi.set_position(8, self.row_1_y)
#        self.wi.draw_borders()

        self.wv   = Component(64, self.ch2, font_size=18)
        self.wv.set_position(32, self.row_1_y)
        self.wv.set_text(str(self.water))

        self.wu   = Component(32, self.ch2, font_size=16)
        self.wu.set_position(96, self.row_1_y)
        self.wu.set_text("Lit", 0, align=0)

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.gi   = Component(self.ch2, self.ch2, font_size=20, image='gas_32x32.png')
        self.gi.set_position(8, self.row_2_y)

        self.gv   = Component(64, self.ch2, font_size=18)
        self.gv.set_position(32, self.row_2_y)
        self.gv.set_text(str(self.gas))

        self.gu   = Component(32, self.ch2, font_size=16)
        self.gu.set_position(96, self.row_2_y)
        self.gu.set_text("m" + u'\u00B3', 0, align=0)

        self.separator3 = Separator(self.width, self.sh1)
        self.separator3.set_position(0, self.sep_3_y)

        self.ei   = Component(self.ch2, self.ch2, font_size=20, image='power_32x32.png')
        self.ei.set_position(8, self.row_3_y)

        self.ev   = Component(64, self.ch2, font_size=18)
        self.ev.set_position(32, self.row_3_y)
        self.ev.set_text("{0:.3f}".format(self.day_electricity))

        self.eu   = Component(32, self.ch2, font_size=16)
        self.eu.set_position(96, self.row_3_y)
        self.eu.set_text("kW", 0, align=0)

        self.separator4 = Separator(self.width, self.sh1, bg_color=255)
        self.separator4.set_position(0, self.sep_4_y)

        self.pi   = Component(self.ch2, self.ch2, font_size=20, image='plug1.png')
        self.pi.set_position(8, self.row_4_y)

        self.pv   = Component(64, self.ch2, font_size=18)
        self.pv.set_position(32, self.row_4_y)
        self.pv.set_text("{0:.3f}".format(self.electricity))

        self.pu   = Component(32, self.ch2, font_size=16)
        self.pu.set_position(96, self.row_4_y)
        self.pu.set_text("/ h", 0, align=0)

        self.egraph = BarGraph(128, self.bar, bg_color=255)
        self.egraph.set_position(0, self.sep_5_y)
        self.egraph.update()
        # --------------------------------------------------

        # Euro water
        self.ewi   = Component(self.ch2, self.ch2, font_size=20, image='tap-water1.jpg')
        self.ewi.set_position(8, self.row_5_y)

        self.ewv   = Component(56, self.ch2, font_size=18, bg_color=255)
        self.ewv.set_position(40, self.row_5_y)
        self.ewv.set_text("{0:.2f}".format(self.eur_water))

        self.ewu   = Component(32, self.ch2, font_size=16, bg_color=255)
        self.ewu.set_position(96, self.row_5_y)
        self.ewu.set_text(u'\u20AC', x=0, align=0) # Euro

        # Euro gas
        self.egi   = Component(self.ch2, self.ch2, font_size=20, image='gas_32x32.png')
        self.egi.set_position(8, self.row_6_y)
        # self.egi.set_text('+', x=0, align=1)

        self.egv   = Component(56, self.ch2, font_size=18, bg_color=255)
        self.egv.set_position(40, self.row_6_y)
        self.egv.set_text("{0:.2f}".format(self.eur_gas))

        self.egu   = Component(32, self.ch2, font_size=16, bg_color=255)
        self.egu.set_position(96, self.row_6_y)
        self.egu.set_text(u'\u20AC', x=0, align=0) # Euro

        # Euro electricity
        self.eei   = Component(self.ch2, self.ch2, font_size=20, image='power_32x32.png')
        self.eei.set_position(8, self.row_7_y)

        self.eev   = Component(56, self.ch2, font_size=18, bg_color=255)
        self.eev.set_position(40, self.row_7_y)
        self.eev.set_text("{0:.2f}".format(self.eur_electricity))

        self.eeu   = Component(32, self.ch2, font_size=16, bg_color=255)
        self.eeu.set_position(96, self.row_7_y)
        self.eeu.set_text(u'\u20AC', x=0, align=0) # Euro

        self.separator8 = Separator(self.width, height=3, bg_color=255, x1=40, x2=104)
        self.separator8.set_position(0, self.sep_8_y)

        # Euro total
        self.eti   = Component(self.ch2, self.ch2, font_size=22)
        self.eti.set_position(8, self.row_8_y)
        self.eti.set_text(u'\u03A3', x=0, align=1) # Sigma

        self.etv   = Component(64, self.ch2, font_size=18)
        self.etv.set_position(32, self.row_8_y)
        self.etv.set_text("{0:.2f}".format(self.eur_total))

        self.etu   = Component(32, self.ch2, font_size=16)
        self.etu.set_position(96, self.row_8_y)
        self.etu.set_text(u'\u20AC', x=0, align=0) # Euro

        # Add components to the layout
        self.add([self.cdate, self.ctime])
        self.add([self.wi, self.wv, self.wu, self.separator2, self.gi, self.gv, self.gu, self.separator3])
        self.add([self.ei, self.ev, self.eu, self.separator4, self.pi, self.pv, self.pu, self.egraph])
        self.add([self.ewi, self.ewv, self.ewu, self.egi, self.egv, self.egu, self.eei, self.eev, self.eeu])
        self.add([self.separator8, self.eti, self.etv, self.etu])


    def inc_water(self, increase):
#        self.wv.color_invert()
        self.water += increase
        self.wv.set_text(str(self.water))

    def set_water(self, value):
        if self.water != value:
            self.water = value
            self.wv.set_text(str(self.water))

    def set_eur_water(self, value):
        if self.eur_water != value:
            self.eur_water = value
            self.ewv.set_text("{0:.2f}".format(self.eur_water))

    def inc_gas(self, increase):
        self.gas += increase
        self.gv.set_text("{0:.2f}".format(self.gas))

    def set_gas(self, value):
        if self.gas != value:
            self.gas = value
            self.gv.set_text("{0:.2f}".format(self.gas))

    def set_eur_gas(self, value):
        if self.eur_gas != value:
            self.eur_gas = value
            self.egv.set_text("{0:.2f}".format(self.eur_gas))

    def set_electricity(self, value):
        if self.electricity != value:
            self.electricity = value
            self.pv.set_text("{0:.3f}".format(self.electricity))

    def inc_electricity(self, increase):
        self.electricity += increase
        self.pv.set_text("{0:.3f}".format(self.electricity))

    def inc_day_electricity(self, increase):
        self.day_electricity += increase
        self.ev.set_text("{0:.3f}".format(self.day_electricity))

    def set_day_electricity(self, value):
        if self.day_electricity != value:
            self.day_electricity = value
            self.ev.set_text("{0:.3f}".format(self.day_electricity))

    def set_eur_electricity(self, value):
        if self.eur_electricity != value:
            self.eur_electricity = value
            self.eev.set_text("{0:.2f}".format(self.eur_electricity))

    def set_eur_total(self, value):
        if self.eur_total != value:
            self.eur_total = value
            self.etv.set_text("{0:.2f}".format(self.eur_total))

    def clear_all(self):
        self.set_water(0)
        self.set_gas(0)
        self.set_electricity(0)
        self.set_day_electricity(0)
        self.set_eur_water(0)
        self.set_eur_gas(0)
        self.set_eur_electricity(0)
        self.set_eur_total(0)
        self.egraph.clear_bars()


    def set_date_time(self):
#        tdate = time.strftime('%d-%b-%y')
        tdate = time.strftime('%d-%b')
        ttime = time.strftime('%H:%M')

        if self.sdate != tdate:
            self.sdate = tdate
            self.cdate.set_text(self.sdate, align=1)

        if self.stime != ttime:
            self.stime = ttime
            self.ctime.set_text(self.stime, x=5)


if __name__ == '__main__':

    from epd import EPD

    # Display Layout instance
    L2 = Layout_2()

    # E-Paper Display instance
    epd = EPD(False, L2, partial_update = True)
    
    # Random values for test
    L2.water           = 890
    L2.gas             = 2.64
    L2.electricity     = 0
    L2.day_electricity = 12.3

    L2.eur_water       = 0.23
    L2.eur_gas         = 0.66
    L2.eur_electricity = 1.79
    L2.eur_total       = L2.eur_water + L2.eur_gas + L2.eur_electricity

    for i in range(18):
        L2.egraph.set_bar(i, i+1)
    
    L2.egraph.set_bar(23,12.0)
        
    for i in range(5):
        L2.inc_water(1)
        L2.inc_gas(0.01)
        L2.set_date_time()
        L2.egraph.set_bar(18+i, 12 - (4 + i))
        epd.update()

    raw_input()
    
    L2.clear_all()
    epd.show()

        
    for i in range(5):
        L2.inc_water(1)
        L2.inc_gas(0.01)
        L2.set_date_time()
        L2.egraph.set_bar(i, 2*(i+1))
        epd.update()

    raw_input()
