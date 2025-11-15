import numpy as np

print("----------senaryo 1----------")
print("-------------------------------")

np.random.seed(42)

karar_tensoru=np.random.randn(5,20,8)
zaman_ortalamalari=np.mean(karar_tensoru,axis=(0,2))
print()
print(f"zaman ortalamaları:\n {zaman_ortalamalari}")

genel_ortalama=np.mean(karar_tensoru)
final_tensoru=karar_tensoru-genel_ortalama
print(f"normalize edilmiş tensör: \n{final_tensoru}")

print("----------senaryo 2----------")
print("-----------------------------")

A=np.random.randn(50,4)
B=np.random.randn(1,4)
kare=(A-B)**2
toplam=np.sum(kare,axis=1)
mesafe=np.sqrt(toplam)
print(f"ilk 5 uzaklık:{mesafe[:5]}")

en_yakin_index=np.argmin(mesafe)
en_yakin_mesafe=np.min(mesafe)
print(f"en yakın mesafe : {en_yakin_mesafe} ve indexi : {en_yakin_index}")




