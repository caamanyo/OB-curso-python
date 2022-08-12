numero_inicial = int(input("Escoge un número inicial:"))
numero_final = int(input("Escoge un número final:"))
lista_impares = []

for num in range(numero_inicial, numero_final + 1):
    if num % 2 != 0:
        lista_impares.append(num)

print(f"Listado de números impares entre {numero_inicial} y {numero_final}:")
print(lista_impares)