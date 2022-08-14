path = '8.Entrada_salida/ejercicio1/hola.txt'

file = open(path, 'w')
buffer = 'Esto es un archivo de texto.\n'
file.write(buffer)
buffer = 'Esta es la siguiente linea del archivo.\n'
file.write(buffer)
buffer = 'Última línea.\n'
file.write(buffer)

file.close()

file = open(path, 'r')

for line in file.readlines():
    print(line)

file.close()