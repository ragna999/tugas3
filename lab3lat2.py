print("Tampilkan n bilangan acak yang lebih kecil dari 0.5")

jumlah = int(input("Masukan jumlah n: "))
import random
for i in range (jumlah):
    print("Data ke",i+1 ,"-",(random.uniform(0.1,0.5)))