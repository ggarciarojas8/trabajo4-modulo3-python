"""
1. Crea un archivo llamado `calculadora_interactiva.py`.
2. 
"""
from operaciones_matematicas import *

def calculadora_interactiva():
    print("")
    print("Bienvenidos a la Calculadora Interactiva")
    while True:
        print("Operaciones matemáticas disponibles")
        print("Operación 1. SUMAR")
        print("Operación 2. RESTAR")
        print("Operación 3. MULTIPLICAR")
        print("Operación 4. DIVISIÓN")
        print("Operación 5. SALIR")

        opcion= input("Seleccione la Operación Matemática que desea Realizar:")
            
        if opcion=="5":
            print("Gracias por Utilizar la Calculadora Interactiva")
            print("Hasta pronto")
            break
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción No Válida. Por favor seleccione una opción válida")
            continue

        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion=="1": 
            print("El Resultado de la Suma es: ", sumatoria(numero1,numero2))
        elif opcion=="2":
            print("El Resultado de la Resta es: ", restar(numero1,numero2))
        elif opcion=="3":
            print("El Resultado de la mutiplicación es: ", multiplicar(numero1,numero2))
        elif opcion=="4":
            print("El Resultado de la división es: ", dividir(numero1,numero2))