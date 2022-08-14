import pickle


class Vehiculo:
    ruedas = 0
    tipo_motor = ''
    is_encendido = False

    def __init__(self, ruedas, tipo_motor):
        self.ruedas = ruedas
        self.tipo_motor = tipo_motor

    def toggle_encendido(self):
        self.is_encendido = False if self.is_encendido == True else True


v = Vehiculo(4, 'diesel')

# Encender vehiculo antes de guardarlo
v.toggle_encendido()

path = '8.Entrada_salida/ejercicio2/vState.bin'

file = open(path, 'wb')
pickle.dump(v, file)
file.close()

# Apagar vehiculo
v.toggle_encendido()
print("¿Coche no guardado está encendido?", v.is_encendido)

file = open(path, 'rb')
saved_v = pickle.load(file)
print("¿Coche guardado está encendido?", saved_v.is_encendido)