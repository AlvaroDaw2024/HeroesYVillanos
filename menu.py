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
    print('1) Buscar por nombre')
    print('2) Buscar por apellidos')
    print('3) Buscar por ID')
    print('4) Filtrar por chagepeteador')
    print('5) Filtrar por entregador tardío')
    print('6) Filtrar por hablador')
    print('7) Filtrar por ausencias')
    print('8) Mostrar todos los villanos')
    print('9) Salir')

def menuFiltroHeroe():
    print('1) Buscar por nombre')
    print('2) Buscar por apellidos')
    print('3) Buscar por ID')
    print('4) Filtrar por código limpio')
    print('5) Filtrar por bien documentado')
    print('6) Filtrar por GitGod')
    print('7) Filtrar por arquitecto')
    print('8) Filtrar por detallista')
    print('9) Mostrar todos los héroes')
    print('10) Salir')

def menuMayorMenor:
    print('1) Mayor')
    print('2) Menor')
    print('3) Exacto')

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
        if opcion==2:
            villanos = [p for p in listaPersonajes if type(p) == Villano]
            menuFiltroVillano()
            opcion2 = int(input('Elige'))
            match opcion2:
                case 1:
                    nombre = input('Escribe el nombre').lower()
                    for villano in villanos:
                        if villano.returnNombre().lower == nombre:
                            print('Villano encontrado!')
                            print(villano)
                case 2:
                    apellido = input('Escribe el apellido').lower()
                    for villano in villanos:
                        if villano.returnApellidos().lower == apellido:
                            print('Villano encontrado!')
                            print(villano)
                case 3:
                    idv = int(input('Escribe la ID'))
                    for villano in villanos:
                        if villano.returnId() == idv:
                            print('Villano encontrado!')
                            print(villano)
                case 4:
                    menuMayorMenor()
                    opcion3 = int(input('Elige'))
                    cantidad = int(input('Y ahora el numero'))
                    match opcion3:
                        case 1:
                            for villano in villanos:
                                if villano.returnChagepeteador() > cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 2:
                            for villano in villanos:
                                if villano.returnChagepeteador() < cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 3:
                            for villano in villanos:
                                if villano.returnChagepeteador() == cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                case 5:
                    menuMayorMenor()
                    opcion3 = int(input('Elige'))
                    cantidad = int(input('Y ahora el numero'))
                    match opcion3:
                        case 1:
                            for villano in villanos:
                                if villano.returnEntregadorTardio() > cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 2:
                            for villano in villanos:
                                if villano.returnEntregadorTardio() < cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 3:
                            for villano in villanos:
                                if villano.returnEntregadorTardio() == cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                case 6:
                    menuMayorMenor()
                    opcion3 = int(input('Elige'))
                    cantidad = int(input('Y ahora el numero'))
                    match opcion3:
                        case 1:
                            for villano in villanos:
                                if villano.returnHablador() > cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 2:
                            for villano in villanos:
                                if villano.returnHablador() < cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 3:
                            for villano in villanos:
                                if villano.returnHablador() == cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                case 7:
                    menuMayorMenor()
                    opcion3 = int(input('Elige'))
                    cantidad = int(input('Y ahora el numero'))
                    match opcion3:
                        case 1:
                            for villano in villanos:
                                if villano.returnAusencias() > cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 2:
                            for villano in villanos:
                                if villano.returnAusencias() < cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                        case 3:
                            for villano in villanos:
                                if villano.returnAusencias() == cantidad:
                                    print('Villano encontrado!')
                                    print(villano)
                case 8:
                    for villano in villanos:
                        print(villano)

                case 9:
                    print('Saliendo')
                    exit()

        elif opcion==1:
            menuFiltroHeroe()
            opcion2 = int(input('Elige'))
            match opcion2:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    print('Saliendo')
                    exit()
                case _:
                    print('Opcion incorrecta')
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
