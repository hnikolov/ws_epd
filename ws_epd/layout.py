class Layout(object):
    def __init__(self):
        self.components  = []
                
        self.width   = 128 # epd2in13.EPD_WIDTH
        self.height  = 250 # epd2in13.EPD_HEIGHT


    def add(self, component):
        if isinstance(component, (list,)):
            self.components.extend( component )
        else:
            self.components.append( component )


    def round_to(self, value, res):
        """
        Round to e.g., 0.5, 0.02, 10, etc.
        """
        if res == 0:
            return round(value)
        return res * (round(value/res))
