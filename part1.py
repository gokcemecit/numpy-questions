
#questions 1-10

import numpy as np
print("-"*20)

arr= np.arange(0,10,1)
print(arr)

print("-"*20)

arr2=np.zeros((3,4))
print(arr2)

print("-"*20)

arr3=np.ones((2,3))
print(arr3)

print("-"*20)

dizi=np.arange(12).reshape(3,4)
print(dizi.shape)
print(dizi.size)

print("-"*20)

arr4=[10,20,30,40]
dizi2=np.array(arr4,dtype=np.int64)
print(dizi2)

print("-"*20)

arr5=np.arange(20)
arr5=arr5[(arr5>5)&(arr5<15)]
print(arr5)

print("-"*20)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)

print("-"*20)

m=np.arange(1,26).reshape(5,5)
print(m[1,:])
print(m[:,2])

print("-"*20)
