print ("Program mencari bilangan terbesar dari 3 bilangan")

a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan kedua: "))
c = int(input("Masukan bilangan ketiga: "))

if a > b > c:
    print("Bilangan pertama adalah bilangan terbesar = %s" % a)
elif b > c:
    print("Bilangan kedua adalah bilangan terbesar = %s" % b)
else:
    print("Bilangan ketiga adalah bilangan terbesar = %s" % c)