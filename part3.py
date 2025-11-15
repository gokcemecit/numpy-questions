#questions 20-30

import numpy as np

np.random.seed(42)

matrix=np.random.randint(0,20,size=(5,5))
column_mean=np.mean(matrix,axis=0)

centered_matrix=matrix-column_mean
print("centered matrix:")
print(centered_matrix)

new_mean=np.mean(centered_matrix,axis=0)
print("new column means:")
print(new_mean)

print("-"*20)

C=np.array([[4,7],[2,6]])
c_det=np.linalg.det(C)
print(f"determinant: {c_det}")
c_inverse=np.linalg.inv(C)
print("inverse:")
print(c_inverse)

expected_identity=np.eye(2)
matrix_dotproduct=C@c_inverse

control=np.allclose(expected_identity,matrix_dotproduct)
if(control):
    print("identity matrix is achieved")
else:
    print("identity matrix couldnt be achieve")

print("-"*20)

data=np.array([1,2,1,4,5,2,7,1])
unique_data,repetition=np.unique(data,return_counts=True)

print(f"unique elements: {unique_data}")

for var,rep in zip(unique_data,repetition):
    print(f"element {var} repeats {rep} times")

print("-"*20)


matrix2=np.random.randn(100)
clipped_matrix2=np.clip(matrix2,-2,2)
print("clipped matrix:")
print(clipped_matrix2)

print("-"*20)

v1=np.array([1,2,3])
v2=np.array([4,5,6])
inner_product=np.dot(v1,v2)
outer_product=np.outer(v1,v2)
print(f"inner product:{inner_product}")
print("outer product:")
print(outer_product)

print("-"*20)

py_list=list(range(1000000))
np_array=np.array(py_list)

print("-"*20)





