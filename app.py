# importar clases del archivo models.py
import os
from models import CatalogoPelicula
from models import Pelicula

opcion = None
opciones = (1,2,3,4)

nombre_catalogo = input("\nIngrese nombre del catalogo:")
catalogo = CatalogoPelicula(nombre_catalogo)

while opcion != 4:
    print("\nOpciones:\n")
    print("1. Agregar Pelicula")
    print("2. Listar Pelicula")
    print("3. Eliminar catálogo películas")
    print("4. Salir")

    opcion = int(input("\nEscribe tu opción ( del 1 al 4):"))
            
        
    if opcion == 1:
        try:
            nombre_pelicula = input("\nIndique el nombre de la pelicula:")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        except:
            print("\nError al agregar pelicula\n\n")
            nombre_catalogo = input("\nIngrese nombre del catalogo:")
            catalogo = CatalogoPelicula(nombre_catalogo)
        else:
            print(f"\nPelicula '{pelicula.nombre}' ha sido agregada\n\n")
    elif opcion == 2:
        try:
            print("\n\n")
            catalogo.listar_peliculas()
        except:
            print("\nError al listar peliculas\n\n")
            nombre_catalogo = input("Ingrese nombre del catalogo:")
            catalogo = CatalogoPelicula(nombre_catalogo)
        
    elif opcion == 3:
        try:
            catalogo.eliminar_peliculas()
        except:
            print("\nError al eliminar catalogo\n\n")
            nombre_catalogo = input("Ingrese nombre del catalogo:")
            catalogo = CatalogoPelicula(nombre_catalogo)

        else:
            print("\nArchivo eliminado\n\n")
            salir = input("Desea continuar el Programa?\n\n(Responda 'Si' para continuar)")
            if (salir.lower == 'si'):
                nombre_catalogo = input("\nIngrese nombre del catalogo:")
                catalogo = CatalogoPelicula(nombre_catalogo)
            else:
                opcion = 4
                           
else:
    print("\nPrograma finalizado")