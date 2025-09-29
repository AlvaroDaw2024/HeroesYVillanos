import random
from clases.CONSTANTES import Constantes
from clases.heroe import Heroe
import datetime
import numpy as np
import logging

from clases.villano import Villano


def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para simular una pelea entre un villano y un héroe")
    print("5) Para salir")

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
            if opcion >= 6:
                print("Selecciona una opcion valida")
            else:
                gestionAulaDeHeroesYVillanos(opcion)


    except Exception as e:
        print(f"TODOS LOS ERRORES AL LOG {e}")


if __name__ == "__main__":
    main()


def gestionAulaDeHeroesYVillanos(opcion):
    match opcion:
        case 1:
            crearHeroe()
        case 2:
            crearVillano()
        case 3:
            funcionFiltro()
        case 4:
            emparejarHeroeVillano()
        case 5:
            exit()



idPersonajes = 0
listaPersonajes = []


def crearHeroe():
    global idPersonajes  # Necesitamos modificar la variable global, sacado del gpt que no sabia como iba en py
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha = sacarFecha()


    codigoLimpio = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    bienDocumentado = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    gitGod = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    arquitecto = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    detallista = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)


    atributos = [codigoLimpio, bienDocumentado, gitGod, arquitecto, detallista]
    puntuacion = np.mean(atributos)


    idPersonajes += 1
    heroe = Heroe(nombre,
                  apellidos,
                  fecha,
                  idPersonajes,
                  puntuacion,
                  codigoLimpio,
                  bienDocumentado,
                  gitGod, arquitecto
                  , detallista)
    listaPersonajes.append(heroe)
    logging.info(f'Héroe creado: {nombre} {apellidos} con ID {idPersonajes} y puntuación {puntuacion}')


def crearVillano():
    global idPersonajes
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha = sacarFecha()

    chagepeteador = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    entregadorTardio = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    ausencias = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)
    hablador = random.randint(Constantes.VALOR_MINIMO, Constantes.VALOR_MAXIMO)

    atributos = [chagepeteador, entregadorTardio, ausencias, hablador]
    puntuacion = np.mean(atributos)

    idPersonajes += 1
    villano = Villano(nombre,
                      apellidos,
                      fecha,
                      idPersonajes,
                      puntuacion,
                      chagepeteador,
                      entregadorTardio,
                      ausencias,
                      hablador)
    listaPersonajes.append(villano)
    logging.info(f'Villano creado: {nombre} {apellidos} con ID {idPersonajes} y puntuación {puntuacion}')


def emparejarHeroeVillano():

    heroes = [p for p in listaPersonajes if type(p) == Heroe]
    villanos = [p for p in listaPersonajes if type(p) == Villano]


    heroe = random.choice(heroes)
    villano = random.choice(villanos)

    logging.info(f"Emparejamiento: {heroe.returnNombre()} vs {villano.returnNombre()}")



def funcionFiltro():
    while True:
        menuFiltro()
        opcion = int(input())
        if opcion == 2:
            villanos = [p for p in listaPersonajes if type(p) == Villano]
            menuFiltroVillano()
            opcion2 = int(input('Elige: '))
            match opcion2:
                case 1:
                    nombre = input('Escribe el nombre: ').lower()
                    for villano in villanos:
                        if villano.returnNombre().lower() == nombre:
                            print('Villano encontrado!')
                            print(villano)
                case 2:
                    apellido = input('Escribe el apellido: ').lower()
                    for villano in villanos:
                        if villano.returnApellidos().lower() == apellido:
                            print('Villano encontrado!')
                            print(villano)
                case 3:
                    idv = int(input('Escribe la ID: '))
                    for villano in villanos:
                        if villano.returnId() == idv:
                            print('Villano encontrado!')
                            print(villano)
                case 4:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
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
                        case _:
                            print('Opcion incorrecta')
                case 5:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
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
                        case _:
                            print('Opcion incorrecta')
                case 6:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
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
                        case _:
                            print('Opcion incorrecta')
                case 7:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
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
                        case _:
                            print('Opcion incorrecta')
                case 8:
                    for villano in villanos:
                        print(villano)
                case 9:
                    print('Saliendo del filtro de villanos')
                    break
                case _:
                    print('Opcion incorrecta')

        elif opcion == 1:
            heroes = [p for p in listaPersonajes if type(p) == Heroe]
            menuFiltroHeroe()
            opcion2 = int(input('Elige: '))
            match opcion2:
                case 1:
                    nombre = input('Escribe el nombre: ').lower()
                    for heroe in heroes:
                        if heroe.returnNombre().lower() == nombre:
                            print('Héroe encontrado!')
                            print(heroe)
                case 2:
                    apellido = input('Escribe el apellido: ').lower()
                    for heroe in heroes:
                        if heroe.returnApellidos().lower() == apellido:
                            print('Héroe encontrado!')
                            print(heroe)
                case 3:
                    idv = int(input('Escribe la ID: '))
                    for heroe in heroes:
                        if heroe.returnId() == idv:
                            print('Héroe encontrado!')
                            print(heroe)
                case 4:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
                    match opcion3:
                        case 1:
                            for heroe in heroes:
                                if heroe.returnCodigoLimpio() > cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 2:
                            for heroe in heroes:
                                if heroe.returnCodigoLimpio() < cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 3:
                            for heroe in heroes:
                                if heroe.returnCodigoLimpio() == cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case _:
                            print('Opcion incorrecta')
                case 5:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
                    match opcion3:
                        case 1:
                            for heroe in heroes:
                                if heroe.returnBienDocumentado() > cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 2:
                            for heroe in heroes:
                                if heroe.returnBienDocumentado() < cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 3:
                            for heroe in heroes:
                                if heroe.returnBienDocumentado() == cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case _:
                            print('Opcion incorrecta')
                case 6:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
                    match opcion3:
                        case 1:
                            for heroe in heroes:
                                if heroe.returnGitgod() > cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 2:
                            for heroe in heroes:
                                if heroe.returnGitgod() < cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 3:
                            for heroe in heroes:
                                if heroe.returnGitgod() == cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case _:
                            print('Opcion incorrecta')
                case 7:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
                    match opcion3:
                        case 1:
                            for heroe in heroes:
                                if heroe.returnArquitecto() > cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 2:
                            for heroe in heroes:
                                if heroe.returnArquitecto() < cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 3:
                            for heroe in heroes:
                                if heroe.returnArquitecto() == cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case _:
                            print('Opcion incorrecta')
                case 8:
                    menuMayorMenor()
                    opcion3 = int(input('Elige: '))
                    cantidad = int(input('Y ahora el numero: '))
                    match opcion3:
                        case 1:
                            for heroe in heroes:
                                if heroe.returnDetallista() > cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 2:
                            for heroe in heroes:
                                if heroe.returnDetallista() < cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case 3:
                            for heroe in heroes:
                                if heroe.returnDetallista() == cantidad:
                                    print('Héroe encontrado!')
                                    print(heroe)
                        case _:
                            print('Opcion incorrecta')
                case 9:
                    for heroe in heroes:
                        print(heroe)
                case 10:
                    print('Saliendo del filtro de héroes')
                    break
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
