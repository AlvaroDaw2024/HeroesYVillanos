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

def menuFiltro():
    print('1) Para buscar Heroe')
    print('2) Para buscar Villano')

def menuFiltroVillano():
    pass

def menuFiltroHeroe():
    pass

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

    codigoLimpio = 0
    bienDocumentado = 0
    gitGod = 0
    arquitecto = 0
    detallista = 0

    atributos = [codigoLimpio, bienDocumentado, gitGod, arquitecto, detallista]
    for puntuacion in atributos:
        atributos[puntuacion] = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    puntuacion = np.mean(atributos)

    heroe = Heroe(nombre,
                  apellidos,
                  fecha,
                  ++idPersonajes,
                  puntuacion,
                  codigoLimpio,
                  bienDocumentado,
                  gitGod, arquitecto
                  , detallista)
    listaPersonajes.append(heroe)


def crearVillano():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha = sacarFecha()

    chagepeteador = 0
    entregadorTardio = 0
    ausencias = 0
    hablador = 0

    atributos = [chagepeteador, entregadorTardio, ausencias, hablador]
    for puntuacion in atributos:
        atributos[puntuacion] = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    puntuacion = np.mean(atributos)

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
    while True:
        menuFiltro()
        opcion = int(input())
        if (opcion==1):
            menuFiltroVillano()
            pass
        elif (opcion==2):
            menuFiltroHeroe()
            pass
        else:
            print('No has elegido una opción valida')



def sacarFecha():
    try:
        dia = int(input("Día (1-31): "))
        mes = int(input("Mes (1-12): "))
        anio = int(input("Año: "))
        fecha = datetime.date(dia, mes, anio)
    except ValueError:
        print('Fecha incorrecta')

    return fecha
