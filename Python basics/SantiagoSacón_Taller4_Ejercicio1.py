p=[]
n=[]
c=[]
t=input("Ingrese las frases de acuerdo al formato:")
p[:]=t.split()
for i in range(len(p)):
    if (p[i]=="MAT"):
        n.append(p[i+1])
        c.append(p[i+2])
print("El número de maestros en el departamento de matemática es: %d"%(len(n)))
for i in range(len(n)):
    print("Nombre:%s "%(n[i]),"Código:%s "%(c[i]))