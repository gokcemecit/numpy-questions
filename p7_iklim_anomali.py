import numpy as np

np.random.seed(42)
tensor=np.random.randint(0,40,size=(10,30,2))

parametre_ortalamalari=np.mean(tensor,axis=(0,1))
print(f"ortalama nem:{parametre_ortalamalari[1]:.2f} ")
print(f"ortalama sıcaklık: {parametre_ortalamalari[0]:.2f} ˚C")

parametre_ortalamalari_reshaped=parametre_ortalamalari.reshape(1,1,2)

anomali_tensoru=tensor-parametre_ortalamalari_reshaped

anomali_ortalama=np.mean(anomali_tensoru,axis=(0,1))
print(f"anomali tensörünün ortalaması: {anomali_ortalama}")

print(f"en yüksek sıcaklık anomolisi: {np.max(anomali_tensoru[:,:,0]):.2f}˚C")
print(f"en düşük sıcaklık anomolisi: {np.min(anomali_tensoru[:,:,0]):.2f}˚C")

