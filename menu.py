import random
from clases.CONSTANTES import Constantes
from clases.heroe import Heroe
import datetime
import numpy as np

from clases.villano import Villano


def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para salir")

def gestionAulaDeHeroesYVillanos(opcion):
    pass
def main():
    try:
        while True:
            menu()
            opcion = int(input("Que eliges"))
            if opcion >= 5:
                print("Selecciona una opcion valida")
            else:
                gestionAulaDeHeroesYVillanos(opcion)


    except Exception as e:
        print(f"TODOS LOS ERRORES AL LOG {e}")


if __name__ == "__main__":
    main()
def gestionAulaDeHeroesYVillanos(opcion):
    pass

idPersonajes = 0
listaPersonajes = []

def crearHeroe():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha = sacarFecha()

    codigoLimpio = random.randint(Constantes.VALOR_MINIMO,Constantes.VALOR_MAXIMO)
    bienDocumentado = random.randint(Constantes.VALOR_MINIMO,Constantes.VALOR_MAXIMO)
    gitGod = random.randint(Constantes.VALOR_MINIMO,Constantes.VALOR_MAXIMO)
    arquitecto = random.randint(Constantes.VALOR_MINIMO,Constantes.VALOR_MAXIMO)
    detallista = random.randint(Constantes.VALOR_MINIMO,Constantes.VALOR_MAXIMO)
    
    puntuaciones = [codigoLimpio,bienDocumentado,gitGod,arquitecto,detallista]
    puntuacion = np.mean(puntuaciones)

    heroe = Heroe(nombre,
                  apellidos,
                  fecha,
                  ++idPersonajes,
                  puntuacion,
                  codigoLimpio,
                  bienDocumentado,
                  gitGod,arquitecto
                  ,detallista)
    listaPersonajes.append(heroe)

def crearVillano():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha = sacarFecha()

    chagepeteador = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    entregadorTardio = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    ausencias = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    hablador = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)

    puntuaciones = [chagepeteador,entregadorTardio,ausencias,hablador]
    puntuacion = np.mean(puntuaciones)

    villano = Villano(nombre,
                apellidos,
                fecha,
                ++idPersonajes,
                puntuacion,
                chagepeteador,
                entregadorTardio,
                ausencias,
                hablador)
    listaPersonajes.append(villano)

def funcionFiltro():

def sacarFecha():
    try:
        dia = int(input("Día (1-31): "))
        mes = int(input("Mes (1-12): "))
        anio = int(input("Año: "))
        fecha = datetime.date(dia, mes, anio)
    except ValueError:
        print('Fecha incorrecta')

    return fecha