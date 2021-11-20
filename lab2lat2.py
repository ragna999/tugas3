print ('program untuk mengurutkan bilangan dari yang terbesar ke terkecil')

def sorting (data):
    ganti = True
    while len (data)-1 > 0 and ganti:
        ganti = False
        for i in range (len(data)-1):
            if data [i] > data [i+1]:
                ganti = True
                swap = data[i]
                data[i] = data[i+1]
                data [i+1] = swap
data = []
for i in range(3):
    inputbilangan = int(input("Masukan bilangan: "))
    data.append(inputbilangan)

sorting (data)
print (data) 