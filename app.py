# importar clases del archivo models.py
import os
import msvcrt
from models import CatalogoPelicula
from models import Pelicula

opcion = None
opciones = (1,2,3,4)

def vhs(nombre):
    os.system('cls')
    print("")
    print(f"Catalogo:{nombre}")
    print(".------------------------.")
    print("|\\/////////       90 min |")
    print("| \/  __  ______  __     |")
    print("|    /  \|\.....|/  \    |")
    print("|    \__/|/_____|\__/    |")
    print("| A                      |")
    print("|    ________________    |")
    print("|___/_._o________o_._\___|")

def espera():
    print("\n                             Presione cualquier tecla para continuar")
    msvcrt.getch()

def continuar():
    salir = input("                             Desea continuar el Programa?\n\n                             (Responda 'Si' para continuar): ")
            
    if (salir.lower() == 'si'):
        vhs(" ")
        nombre_catalogo = input("                             Ingrese nombre del catalogo: ")
        catalogo = CatalogoPelicula(nombre_catalogo)
        espera()
    else:
        opcion = 4


vhs(" ")
nombre_catalogo = input("                             Ingrese nombre del catalogo: ")
catalogo = CatalogoPelicula(nombre_catalogo)
espera()



while opcion != 4:
    os.system('cls')
    print("")
    print(f"Catalogo:{nombre_catalogo}")
    print(".------------------------.")
    print("|\\/////////       90 min | Opciones:")
    print("| \/  __  ______  __     |")
    print("|    /  \|\.....|/  \    |   1. Agregar Pelicula")
    print("|    \__/|/_____|\__/    |   2. Listar Pelicula")
    print("| A                      |   3. Eliminar catálogo películas")
    print("|    ________________    |   4. Salir")
    print("|___/_._o________o_._\___|")

    opcion = input("                             Escribe tu opción ( del 1 al 4): ")
    while opcion.isdigit() == False or int(opcion) not in opciones:
         os.system('cls')
         print("")
         print(f"Catalogo:{nombre_catalogo}")
         print(".------------------------.")
         print("|\\/////////        90 min | Opciones:")
         print("| \/  __  ______  __     |")
         print("|    /  \|\.....|/  \    |   1. Agregar Pelicula")
         print("|    \__/|/_____|\__/    |   2. Listar Pelicula")
         print("| A                      |   3. Eliminar catálogo películas")
         print("|    ________________    |   4. Salir")
         print("|___/_._o________o_._\___|")

         opcion = input("                             Escribe tu opción ( del 1 al 4): ")
         
    opcion = int(opcion)         
        
    if opcion == 1:
        try:
            vhs(nombre_catalogo)
            nombre_pelicula = input("                             Indique el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        except:
            print("                             Error al agregar pelicula\n\n")
            continuar()
        else:
            print(f"\n                             Pelicula '{pelicula.nombre}' ha sido agregada")
            espera()

    elif opcion == 2:
        try:
            vhs(nombre_catalogo)
            print("")
            catalogo.listar_peliculas()
            espera()
        except:
            print("                             Error al listar peliculas")
            continuar()
    elif opcion == 3:
        try:
            catalogo.eliminar_peliculas()
        except:
            vhs(nombre_catalogo)
            print("\n                             Error al eliminar catalogo")
            continuar()
        else:

            vhs(nombre_catalogo)
            print("                             Archivo eliminado\n\n")
            continuar()               
else:
    vhs(nombre_catalogo)
    print("                             Programa finalizado")