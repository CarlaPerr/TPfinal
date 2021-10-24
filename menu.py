#! /usr/bin/python3
from stock import Stock
import sys

#tener un menú, que permita al usuario acceder a las opciones, una opción para salir.

class Menu:
    '''Mostrar un menú y responder a las opciones'''

    def __init__(self):
        self.Producto = Producto()
        self.opciones= {
            "1": self.nuevo_producto,
            "2": self.modificar_producto,
            "3": self.eliminar_producto,
            "4": self.buscar_producto,
            "5": self.informe,
            "6": self.salir

    def mostrar_menu(self):
        '''Muestra el menú de opciones'''
        print("""
Menú del Stock:
1. Ingresar nuevo Producto
2. Modificar Producto
3. Eliminar Producto
4. Buscar Producto
5. Generar informe
6. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")

            # Guardamos en la variable accion el método que corresponde a la
            # opción elegida por el usuario. Por ejemplo, si opcion tiene el
            # valor 1, accion va a guardar el valor correspondiente a
            # self.opciones[1], es decir: self.mostrar_notas
            accion = self.opciones.get(opcion)

            # Si hay algún valor guardado en accion, ejecutamos el método que
            #tiene ese nombre, y si no mostramos un error:
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

 #Solicitar un nombre, marca, precio para agregar un nuevo producto.
    def nuevo_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = input("Ingrese el precio del producto: ")
        self.stock.producto_nuevo(nombre, marca, precio)
        print("Su Producto ha sido cargado correctamente.")
        
 #Solicitar el nombre del producto a modificar, busca el producto y le modifica la marca y el precio. 
    def modificar_producto(self):
        nombre = input("Ingrese el nombre del prodcuto a modificar: ")
        marca = input("Ingrese la nueva marca del prodcuto: ")
        precio = input("Ingrese el nuevo precio del prodcuto: ")
        if marca:
            self.stock.modificar_marca(nombre, marca)
        if precio:
            self.stock.modificar_precio(nombre, precio)

 #Solicita una busqueda y muestra el producto que coincide, si es que existe. 
    def buscar_producto(self):
        filtro = input("Buscar: ")
        Producto = self.stock.buscar(filtro)
        if Producto:
            self.productos(Producto)
        else:
            print("Ningun producto coincide con la búsqueda")

    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar(). 
if __name__ == "__main__":
    Menu().ejecutar() 

