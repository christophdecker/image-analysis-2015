import numpy
a = numpy.asarray([[2,5,4,3,1],[1,2,1,5,7]])
print a.shape
print a
print numpy.where(a == 2)
print numpy.where(a == 4)
print a[numpy.where(a == 1)]
