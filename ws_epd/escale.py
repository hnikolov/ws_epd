# -*- coding: utf-8 -*-
import time
from layout import Layout
from component import Component, Separator

class Escale(Layout):
    def __init__(self):
        super(Escale, self).__init__()
                
        self.ch1     =  20 # component height 1
        self.ch2     =  24 # component height 2
        self.sh1     =   3 # separator height 1

        # Offsets
        self.row_0_y = 0
        self.sep_1_y = self.row_0_y + self.ch1 # after (date and time)
        self.row_1_y = self.sep_1_y + self.sh1
        self.sep_2_y = self.row_1_y + self.ch2
        self.row_2_y = self.sep_2_y + self.sh1
        self.sep_3_y = self.row_2_y + self.ch2
        self.row_3_y = self.sep_3_y + self.sh1 + 6
#        self.sep_4_y = self.row_3_y + self.ch2
#        self.row_4_y = self.sep_4_y + self.sh1
        self.row_4_y = self.row_3_y + self.ch2
        self.sep_5_y = self.row_4_y + self.ch2
        self.row_5_y = self.sep_5_y + self.sh1
        self.sep_6_y = self.row_5_y + self.ch2
        self.row_6_y = self.sep_6_y + self.sh1 + 6
#        self.sep_7_y = self.row_6_y + self.ch2
#        self.row_7_y = self.sep_7_y + self.sh1
        self.row_7_y = self.row_6_y + self.ch2

        # Data variables
        self.value_1 = 0
        self.value_2 = 0
        self.value_3 = 0
        self.value_4 = 0
        self.value_5 = 0
        
        # Build the layout
        # ----------------
        self.h1  = Component(self.width, self.ch1, bg_color=0, font_size=16)
        self.h1.set_position(0, self.row_0_y)
        self.h1.set_text("0.25g resolution", align=1)
        
        self.v1i  = Component(self.ch2, self.ch2, font_size=14)
        self.v1i.set_position(0, self.row_1_y)
        self.v1i.set_text('1', x=0, align=1) # 1 sample (no averaging)

        self.v1v  = Component(64, self.ch2, font_size=18)
        self.v1v.set_position(32, self.row_1_y)
        self.v1v.set_text("{0:.2f}".format(self.value_1))

        self.v1u  = Component(32, self.ch2, font_size=16)
        self.v1u.set_position(96, self.row_1_y)
        self.v1u.set_text('g', x=0, align=0) # grams

        self.separator2 = Separator(self.width, self.sh1, bg_color=255)
        self.separator2.set_position(0, self.sep_2_y)
        
        self.v2i  = Component(self.ch2, self.ch2, font_size=14)
        self.v2i.set_position(0, self.row_2_y)
        self.v2i.set_text('4', x=0, align=1) # Average of 4 samples

        self.v2v  = Component(64, self.ch2, font_size=18)
        self.v2v.set_position(32, self.row_2_y)
        self.v2v.set_text("{0:.2f}".format(self.value_2))

        self.v2u  = Component(32, self.ch2, font_size=16)
        self.v2u.set_position(96, self.row_2_y)
        self.v2u.set_text('g', x=0, align=0) # grams
      
        # ----------------
        self.h2  = Component(self.width, self.ch1, bg_color=0, font_size=16)
        self.h2.set_position(0, self.row_3_y)
        self.h2.set_text("0.5g resolution", align=1)
        
        self.v3i  = Component(self.ch2, self.ch2, font_size=14)
        self.v3i.set_position(0, self.row_4_y)
        self.v3i.set_text('1', x=0, align=1) # 1 sample (no averaging)

        self.v3v  = Component(64, self.ch2, font_size=18)
        self.v3v.set_position(32, self.row_4_y)
        self.v3v.set_text("{0:.2f}".format(self.value_3))

        self.v3u  = Component(32, self.ch2, font_size=16)
        self.v3u.set_position(96, self.row_4_y)
        self.v3u.set_text('g', x=0, align=0) # grams

        self.separator5 = Separator(self.width, self.sh1, bg_color=255)
        self.separator5.set_position(0, self.sep_5_y)
        
        self.v4i  = Component(self.ch2, self.ch2, font_size=14)
        self.v4i.set_position(0, self.row_5_y)
        self.v4i.set_text('4', x=0, align=1) # Average of 4 samples

        self.v4v  = Component(64, self.ch2, font_size=18)
        self.v4v.set_position(32, self.row_5_y)
        self.v4v.set_text("{0:.2f}".format(self.value_4))

        self.v4u  = Component(32, self.ch2, font_size=16)
        self.v4u.set_position(96, self.row_5_y)
        self.v4u.set_text('g', x=0, align=0) # grams       
        
        # ----------------
        self.h3  = Component(self.width, self.ch1, bg_color=0, font_size=16)
        self.h3.set_position(0, self.row_6_y)
        self.h3.set_text("1g resolution", align=1)
        
        self.v5i  = Component(self.ch2, self.ch2, font_size=14)
        self.v5i.set_position(0, self.row_7_y)
        self.v5i.set_text('1', x=0, align=1) # 1 sample (no averaging)

        self.v5v  = Component(64, self.ch2, font_size=18)
        self.v5v.set_position(32, self.row_7_y)
        self.v5v.set_text("{0:.2f}".format(self.value_5))

        self.v5u  = Component(32, self.ch2, font_size=16)
        self.v5u.set_position(96, self.row_7_y)
        self.v5u.set_text('g', x=0, align=0) # grams        
 
        # Add components to the layout
        self.add([self.h1, self.v1i, self.v1v, self.v1u, self.separator2, self.v2i, self.v2v, self.v2u])
        self.add([self.h2, self.v3i, self.v3v, self.v3u, self.separator5, self.v4i, self.v4v, self.v4u])
        self.add([self.h3, self.v5i, self.v5v, self.v5u])


    def set_value_1(self, value):
        if self.value_1 != value:
            self.value_1 = value
            self.v1v.set_text("{0:.2f}".format(self.value_1))

    def set_value_2(self, value):
        if self.value_2 != value:
            self.value_2 = value
            self.v2v.set_text("{0:.2f}".format(self.value_2))

    def set_value_3(self, value):
        if self.value_3 != value:
            self.value_3 = value
            self.v3v.set_text("{0:.1f}".format(self.value_3))

    def set_value_4(self, value):
        if self.value_4 != value:
            self.value_4 = value
            self.v4v.set_text("{0:.1f}".format(self.value_4))

    def set_value_5(self, value):
        if self.value_5 != value:
            self.value_5 = value
            self.v5v.set_text("{0:.0f}".format(self.value_5))

    def clear_all(self):
        self.value_1 = 0
        self.value_2 = 0
        self.value_3 = 0
        self.value_4 = 0
        self.value_5 = 0

        self.set_value_1(0)
        self.set_value_2(0)
        self.set_value_3(0)
        self.set_value_4(0)
        self.set_value_5(0)

        
if __name__ == '__main__':

    from epd import EPD

    # Display Layout instance
    L1 = Escale()
    
    # E-Paper Display instance
    epd = EPD(False, L1)

    val = 123
    for i in range(10):
        val   += .22
        val_25 = L1.round_to(val, 0.25)
        val_50 = L1.round_to(val, 0.5)
        val_1  = L1.round_to(val, 1.0)

        L1.set_value_1(val_25)
        L1.set_value_2(val_25)
        L1.set_value_3(val_50)
        L1.set_value_4(val_50)
        L1.set_value_5(val_1)
        epd.update()

    epd.refresh()
    L1.clear_all()
    epd.update()

    val += 456
    for i in range(11):
        val   += .39
        val_25 = L1.round_to(val, 0.25)
        val_50 = L1.round_to(val, 0.5)
        val_1  = L1.round_to(val, 1.0)
        
        L1.set_value_1(val_25)
        L1.set_value_2(val_25)
        L1.set_value_3(val_50)
        L1.set_value_4(val_50)
        L1.set_value_5(val_1)
        
        epd.update()

    raw_input()
