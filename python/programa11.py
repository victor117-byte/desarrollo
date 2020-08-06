# Programa 11
# Programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
# Creador Victor Hernandez Berrios
# Iniciado el 04/08/20

# Inicio
# se solicita al usuario la inversion, taza anual y periodo en anios
inversion = float (input('ingrersa el mondo de la inversion'))
interes = float (input('ingresa interes anual'))
anio = int (input('ingresa el periodo'))
# Se imprime el capital esperado
print("capital final: " + str(round(inversion * (interes / 100 + 1) ** anio, 2)))
# Fin del programa