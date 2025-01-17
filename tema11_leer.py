texto = ""
with open('archivo.txt', 'r') as archivo:
    texto = archivo.read()

print(texto)
archivo.seek(0)