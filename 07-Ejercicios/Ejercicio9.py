"""
Ejercicio 9 
Hacer un programa que pida numeros al usuario indefenidamente hasta meter el numero 111

"""
contador = 1
while contador <=100:
    numero = int(input("Ingrese un numero: "))
    if(numero == 111):
        break 
    else:
        print(f"El numero es {numero}")