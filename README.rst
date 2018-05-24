ws_epd
==========

Convenience utility for WaveShare E-Paper Displays.
Currently supports 2.13inch_e-Paper_HAT.
There is a mock-mode which uses Tk to show PIL Image objects.
The advantage of this over using Image.show() is that it will reuse the
same window, so you can show multiple images without opening a new
window for each image (good to simulate display updates). 
This mode is to be used to quickly develop and test display layouts on desktop/laptop.
There is no need to download to RaspberryPi and using real 2.13inch_e-Paper_HAT.

Try in the src folder:

python layout_1.py

Note: Very preliminary version, the mock-up is not completely precise w.r.t. to the real epd. Work in progress.
