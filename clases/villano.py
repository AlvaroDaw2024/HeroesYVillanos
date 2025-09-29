from persona import Persona

class Villano(Persona):

    def __init__(self,nombre,apellidos, fnac, id, puntuacion,chagepeteador,entregadorTardio,ausencias,hablador):
        super().__init__(self,nombre,apellidos,fnac,id,puntuacion)
        self.chagepeteador = chagepeteador
        self.entregadorTardio = entregadorTardio
        self.ausencias = ausencias
        self.hablador = hablador

    def returnChagepeteador(self):
        return self.chagepeteador
    def returnEntregadorTardio(self):
        return self.entregadorTardio
    def returnHablador(self):
        return self.hablador
    def returnAusencias(self):
        return self.ausencias
