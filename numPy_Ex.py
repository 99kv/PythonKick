import numpy as np

# An ndarray is a (usually fixed-size) multidimensional container of items of the same type and size.
# The number of dimensions and items in an array is defined by its shape, which is a tuple of N positive
# integers that specify the sizes of each dimension.

a = np.zeros(3)
print(a)
print(type(a))  #ndarray
print(type(a[0])) # default is float64
print(a.shape)
a.shape = (1,3)
print(a.shape)
print(a)
print("------")

print("--empty--")
z = np.empty(3)
print("empty ")
print(z)
print("------")

print("--linspace--") # evenly divided values from 1 to 100 with 6 elements
x = np.linspace(1,100,6)
print(x)
print("------")

# ndmin = what are the minimum dimensions - creates nested arrays
a = np.array([1,2,3,4],ndmin=1)
print(a)
# OUTPUT
# [1 2 3 4]
print("------")


# define multi dimensional array
a = np.array([[1, 2], [3, 4]])
print(a)
# OUTPUT
# [[1 2]
#  [3 4]]


#desired type of data array
a = np.array([[1, 2], [3, 4], [4,5]], dtype=complex)
print(a)
# OUTPUT
# [ [1.+0.j 2.+0.j]
#   [3.+0.j 4.+0.j]]

print(a.shape)
print("------")