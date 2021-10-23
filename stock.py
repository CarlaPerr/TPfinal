#! /usr/bin/python3

from producto import Producto

#Hereda de clase producto. 
#Representa una lista de productos, que tienen un nombre, su marca y precio. 
#Ademas, agrega esos productos a una lista. 
#Inicializa con una lista vacia. 

class Stock:
    def __init__(self):
        self.productos = []

    def producto_nuevo(self, nombre, marca, precio):
        p_nuevo = Producto(nombre, marca, precio)
        self.productos.append(p_nuevo)

#Retorna una lista de todos los productos que coincidan con el filtro de busqueda.

    def buscar(self, filtro):
        lista = []
        for p in self.productos:
            if p.coincide(filtro):
                lista.append(p)
        return lista




