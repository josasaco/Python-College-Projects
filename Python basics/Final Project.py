import numpy as np; import random as r; from math import sqrt
tablero = np.zeros((10,10),int)
z=np.zeros((10,10),int)
pos1=[]
pos2=[]
pos3=[]
b=0
dxy=[]
S1=1
S2=1
S3=1
print("Realizado por: Santiago Sacón")

n1 = r.randint(0, 9)
m1 = r.randint(0, 9)
n2 = r.randint(0, 9)
m2 = r.randint(0, 9)
n3 = r.randint(0, 9)
m3 = r.randint(0, 9)
tablero[n1, m1] = 1
tablero[n2, m2] = 2
tablero[n3, m3] = 3
print(tablero)


while b<10:

    x = int(input("Ingrese la fila en la que ingresará el dato:"))
    y = int(input("Ingrese la columna en la que ingresará el dato:"))
    v=1
    while v==1:
        if(x<1 or x>10):
            x = int(input("Ingrese correctamente la fila en la que ingresará el dato:"))
        elif(y<1 or y>10):
            y = int(input("Ingrese correctamente la columna en la que ingresará el dato:"))
        elif(n1==(x-1) and m1==(y-1)) or (n2==(x-1) and m2==(y-1)) or (n3==(x-1) and m3==(y-1)):
            print("Posición llena, ingrese nuevamente las posiciones:")
            x = int(input("x:"))
            y = int(input("y:"))
        else:
            v=2
    tablero[x-1,y-1] = 5
    dxy1 = sqrt((((x-1) - n1) ** 2) + (((y-1) - m1) ** 2))
    dxy2 = sqrt((((x-1) - n2) ** 2) + (((y-1) - m2) ** 2))
    dxy3 = sqrt((((x-1) - n3) ** 2) + (((y-1) - m3) ** 2))
    dxy = [dxy1, dxy2, dxy3]
    dxy.sort()
    if(dxy1==min(dxy)):
        z[x-1,y-1]=1
    elif(dxy2==min(dxy)):
        z[x-1,y-1]=2
    elif(dxy3==min(dxy)):
        z[x-1,y-1]=3

    b+=1
z[n1,m1]=1
z[n2,m2]=2
z[n3,m3]=3

print("El tablero con los datos llenos es:\n",tablero)
print()
print("El tablero con los elementos más cercanos es\n:",z)
