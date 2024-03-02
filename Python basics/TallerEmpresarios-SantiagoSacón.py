import numpy as np
ga=[]
turquia=["E1t","E2t","E3t","E4t","E5t"]
mexico=["E1m","E2m","E3m","E4m","E5m"]
chile=["E1c","E2c","E3c","E4c","E5c"]
e=np.random.randint(100,15001,(4,15))
print(e)
#1
mrt=e[3,0:5]/e[0,0:5]
imt=np.argmax(mrt)
mt=turquia[imt] #mayor rentabilidad Turquía
mrm=e[3,len(turquia):len(mexico)+len(turquia)]/e[0,len(turquia):len(turquia)+len(mexico)]
imm=np.argmax(mrm)
mm=turquia[imm] #mayor rentabilidad México
mrc=e[3,len(turquia)+len(mexico):]/e[0,len(turquia)+len(mexico):]
imc=np.argmax(mrc)
mc=turquia[imc] #mayor rentabilidad Chile
#2
nl=turquia+mexico+chile
print(nl)
mrt=e[3,:]/e[0,:]
emr=nl[mrt.argmax()]
if emr in turquia:
    r="El empresario con mayor rentabilidad es turco"
elif emr in mexico:
    r="El empresario con mayor rentabilidad es mexicano"
else:
    r="El empresario con mayor rentabilidad es chileno"
#3
etp=e[0,len(turquia):].max()
bt=e[0,0:len(turquia)]>etp
netp=bt.sum()
#4
inv=e[1,e[0,:]>800]
pi=inv.mean()
#5
c1=0
c2=0
c3=0
rr=e[3,0:5]/e[0,0:5]
for i in rr:
    if i >=0.8:
        c1+=1
    elif 0.4<=i<0.8:
        c2+=1
    else:
        c3+=1
#6
gat=(e[3,0:len(turquia)]).sum()
gam=(e[3,len(turquia):len(turquia)+len(mexico)]).sum()
gac=(e[3,len(turquia)+len(mexico):]).sum()
ga=[gat,gam,gac]
if max(ga)==gat:
    print("El país con mayor ganancia anual es Turquía con:%d $"%(gat))
elif max(ga)==gam:
    print("El país con mayor ganancia anual es México con:%d $"%(gam))
else:
    print("El país con mayor ganancia anual es Chile con:%d $"%(gac))
if min(ga)==gat:
    print("El país con menor ganancia anual es Turquía con:%d $"%(gat))
elif min(ga)==gam:
    print("El país con menor ganancia anual es México con:%d $"%(gam))
else:
    print("El país con menor ganancia anual es Chile con:%d $"%(gac))