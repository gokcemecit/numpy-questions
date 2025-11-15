import numpy as np

A=np.random.rand(5,10)
B=np.random.rand(5,10)
C=np.random.rand(10,10)

tensor_ab_matrixi=np.stack((A,B),axis=0)
print(f"a ve b nin yeni eksende birleşimi: \n{tensor_ab_matrixi}")

sonuc_matrix=np.matmul(tensor_ab_matrixi,C)
print(f"sonuç matrixi:\n {sonuc_matrix}")