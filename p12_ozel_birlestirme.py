import numpy as np

A=np.random.randn(10,3)
B=np.random.randn(10,3)

yeni_matrix=np.column_stack((A[:,0],B[:,1],A[:,2]))

sutun1_medyan=np.median(yeni_matrix[:,0])
sutun2_std=np.std(yeni_matrix[:,1])
sutun3_toplam=np.sum(yeni_matrix[:,2])

sonuc_vektoru=np.array([sutun1_medyan,sutun2_std,sutun3_toplam])
print(f"sonuç vektörü: \n {sonuc_vektoru}")