import os

class Traductor:
    def __init__(self, archivo="diccionario.txt"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                pass

    def capturar_palabras(self, palabra_esp, palabra_ing):
        with open(self.archivo, 'a') as f:
            f.write(f"{palabra_esp.lower()}:{palabra_ing.lower()}\n")
        print(f"Palabras '{palabra_esp}' y '{palabra_ing}' almacenadas correctamente.")

    def buscar_palabra(self, palabra, idioma):
        with open(self.archivo, 'r') as f:
            for linea in f:
                esp, ing = linea.strip().split(":")
                if idioma == "espanol" and palabra.lower() == esp:
                    return ing.capitalize()
                elif idioma == "ingles" and palabra.lower() == ing:
                    return esp.capitalize()
        return None


def menu():
    traductor = Traductor()

    while True:
        print("\nBienvenido al traductor")
        print("1. Capturar palabras")
        print("2. Buscar palabras")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            palabra_esp = input("Palabra en español: ")
            palabra_ing = input("Palabra en inglés: ")
            traductor.capturar_palabras(palabra_esp, palabra_ing)

        elif opcion == "2":
            print("\nBuscar:")
            print("1. Español")
            print("2. Inglés")
            sub_opcion = input("Opción: ")

            if sub_opcion == "1":
                palabra = input("Palabra en español: ")
                resultado = traductor.buscar_palabra(palabra, "espanol")
                if resultado:
                    print(f"Palabra encontrada: {resultado}")
                else:
                    print("Palabra no encontrada.")

            elif sub_opcion == "2":
                palabra = input("Palabra en inglés: ")
                resultado = traductor.buscar_palabra(palabra, "ingles")
                if resultado:
                    print(f"Palabra encontrada: {resultado}")
                else:
                    print("Palabra no encontrada.")
            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
