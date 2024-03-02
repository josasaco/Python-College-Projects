import random as r
num=eval(input("Ingrese el número de caracteres de la letra: ")) ; randomW="" ; letterS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pI=0 ; pF=len(letterS)-1


aux=1
while(aux<=num) :
    randomNum=r.randint(pI,pF)
    randomW+=letterS[randomNum]
    aux+=1

spacesNum=num-2
spacesOut=" _"
aux=1
while(aux<=spacesNum) :
    spacesOut=" _"
    aux+=1

print("Palabra: %s" % randomW[0] + (num-2)*spacesOut + "%s" % randomW[num-1])
guess=input("Ingrese una palabra con %d letras y que empiece con %s y finalice con %s: " % (num,randomW[0],randomW[num-1]))
if(guess[:]==randomW[:]):
    print("Salvado")
else:
    print("Ahorcado")
    
