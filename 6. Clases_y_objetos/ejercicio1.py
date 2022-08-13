class Vehiculo:
    color = None
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 1200

c = Coche()

c.color = "Verde"

print("Color:", c.color)
print("Ruedas:", c.ruedas)
print("Puertas:", c.puertas)
print("Velocidad:", c.velocidad)
print("Cilindrada:", c.cilindrada)
