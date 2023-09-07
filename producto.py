productos = {}
i = 0
ingresar = input("desea ingresar algun producto: ")

while ingresar == "si":
    i+=1
    producto = {
        "nombre": input("ingrese nombre del producto: "),
        "tipo": input("ingrese el tipo de producto: "),
        "precio": input("ingrese el precio del producto: ")
    }
    productos["producto"+str(i)] = producto
    ingresar = input("quiere ingresar otro producto? s/n")

print("lista de productos: ")
for key, value in productos.items():
    print(f"{key},{value}")

print("opciones: ")
opciones = input(" 1-eliminar \n 2-agregar") 

if opciones == "1":
    productos.clear()
elif opciones == "2":
    i = i + 1
    productoAgregado = {
        "nombre": input("ingrese nombre del producto: "),
        "tipo": input("ingrese el tipo de producto: "),
        "precio": input("ingrese el precio del producto: ")
    }
    productos["producto"+str(i)] = productoAgregado

#pendientes actualizar y consultar(realizar en casa)
if productos == "":
    print("lista de productos: vacia") 
else:    
    print("lista de productos: ")
    for key, value in productos.items():
     print(f"{key},{value}")       

    
          


