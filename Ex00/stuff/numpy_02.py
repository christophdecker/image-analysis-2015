a[:] = 1 #write a 1 to every entry
a[1,2] = 2 #assign 2 to the row 1, col 2 (indices start at 0!)

s = numpy.sum(a) #sum over all array elements
assert s == 7

a[:,0] = 42 #assign 42 to the 0-th column
            # ':' ==> select all rows
            # '0' ==> select the 0-th column

a[0,...] = 42 # fill 0-th element of first array dimension (here: column)
              # with 42's, no matter how many dimensions a has

b = a[:,0:2] #make a subarray: select only columns 0 and 1
             # ( range [0..2) )
