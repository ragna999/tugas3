print("INVESTASI")

x = int(input("Modal awal: "))

a = 0*x
b = 0*x
c = 0.01*x
d = 0*x
e = 0.05*x
f = 0.05*x
g = 0.05*x
h = 0.03*x
y=[a,b,c,d,e,f,g,h]

for i in range(len(y)):
    print("Laba bulan ke",i+1 ,"Sebesar: ",y[i])

z=(a+b+c+d+e+f+g+h)
print("Jumblah laba selama 8 bulan: ",z)