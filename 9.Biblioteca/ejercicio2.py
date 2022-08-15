import functools

listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

solo_impares = filter(lambda x: x % 2, listado)
suma_impares = functools.reduce(lambda x, y: x + y, solo_impares)
print(suma_impares)
