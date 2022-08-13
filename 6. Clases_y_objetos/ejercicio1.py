class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 1200

c = Coche()
print(c.puertas)