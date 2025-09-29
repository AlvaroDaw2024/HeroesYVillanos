from persona import Persona

class Heroe(Persona):

    def __init__(self,nombre,apellidos, fnac, id, puntuacion,codigoLimpio,bienDocumentado,gitgod,arquitecto,detallista):
        super().__init__(self,nombre,apellidos,fnac,id,puntuacion)
        self.codigoLimpio = codigoLimpio
        self.bienDocumentado = bienDocumentado
        self.gitgod = gitgod
        self.arquitecto = arquitecto
        self.detallista = detallista

    def returnCodigoLimpio(self):
        return self.codigoLimpio
    def returnBienDocumentado(self):
        return self.bienDocumentado
    def returnGitgod(self):
        return self.gitgod
    def returnArquitecto(self):
        return self.arquitecto
    def returnDetallista(self):
        return self.detallista

    def __str__(self):
        return f'Heroe ' + super().__str__()
    #esto lo he pensado yo, no se si esta correcto
