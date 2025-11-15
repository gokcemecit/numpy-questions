import numpy as np

matrix=np.random.randn(20,5)

rastgele_satirlar=np.random.choice(20,size=10,replace=True)
rastgele_sutunlar=np.random.choice(5,size=10,replace=True)

for i in range(10):
    matrix[rastgele_satirlar[i],rastgele_sutunlar[i]]=np.nan


print(f"matrixin ilk 5 satırı: \n {matrix[:5]}")

sutun_medyanlari=np.nanmedian(matrix,axis=0)
print("sutun medyanlar:")
print(sutun_medyanlari)

sutun_medyanlari=sutun_medyanlari.reshape(1,5)

doldurulmus_matrix=np.where(np.isnan(matrix),sutun_medyanlari,matrix)

print(f"doldurulmus matrixin ilk 5 satırı: \n{doldurulmus_matrix[:5]}")



