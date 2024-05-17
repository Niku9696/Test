import numpy as np

a = np.array([1,2,6,9])
b = np.array([3,8,0,3])


d = 6
c = 6 * np.dot(a,b)

print("The dot product between the two vectors of a and b is {}".format(c))
