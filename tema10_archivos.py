from io import open

texto = "Una linea con texto\nOtra linea con texto"
archivo = open('archivo.txt', 'w')
archivo.write(texto)
archivo.close()