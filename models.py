import os
import msvcrt

class Pelicula:
    def __init__(self,nombre):
        self.__nombre = nombre

    #crear método __str__
    def __str__(self):
        str1 = f'Pelicula: {self.__nombre}'
        return str1
    
    #crear metodos de acceso: mostrar el atributo nombre y modificar
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
        print (f'se agrego {valor}')
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
         with open(self.ruta_archivo, 'r') as archivo:
            print(archivo.read())
            archivo.close
            

    def eliminar_peliculas(self):
        os.remove(self.ruta_archivo)
        print(f'Archivo eliminado: {self.ruta_archivo}')
