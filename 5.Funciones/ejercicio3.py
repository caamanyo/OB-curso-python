año = int(input("Escoge un año:"))

def es_bisiesto(año):
    if año % 4 == 0:
        return True
    else:
        return False

resultado = f"{año} es bisiesto." if es_bisiesto(año) else f"{año} no es bisiesto."

print(resultado)