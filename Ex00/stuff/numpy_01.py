import numpy
#create a 2D array of shape (4,6), data type is unsigned char
a = numpy.zeros((4,6), dtype=numpy.uint8)
print a.ndim  #2-dimensional
print a.shape, a.shape[0], a.shape[1] 
print a.dtype #numpy.uint8

#uniform random numbers in [0,1)
b = numpy.random.random(a.shape)

#basic algebra for arrays
c = a+b
d = a*b
e = a/(b+1) 
f = numpy.sqrt(b)

