import numpy as np

sinav_puanlari=np.random.randint(0,100,size=(100,3))

siralama_indeksleri=np.lexsort((sinav_puanlari[:,0],-sinav_puanlari[:,2]))

siralanmis_puanlar=sinav_puanlari[siralama_indeksleri]

ilk_10=siralanmis_puanlar[:10]
print(f"ilk 10 öğrencinin puanları: {ilk_10}")

