path = '8.Entrada_salida/ejercicio1/hola.txt'
file = open(path, 'w')
buffer = "Esto es un archivo de texto."
data = file.write(buffer)
file.close()