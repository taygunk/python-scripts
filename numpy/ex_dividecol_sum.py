import numpy
#!/usr/bin/python

#----------- Divide each column by col sum ---------------#

e = numpy.array([[1., 2.], [3., 4.], [6.,8. ]])
print(e)
#array([[ 1.,  2.],
#       [ 3.,  4.],
#       [ 6.,  8.]])

result = e / numpy.sum(e, axis=0)
print(result)
#array([[ 0.1       ,  0.14285714],
#       [ 0.3       ,  0.28571429],
#       [ 0.6       ,  0.57142857]])


#----------- Divide each column by row sum ---------------#
print(e)
result = (e.T / numpy.sum(e, axis=1)).T
print(result)