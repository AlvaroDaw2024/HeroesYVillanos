from persona import Persona

class Villano(Persona):

    def __init__(self,nombre,apellidos, fnac, id, puntuacion,chagepeteador,entregadorTardio,ausencias,hablador):
        super().__init__(self,nombre,apellidos,fnac,id,puntuacion)
        self.chagepeteador = chagepeteador
        self.entregadorTardio = entregadorTardio
        self.ausencias = ausencias
        self.hablador = hablador