deportes = []
i = 0 
ingresar = input("desea ingresar algun deporte? s/n")
while ingresar == "s":
    print("1-agregar \n 2-eliminar \n 3-mostrar \n 4-actualizar")
    opciones = input("ingrese la opcion deseada")
    if opciones == "1":
        agregar = input("ingrese el deporte a ingresar: ")
        deportes.append(agregar)
    elif opciones == "2":
        agregar = input("ingrese el deporte a eliminar: ")
        deportes.remove(agregar)
    elif opciones == "3":
        agregar = input("ingrese el deporte a mostrar: ")
        deportes.append(agregar)
    elif opciones == "4":
        agregar = input("ingrese el deporte a actualizar: ")
        deportes.append(agregar)   
    ingresar = input("desea seguir operndo? s/n")        

for key in deportes:
    i+=1
    print(i,key)


    
