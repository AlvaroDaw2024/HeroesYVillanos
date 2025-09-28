

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

def crearHeroe():
    pass

def crearVillano():
    pass