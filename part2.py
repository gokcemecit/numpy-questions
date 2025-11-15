#questions 11-19

import numpy as np

print("-"*20)

np.random.seed(42)

arr=np.random.randint(0,10,size=(2,3))
transposed_arr=arr.T

print(arr)
print(transposed_arr)

print("-"*20)

dizi=np.array([1,2,np.nan,4,5,np.nan,7])
nan_list=np.isnan(dizi)
nan_count=np.sum(nan_list)
print(nan_count)

print("-"*20)

matrix=np.random.randint(0,20,size=(5,5))
matrix_mean=np.mean(matrix)
matrix_max=np.max(matrix)
matrix_std=np.std(matrix,axis=0)
print(f"max: {matrix_max}, mean:{matrix_mean}, std per column:{matrix_std}")

print("-"*20)

a=np.array([1,2])
b=np.array([3,4])

vertical=np.vstack((a,b))
horizontal=np.hstack((a,b))

print(vertical)
print(horizontal)

print("-"*20)

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

dot_product=np.dot(A,B)
print(dot_product)

print("-"*20)



