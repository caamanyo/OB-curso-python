from math import pi

calc_area_triangulo = lambda base, altura: (base * altura) / 2
calc_area_circulo = lambda radio: math.pi * radio ** 2

print(calc_area_triangulo(2, 4))
print(round(calc_area_circulo(1), 2))