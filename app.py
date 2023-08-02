# importar clases del archivo models.py

opcion = None

nombre_catalogo = input("Ingrese nombre del catalogo:")
catalogo = CatalogoPelicula(nombre_catalogo)

while opcion != 4:
    print("Opciones: ")
    print("1. Agregar Pelicula")
    print("2. Listar Pelicula")
    print("3. Eliminar catálogo películas")
    print("4. Salir")

    opcion = int(input("Escribe tu opción ( del 1 al 4):"))

    if opcion == 1:
        nombre_pelicula = input(" Indique el nombre de la pelicula:")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar_pelicula(pelicula)
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass

else:
    print("Programa finalizado")