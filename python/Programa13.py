# Programa 13
# Escribir un programa imprima un menu de la pizzeria Bella Napoli
# Creador Victor Hernandez Berrios
# Iniciado el 04/08/20

# Inicio
# Se imprime el menu y se captura el tipo de pizza que desea el cliente en la variable tipo
print("Binevenido a la pizzeria Bella Napolli.\nTipos de pizza\nT1-Vegetariana\nT2- No vegetariana\n")
tipo = input("Introduce el numero correspondiente al tipo de pizza que quieres ")
# Se valida el tipo de pizza vegetariana o no vegetariana en la variable tipo
if  tipo == "1":
    # Se imprime los diferentes ingredientes que desea el cliente y se valida con la variable ingrediente
    print("ingredientes de pizza vegetariana\n1- Pimiento\n2- Tofu\n")
    ingrediente = input("introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("Tofu")
else:
    # Se imprime los diferentes ingredientes que desea el cliente y se valida con la variable ingrediente
    print("ingredientes de pizza no vegetariana\n1- Peperoni\n2- Jamon\n3- Salmon\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozarrella, tomate y ", end="")
    if ingrediente =="1":
        print("peperoni")
    elif ingrediente =="2":
        print("Jamon")
    else:
        print("Salmon")
print("Gracias por tu compra!")
# Fin del programa