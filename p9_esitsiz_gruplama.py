import numpy as np

veri=np.random.randn(1000)

bolme_indeksleri=[50,150,300,500]
gruplar=np.split(veri,bolme_indeksleri)


persentiller=[]
for i,grup in enumerate(gruplar):
    persentil_90=np.percentile(grup,90)
    persentiller.append(persentil_90)
    print(f"grup {i+1} %90lık persentili : {persentil_90:.4f}")

sonuc_vektoru=np.array(persentiller)
print(f"sonuç vektörü : \n{sonuc_vektoru}")