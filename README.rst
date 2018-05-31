ws_epd
==========

Convenience utility for WaveShare E-Paper Displays.
Supports 2.13inch_e-Paper_HAT.
There is an emulation mode (``self.epd = EPD(False)``) which uses Tk to show PIL Image objects.
The advantage of using Tk over using Image.show() is that it will reuse the
same window, so you can show multiple images without opening a new
window for each image (good to simulate display updates). 
The emulation mode is to be used to quickly develop and test display layouts on desktop/laptop.
There is no need to download to RaspberryPi and use real 2.13inch_e-Paper_HAT to check the display layout.

Try in the ws_epd folder: ::

    $ cd ws_epd/ws_epd
    $ python layout_1.py

To run in emulation mode, make sure that the E-Paper Display instance is given False as an argument:

``self.epd = EPD( False )``

When using a real 2.13inch_e-Paper_HAT connected to a RaspberryPi, make sure you change the instance to:

``self.epd = EPD( True )``

Install ``ws_epd`` from source
------------------------------

To use this utility in other projects, install it by ::

	$ cd ws_epd
	$ sudo python setup.py develop

Option *develop* installs ``ws_epd`` in *editable* mode. 
This is very convenient because your changes are immediately reflected into the installed package.
This means that you do not need to re-install ``ws_epd`` in order your changes to take effect.

Un-install
----------

Un-installing ``ws_epd`` is easy: ::

	$ cd ws_epd
	$ sudo python setup.py develop --uninstall


Dependences on Python packages
------------------------------

``ws_epd`` uses **Tk, Pillow** for emulation and **Pillow, spidev** when using a real display on a RaspberryPi.
Currently, **Pillow** will be installed during the installation of ``ws_epd`` if not present on your system. 

**Note:** Packages will **not** be un-installed if you un-install ``ws_epd``. 
