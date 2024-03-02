n=[]
v=[]
c=[]
e=[]
ne=[]
mm=[]
men=[]
may=[]
l=[5,6,7,8,9,10]
t=input("Ingrese los nombres de las plantas:")
n[:]=t.split()
#la siguiente validación al encontrar un valor que no cumpla las condiciones simplemente no lo agrega la lista y seguirá pidiendo valores hasta llenarla

for i in range(len(n)):
    nv=1
    while(nv not in l):
        nv=int(input("Ingrese la puntuación de visitas: "))
    v.append(nv)
for i in range(len(n)):
    nv2=1
    while(nv2 not in l):
        nv2=int(input("Ingrese el costo de mantenimiento: "))
    c.append(nv2)
for i in range(len(n)):
    es=(0.7*(v[i]))+(0.3*(c[i]))
    e.append(es)
for i in e:
    npe=((1*i)/3)
    ne.append(npe)
imax=ne.index(max(ne))
imin=ne.index(min(ne))
print("Mayor:%s"%(n[imax]),"Puntos planta:%2f"%(ne[imax]))
print("Menor:%s"%(n[imin]),"Puntos planta:%2f"%(ne[imin]))

suma=0
for i in e:
    suma+=i

prom=suma/len(e)
print("El promedio de los puntos planta es: %2f"%(prom))

for i in range(len(e)):
    if(e[i]<prom):
        men.append(e[i])
    elif(e[i]>prom):
        may.append(e[i])
for i in range(len(e)):
    if(max(men)==e[i]):
        print("La planta con el valor estrella mas cercano al promedio (inferior) es: %s"%(n[i]),"Valor estrella: %2f"%(e[i]))
for i in range(len(e)):
    if(min(may)==e[i]):
        print("La planta con el valor estrella mas cercano al promedio (superior) es: %s"%(n[i]),"Valor estrella: %2f"%(e[i]))









