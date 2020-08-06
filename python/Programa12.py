# Programa 12
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
# Creador Victor Hernandez Berrios
# Iniciado el 04/08/20

# Inicio
# Se solicita un numero entero en la variable num
num = int(input('ingrese u numero entero '))
# validar si la variable num es par o inpar
if num % 2 == 0:
    print('El número', num, 'es par.')
else:
    print('El número ' + str(num) + ' es impar.')

# Fin del programa