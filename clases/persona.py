import datetime

class Persona:

    def __init__(self,nombre,apellidos, fnac, id, puntuacion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fnac = fnac
        self.id = id
        self.puntuacion = puntuacion


    def returnNombre(self):
        return self.nombre
    def returnApellidos(self):
        return self.apellidos
    def returnId(self):
        return self.id
    def returnPuntuacion(self):
        return self.puntuacion
    def returnPuntuacion(self):
        return self.puntuacion

    def calcularEdad(self) -> int:
            hoy = datetime.date.today()
            years = hoy.year - self.fecha_nacimiento.year
            if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
                years -= 1
            return years

    def __str__(self):
        return f'{self.nombre} {self.apellidos} con puntuacion {self.puntuacion}'