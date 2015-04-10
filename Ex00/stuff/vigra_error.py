import numpy, vigra
a = numpy.random.random( (10,20) )

x = vigra.filters.gaussianSmoothing(a, 1)
