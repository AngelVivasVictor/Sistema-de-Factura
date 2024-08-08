# -*- coding: utf-8 -*-
import sys
sys.path.append("python-modules")
from tools.validate.validate import *
from tools.view.view import *

# Diccionario global para almacenar los productos
validating_existence_file("productos.dat")
productos = loading_file_into_memory("productos.dat")

validating_existence_file("forma_pago.dat")
forma_pago = loading_file_into_memory("forma_pago.dat")

validating_existence_file("proveedores.dat")
proveedores = loading_file_into_memory("proveedores.dat")

validating_existence_file("clientes.dat")
clientes = loading_file_into_memory("clientes.dat")

validating_existence_file("ventas.dat")
ventas = loading_file_into_memory("ventas.dat")
"""
   ""Nombre del proyecto: sistema de facturacion de un supermercado
   
   -Estructuras de los diccionarios:-----------------------------------------------------------------------------------------------------------------------------
        #Diccionarios: clientes, productos, proveedores, ventas
        ""--Clientes = {id_cliente: [nombre completo, dni, direccion, localidad, codigo postal, telefono, mail, activo]}
        ""--Productos = {id producto:[nombre, cantidad, precio unitario, costo, id_proveedor, activo]}
        ""--Proveedores = {id_proveedor: [cuit, razon social, telefono, mail, direccion, activo]}
        ""--Formas_pago = {id_pago: "efectivo"}
          NOTA:en los MENUS "Cliente, Productos, Proveedores" deben tener la siguentes operaciones: 
                #-ingresar datos nuevos, consultar, modificar y eliminar (cambiar el estado de true o false en campo activo)
        ""-Ventas = {id_ticket: [dni, nombre completo, telefono, fecha, hora, {id_producto: [cantidad, precio_unitario]}, total, forma_pago]}
"""



def ventas():
    listem = []
    total = 0
    existencia_clientes = False
    dni_cliente = raw_input("Ingrese el DNI del Cliente: ")
    dni_cliente = int(dni_cliente)
    for dni, dato_cliente in clientes.iteritems():
        if dni_cliente == dni:
            existencia_clientes = True
            print("Cliente encontrado, para el DNI:", dni)
            listem.append(dni)
            listem.append(dato_cliente[0])
            listem.append(dato_cliente[5])
            print(listem)
    
    # --[Listado de los productos]--
    for id, datos in productos.iteritems():
            print("El producto: " + str(datos[0]) + " con el ID " + str(id))
    while existencia_clientes == True:
        # --[Ingreso de Producto]--
        existencia_productos = False
        id_producto = raw_input("Ingrese el ID del producto: ")
        id_producto = int(id_producto)
        # --[Validacion de su existencia]--
        for id, datos_producto in productos.iteritems():
            if id_producto == id:
                existencia_productos = True
        # --[Ingresa cantidad solicitada por el cliente]--
                while existencia_productos == True:
                    # --[Cantidad de producto disponible]--
                    cantidad_productos = raw_input("Ingrese la cantidad del articulos: ")
                    cantidad_productos = int(cantidad_productos)
                    stock_producto = int(datos_producto[1])
                    if stock_producto >= cantidad_productos:
                        print("La cantidad solicitada esta en disponible.")
                        listem.append(datos_producto[0])  
                        listem.append(cantidad_productos)
                        listem.append(datos_producto[2])
                        total_producto = datos_producto[2] * cantidad_productos
                        total_producto = float(total_producto)
                        listem.append(total_producto)
                        total = total + total_producto
                        print(listem)
                        print("El producto fue adquerido con exito")
                        print("Seleccione una opcion.")
                        print("1.Para ingresar otro producto.")
                        print("2.Para Finalizar el Ticket.")
                        opcion = raw_input(": ")
                        opcion = validate_integer(opcion)
                        opcion = validate_range(opcion, 1, 2)
                        if opcion == 1:
                            existencia_productos = False
                        elif opcion == 2:
                            existencia_clientes  = False
                            existencia_productos = False
                    # --[Cantidad de producto no disponible]-- 
                    else:
                        print("\nLa cantidad ingresada no esta disponible.")
                        print("Seleccione una opcion.")
                        print("1.Para ingresar una cantidad disponible.")
                        print("2.Para ingresar otro producto.")
                        opcion = raw_input(": ")
                        opcion = validate_integer(opcion)
                        opcion = validate_range(opcion, 1, 2)
                        if opcion == 1:
                            print("Reingrese la nueva cantidad.")
                        elif opcion == 2:
                            existencia_productos = False                         
        # --[Producto no existente]--     
        if existencia_productos:
            print("El producto NO esta en disponible.")
            print("1.Para ingresar un Producto disponible.")
            print("2.Para Salir del Sistema.")
            opcion = raw_input(": ")
            opcion = validate_integer(opcion)
            opcion = validate_range(opcion, 1, 2)
            if opcion == 1:
                print("Ingrese otro Producto")
                existencia_clientes == True
            elif opcion == 2:
                existencia_clientes == False
                
    listem.append(total)
    print(listem)
    # --[Cliente no existente]-- 
    if existencia_clientes == False:
        print("El Cliente no esta registrado.")
        print("1.Para ingresar un cliente registrado.")
        print("2.Para Salir del Sistema.")
        opcion = raw_input(": ")
        opcion = validate_integer(opcion)
        opcion = validate_range(opcion, 1, 2)
        if opcion == 1:
            print("Ingrese un Cliente valido.")
            ventas()
        elif opcion == 2:
            print("SALIO del sistema correctamente")

    print("Fin")   


print(clientes)
print("/n")
print(proveedores)
print("/n")
print(forma_pago)
print("/n")
print(productos)

ventas()