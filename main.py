#https://github.com/spectralpython/spectral/blob/master/spectral/io/envi.py
import matplotlib.pyplot as plt
import numpy
import tkinter
from tkinter import*


# #open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker_8_binning\capture\Colorchecker.raw'
#
# '''
# spatial_pixels = 2144
# sample_lines = 1357
# spectral_bands = 135
# open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker_8_binning\capture\Colorchecker.raw'
#
# # Specim V10 no binning
# # Cannot read whole file due to its huge size. Need to skip n bytes fopen.seek(spatial_pixels*n*spectral_bands)
# open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker no binning\capture\halogen_emptyname_0008.raw'
# spatial_pixels = 2144
# sample_lines = 100 #1259
# spectral_bands = 1080
#
# # Specim V10 no binning
# spatial_pixels = 1100
# sample_lines = 500 #2252
# spectral_bands = 567
# open_path = r'C:\READ ENVI Matlab + Python\5_unwashed_washed_2019_09_02_17_06_03\data'
#
# # Specim IQ
# spatial_pixels = 512
# sample_lines = 512
# spectral_bands = 204
# open_path = r'C:\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'
#
# # N25 Infrared
# spatial_pixels = 320
# sample_lines = 449
# spectral_bands = 256
# open_path = r'C:\SPECTRAL IMAGES\Specim N25\Paintings Sarita\IR\capture\IR_best_orientation_inversed_0009.raw'
#
# '''
# # Specim IQ
# spatial_pixels = 512
# sample_lines = 512
# spectral_bands = 204
# open_path = r'F:\PHD\UEF Thesis\Dimitry\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'
#
# #
# fopen = open(open_path, "rb")
#
# u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
# print(u.shape)
# print(spatial_pixels*sample_lines*spectral_bands)
# u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
# print(u1.shape)
# plt.imshow(u1[150:350,160,150:350], cmap="gray")
# plt.show()
#
# # write to file
# filename = r"C:\SPECTRAL IMAGES\Temp\Colorchecker_8bin_float32.raw"
# fileobj = open(filename, mode='wb')
# c = numpy.ndarray(shape=(spatial_pixels*sample_lines*spectral_bands,1), dtype=float)
# c = u/255
# c.tofile(fileobj)
# fileobj.close()

#intialize gui
window = tkinter.Tk() #initialize

window.title("Spectral Bandwise Display") #title

labelTitle = tkinter.Label(window, text="Spectral Image", font=("Helvetica", 16)) #label
labelTitle.grid(row=1, column=1)

window.geometry("500x200") #window size


#View Raw Image-----------------------------------------------------

#labelFirst
labelRead = Label (window, text="View raw image ", font=("Arial", 10))
labelRead.grid(row=2, column=1)

#butto creation
#action for buttonFirst
def clicked():
    # Specim IQ
    spatial_pixels = 512
    sample_lines = 512
    spectral_bands = 204
    open_path = r'F:\PHD\UEF Thesis\Dimitry\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'
    fopen = open(open_path, "rb")
    u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
    print(u.shape)
    print(spatial_pixels*sample_lines*spectral_bands)
    u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
    print(u1.shape)
    plt.imshow(u1[:,160,:], cmap="gray")
    plt.show()

#buttonRead
buttonRead = Button (window, text="Enter", command=clicked)
buttonRead.grid(row=2, column=2)
#View Raw Image Done!-------------------------------------------------------

#Crop Image----------------------------------------------------------
#labelCrop
labelCrop = Label (window, text="Crop Image ", font=("Arial", 10))
labelCrop.grid(row=3, column=1)

#textbox
txtboxX1 = Entry(window,width=10)
txtboxX1.grid(row=3, column=2)

txtboxX2 = Entry(window,width=10)
txtboxX2.grid(row=3, column=3)

txtboxY1 = Entry(window,width=10)
txtboxY1.grid(row=3, column=4)

txtboxY2 = Entry(window,width=10)
txtboxY2.grid(row=3, column=5)

#button creation
#action for buttonCrop
def clickedCrop():

    #getting values from textbox
    stringX1 = txtboxX1.get()
    intX1 = int(stringX1)

    stringX2 = txtboxX2.get()
    intX2 = int(stringX2)

    stringY1 = txtboxY1.get()
    intY1 = int(stringY1)

    stringY2 = txtboxY2.get()
    intY2 = int(stringY2)
    #-------------------------------------

    # Specim IQ
    spatial_pixels = 512
    sample_lines = 512
    spectral_bands = 204
    open_path = r'F:\PHD\UEF Thesis\Dimitry\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'
    fopen = open(open_path, "rb")
    u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
    print(u.shape)
    print(spatial_pixels*sample_lines*spectral_bands)
    u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
    print(u1.shape)
    plt.imshow(u1[intX1:intX2,160,intY1:intY2], cmap="gray")
    plt.show()

#buttonCrop
buttonCrop = Button (window, text="crop", command=clickedCrop)
buttonCrop.grid(row=3, column=6)
#Crop Image Done----------------------------------------------------------


#View bandwise----------------------------------------------------------
#labelBand
labelBand = Label (window, text="View Bandwise ", font=("Arial", 10))
labelBand.grid(row=4, column=1)

#labelBandNumber
labelBandNumber = Label (window, text="Band Number ", font=("Arial", 10))
labelBandNumber.grid(row=4, column=2)
bandNumber = 0 #intitally 0 so people can see without typing anythin

#textbox
txtboxBand = Entry(window,width=10)
txtboxBand.grid(row=4, column=3)

#button creation
#action for buttonBand
def clickedBand():

    stringBand = txtboxBand.get()
    bandNumber = int(stringBand)

    # Specim IQ
    spatial_pixels = 512
    sample_lines = 512
    spectral_bands = 204
    open_path = r'F:\PHD\UEF Thesis\Dimitry\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'
    fopen = open(open_path, "rb")
    u = numpy.fromfile(fopen, dtype=numpy.uint16)  # uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
    print(u.shape)
    print(spatial_pixels * sample_lines * spectral_bands)
    u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
    print(u1.shape)
    plt.imshow(u1[:, bandNumber, :], cmap="gray")
    plt.show()

#buttonShow
buttonShow = Button (window, text="show", command=clickedBand)
buttonShow.grid(row=4, column=4)

def clickedNext():
    stringBand = txtboxBand.get()
    bandNumber = int(stringBand)
    print = bandNumber+10
    txtboxBand.delete(0, END)
    txtboxBand.insert(0, print)


#buttonBand --uses new function for band
buttonNext = Button (window, text="+10", command=clickedNext)
buttonNext.grid(row=4, column=5)


#View bandwise done----------------------------------------------------------


window.mainloop() #execute gui

