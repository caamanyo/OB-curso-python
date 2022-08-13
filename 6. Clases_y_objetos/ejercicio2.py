class Alumno:
    _nombre = ""
    _nota = 0
    _aprobado = ""

    def __init__(self):
        self.set_nombre()
        self.set_nota()
        self._aprobado = "ha aprobado" if self.is_aprobado() else "no ha aprobado"
        print(f"{self._nombre} {self._aprobado} el curso. La nota final es un {self._nota}.")

    def set_nombre(self):
        self._nombre = input("Nombre del alumno:")

    def set_nota(self):
        self._nota = float(input("Introduce la nota del alumno:"))

    def is_aprobado(self):
        return True if self._nota >= 5 else False

a = Alumno()