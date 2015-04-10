import numpy, vigra
import matplotlib; matplotlib.use('Qt4Agg')
from matplotlib import pyplot as plot

img = vigra.impex.readImage("myImage.png")[...,0] # read in red channel
plot.figure()
plot.gray() #select grayscale color map
plot.imshow(img)
plot.show()

