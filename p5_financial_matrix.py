import numpy as np

np.random.seed(42)

finansal_matrix=np.round(np.random.uniform(100,200,size=(120,6)),4)
print("fiyat matrisi:")
print(finansal_matrix[:5])      
#
farklar=np.diff(finansal_matrix,axis=0)
gunluk_getiri=farklar/finansal_matrix[:-1]

kovaryans_matrixi=np.cov(gunluk_getiri,rowvar=False)
print(f"kovaryans matrixi: \n{kovaryans_matrixi}")

eig_degerleri,eig_vektorleri=np.linalg.eig(kovaryans_matrixi)

min_index=np.argmin(eig_degerleri)
min_eig=eig_degerleri[min_index]
min_eig_vektoru=eig_vektorleri[:,min_index]

print(f"en küçük özdeğer: {min_eig}")
print(f"en küçük özdeğere denk gelen özvektör \n {min_eig_vektoru}")






