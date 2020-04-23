import matplotlib.pyplot as plt
import numpy
import tkinter
from tkinter import*
# Specim IQ

#contrast check for card photogrammetry
spatial_pixels = 512
sample_lines = 512
spectral_bands = 204
open_path = r'C:\Users\Nihal\Desktop\Pycharm\secondproject\image set\409\capture\409.raw'
fopen = open(open_path, "rb")
u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
print(u.shape)
print(spatial_pixels*sample_lines*spectral_bands)
u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
print(u1.shape)

#plt.imshow(u1[:,160,:], cmap="gray")

u1 = u1/100
white = u1[300,:,400]
dark = u1[100,:,100]
contrast = white/dark
plt.plot(white,'r')
plt.plot(dark,'r')
plt.plot(contrast,'b')
plt.show()


plt.show()