# -*- coding: utf-8 -*-
import time
from component import Component, Separator

class Layout_1:
    def __init__(self):
        self.components  = []
                
        self.width   = 128 # epd2in13.EPD_WIDTH
        self.height  = 250 # epd2in13.EPD_HEIGHT
        self.ch1     =  18 # component height 1
        self.ch2     =  24 # component height 2
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
        self.row_5_y = self.sep_5_y + self.sh1 + 4
        self.sep_6_y = self.row_5_y + self.ch2
        self.row_6_y = self.sep_6_y + self.sh1
        self.sep_7_y = self.row_6_y + self.ch2
        self.row_7_y = self.sep_7_y + self.sh1
        self.sep_8_y = self.row_7_y + self.ch2
        self.row_8_y = self.sep_8_y + self.sh1

        # Random values for test
        self.water    = 890
        self.gas      = 2.64
        self.elec     = 0
        self.day_elec = 12.3
        self.sdate    = time.strftime('%d-%b-%y')
        self.stime    = time.strftime('%H:%M')

        self.eur_water  = 0.23
        self.eur_gas    = 0.66
        self.eur_energy = 1.79
        self.eur_total  = self.eur_water + self.eur_gas + self.eur_energy
        
        # Build the layout
        self.cdate   = Component(80, self.ch1, font_size=14, bg_color=0)
        self.cdate.set_position(0, 0)
        self.cdate.set_text(self.sdate, align=1)

        self.ctime   = Component(48, self.ch1, font_size=14, bg_color=255)
        self.ctime.set_position(80, 0)
        self.ctime.set_text(self.stime, x=4)
#        self.ctime.draw_borders()
    # ----------------
        self.separator1 = Separator(self.width, self.sh1, bg_color=255)
        self.separator1.set_position(0, self.sep_1_y)

        self.wi   = Component(self.ch2, self.ch2, font_size=20, image='tap-water1.jpg')
        self.wi.set_position(0, self.row_1_y)
#        self.wi.draw_borders()

        self.wv   = Component(56, self.ch2, font_size=18)
        self.wv.set_position(32, self.row_1_y)
        self.wv.set_text(str(self.water))

        self.wu   = Component(40, self.ch2, font_size=16)
        self.wu.set_position(88, self.row_1_y)
        self.wu.set_text("Lit", 0, align=0)

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)

        self.gi   = Component(self.ch2, self.ch2, font_size=20, image='gas_32x32.png')
        self.gi.set_position(0, self.row_2_y)

        self.gv   = Component(56, self.ch2, font_size=18)
        self.gv.set_position(32, self.row_2_y)
        self.gv.set_text(str(self.gas))

        self.gu   = Component(40, self.ch2, font_size=16)
        self.gu.set_position(88, self.row_2_y)
        self.gu.set_text("m" + u'\u00B3', 0, align=0)

        self.separator3 = Separator(self.width, self.sh1)
        self.separator3.set_position(0, self.sep_3_y)

        self.pi   = Component(self.ch2, self.ch2, font_size=20, image='plug1.png')
        self.pi.set_position(0, self.row_3_y)

        self.pv   = Component(56, self.ch2, font_size=18)
        self.pv.set_position(32, self.row_3_y)
        self.pv.set_text("{0:.3f}".format(self.elec))

        self.pu   = Component(40, self.ch2, font_size=16)
        self.pu.set_position(88, self.row_3_y)
        self.pu.set_text("kWh", 0, align=0)

        self.separator4 = Separator(self.width, self.sh1, bg_color=255)
        self.separator4.set_position(0, self.sep_4_y)

        self.ei   = Component(self.ch2, self.ch2, font_size=20, image='power_32x32.png')
        self.ei.set_position(0, self.row_4_y)

        self.ev   = Component(56, self.ch2, font_size=18)
        self.ev.set_position(32, self.row_4_y)
        self.ev.set_text("{0:.3f}".format(self.day_elec))

        self.eu   = Component(40, self.ch2, font_size=16)
        self.eu.set_position(88, self.row_4_y)
        self.eu.set_text("kWh", 0, align=0)

        self.separator5 = Separator(self.width, 3, bg_color=0)
        self.separator5.set_position(0, self.sep_5_y)
        # --------------------------------------------------

        # Euro water
        self.ewi   = Component(self.ch2, self.ch2, font_size=20, image='tap-water1.jpg')
        self.ewi.set_position(0, self.row_5_y)

        self.ewv   = Component(56, self.ch2, font_size=18)
        self.ewv.set_position(32, self.row_5_y)
        self.ewv.set_text("{0:.2f}".format(self.eur_water))

        self.ewu   = Component(40, self.ch2, font_size=16)
        self.ewu.set_position(88, self.row_5_y)
        self.ewu.set_text(u'\u20AC', x=0, align=0) # Euro
        
        # Euro gas
        self.egi   = Component(self.ch2, self.ch2, font_size=20, image='gas_32x32.png')
        self.egi.set_position(0, self.row_6_y)
        # self.egi.set_text('+', x=0, align=1)

        self.egv   = Component(56, self.ch2, font_size=18)
        self.egv.set_position(32, self.row_6_y)
        self.egv.set_text("{0:.2f}".format(self.eur_gas))

        self.egu   = Component(40, self.ch2, font_size=16)
        self.egu.set_position(88, self.row_6_y)
        self.egu.set_text(u'\u20AC', x=0, align=0) # Euro       
        
        # Euro energy
        self.eei   = Component(self.ch2, self.ch2, font_size=20, image='power_32x32.png')
        self.eei.set_position(0, self.row_7_y)

        self.eev   = Component(56, self.ch2, font_size=18)
        self.eev.set_position(32, self.row_7_y)
        self.eev.set_text("{0:.2f}".format(self.eur_energy))

        self.eeu   = Component(40, self.ch2, font_size=16)
        self.eeu.set_position(88, self.row_7_y)
        self.eeu.set_text(u'\u20AC', x=0, align=0) # Euro 

        self.separator8 = Separator(self.width, 3, bg_color=255, x2=96)
        self.separator8.set_position(0, self.sep_8_y)

        # Euro total
        self.eti   = Component(self.ch2, self.ch2, font_size=22)
        self.eti.set_position(0, self.row_8_y)
        self.eti.set_text(u'\u03A3', x=0, align=1) # Sigma

        self.etv   = Component(56, self.ch2, font_size=18)
        self.etv.set_position(32, self.row_8_y)
        self.etv.set_text("{0:.2f}".format(self.eur_total))

        self.etu   = Component(40, self.ch2, font_size=16)
        self.etu.set_position(88, self.row_8_y)
        self.etu.set_text(u'\u20AC', x=0, align=0) # Euro 

        # Add components to the layout
        self.add([self.cdate, self.ctime])
        self.add([self.wi, self.wv, self.wu, self.separator2, self.gi, self.gv, self.gu, self.separator3])
        self.add([self.pi, self.pv, self.pu, self.separator4, self.ei, self.ev, self.eu, self.separator5])
        self.add([self.ewi, self.ewv, self.ewu, self.egi, self.egv, self.egu, self.eei, self.eev, self.eeu])
        self.add([self.separator8, self.eti, self.etv, self.etu])


    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )
        

    def inc_water(self, increase):
        self.water += increase
        self.wv.set_text(str(self.water))

    def set_water(self, value):
        self.water = value
        self.wv.set_text(str(self.water))

    def set_elec(self, value):
        self.elec = value
        self.pv.set_text("{0:.3f}".format(self.elec))

    def inc_day_elec(self, increase):
        self.day_elec += increase
        self.ev.set_text("{0:.3f}".format(self.day_elec))

    def set_day_elec(self, value):
        self.day_elec = value
        self.ev.set_text("{0:.3f}".format(self.day_elec))

    def inc_gas(self, increase):
        self.gas += increase
        self.gv.set_text("{0:.2f}".format(self.gas))

    def set_gas(self, value):
        self.gas = value
        self.gv.set_text("{0:.2f}".format(self.gas))

    def clear_all(self):
        self.set_water(0)
        self.set_elec(0)
        self.set_day_elec(0)
        self.set_gas(0)


    def set_date_time(self):
        tdate = time.strftime('%d-%b-%y')
        ttime = time.strftime('%H:%M')
        
        if self.sdate != tdate:
            self.sdate = tdate
            self.cdate.set_text(self.sdate, x=10)
    
        if self.stime != ttime:
            self.stime = ttime
            self.ctime.set_text(self.stime, x=4)
            
            
if __name__ == '__main__':

    from epd import EPD

    # Display Layout instance
    L1 = Layout_1()
    
    # E-Paper Display instance
    epd = EPD(False)
    epd.add( L1.components )

    epd.refresh()
#    self.epd.clear()
    epd.show()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.set_date_time()
        epd.update_1b1()

    epd.refresh()
    L1.clear_all()
    epd.update()

    for i in range(10):
        L1.inc_water(1)
        L1.inc_gas(0.01)
        L1.set_date_time()
        epd.update()

    raw_input()

#    for k,v in icons_list.iteritems():
#        print k, hex(ord(v)) #, unichr(ord(v))
