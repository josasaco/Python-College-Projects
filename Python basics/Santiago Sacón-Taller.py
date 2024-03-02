import random as r
items,s1,s2=[],[],[]
ns,ss,pp=[],[],[]
salir=7
while(salir!=0):
    print("\n*** MENU *** \n"
          "1. Ingreso de items\n2. Ingreso de preferencia por semestre \n"
          "3. Impresión de los items con mayor y menor preferencia en Stock\n4. Salir\n")
    opc=int(input("Ingrese una opción: "))
    if opc==1:
        str1=input("Ingrese items: ")
        items=list(str1.split("!"))
    elif opc==2:
        while(len(s1)!=len(items)):
            print(" *--- SUB-MENU ---*\n"
                "1.Ingreso Preferencia Semestre I\n"
                "2.Ingreso Preferencia Semestre II\n")
            opc2=eval(input("Ingrese opción: "))
            if(opc2==1):
                pref1=input("Ingrese PSI: ")
                s1=list(pref1.split("!"))
                for z in range(len(s1)):
                    s1[z]=eval(s1[z])
            else:
                pref2=input("Ingrese PSII: ")
                s2=list(pref2.split("!"))
                for z in range(len(s2)):
                    s2[z] = eval(s2[z])
    elif opc==3:
        #parte A
        new=len(items)//2
        for i in range(new):
            a=r.choice(items)
            ns.append(a)
        print(ns)
        #parteB
        ss=items[:]
        for i in range(new):
            ss.remove((ns[i]))
        print(ss)
        #parte C
        for i in range(new):
            b=ss[i]/s1[i]
            pp.append(b)
        for i in range(new):
            c=ss[i]/s2[i]
            pp.append(c)
    elif opc==4:
         salir=0
         #No he podido completar el trabajo :(