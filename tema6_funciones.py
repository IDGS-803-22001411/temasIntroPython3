import os
def funcion1():
    os.system('cls')
    print("dame 2 numeros")
    numero1= int(input("numero 1: "))
    numero2= int(input("numero 2: "))
    os.system('cls')
    print("la resta de 2 numeros es: ", numero1 - numero2)
    run()

def funcion2():
    print("dame 2 numeros")
    numero1= int(input("numero 1: "))
    numero2= int(input("numero 2: "))
    os.system('cls')
    print("la suma de 2 numeros es: ", numero1 + numero2)
    run()

def funcion3():
    print("dame 2 numeros")
    numero1= int(input("numero 1: "))
    numero2= int(input("numero 2: "))
    os.system('cls')
    print("la multiplicacion de 2 numeros es: ", numero1 * numero2)
    run()
    

def funcion4():
    print("dame 2 numeros")
    numero1= int(input("numero 1: "))
    numero2= int(input("numero 2: "))
    os.system('cls')
    print("la division de 2 numeros es: ", numero1/numero2)
    run()

def salir():
    os.system('cls')
    print("Salir")
        

def run():
    print("1-suma")
    print("2-resta")
    print("3-multiplicacion")
    print("4-division")
    print("5-salir")
    opcion=int(input("dame una opcion "))
    if opcion==1:
        funcion2()
    if opcion==2:
        funcion1()
    if opcion==3:
        funcion3()
    if opcion==4:
        funcion4()
    if opcion==5:
        salir()
if __name__=="main_":
    run()