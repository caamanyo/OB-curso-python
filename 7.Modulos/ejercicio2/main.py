import time as t

def main():
    class Alarma:
        fecha = t.strftime("%d-%m-%Y")
        hora = t.strftime("%H:%M:%S")
        hours_to_freedom = 19 - int(hora[0:2]) - 1 if int(hora[3:5]) != 0 else 19 - int(hora[0:2])
        min_to_freedom = 60 - int(hora[3:5]) - 1 if int(hora[3:5]) != 0 else "0"
        sec_to_freedom = 60 - int(hora[-2:]) if int(hora[-2:]) != 0 else "0"
    
        def __init__(self):
            print(f'Fecha: {self.fecha}')
            print(f'Hora: {self.hora}')
            print(self.hours_to_freedom)
            print(self.min_to_freedom)
            print(self.sec_to_freedom)
            print(self.fin_jornada())
        
        def fin_jornada(self):
            return "Hora de volver a casa!" if int(t.strftime('%H')) >= 19 else f"Sigue trabajando. Quedan {self.hours_to_freedom} horas, {self.min_to_freedom} minutos y {self.sec_to_freedom} segundos."

    al = Alarma()
    
    


if __name__ == "__main__":
    main()