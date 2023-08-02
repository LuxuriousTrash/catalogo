import os

class Pelicula:
    def __init__(self,nombre):
        self.__nombre = nombre

    #crear método __str__

    #crear metodos de acceso: mostrar el atributo nombre y modificar

class CatalogoPelicula:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        # abrir el archivo con with 
        # imprimir lo que hay en el archivo ( arhivo.read() )
        pass

    def eliminar_peliculas(self):
        os.remove(self.ruta_archivo)
        print(f'Archivo eliminado: {self.ruta_archivo}')
