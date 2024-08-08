# -*- coding: utf-8 -*-

"""--Proveedores = {cuit(2 digitos + dni + 1 digitos): [razon social, telefono, mail, direccion, activo]}"""

import sys
sys.path.append("python-modules")
from tools.validate.validate import *
from tools.view.view import *

# Diccionario global para almacenar los proveedores
validating_existence_file("proveedores.dat")
proveedores = loading_file_into_memory("proveedores.dat")

def agregar_proveedor():
    listem = []
    existencia = False
    print("\nSistema de Facturacion del Supermercado.\n\nMenu Agregar nuevo proveedor.")
    cuit_proveedor = raw_input("\n\tIngrese el CUIT del proveedor: ")
    cuit_proveedor = int(cuit_proveedor)
    for id in proveedores.keys():
        if cuit_proveedor == id:
            existencia = True
    if existencia == False:
        razon_social = raw_input("\n\Ingrese la razon social del proveedor: ")
        telefono = raw_input("\n\Ingrese el telefono proveedor: ")
        telefono = int(telefono)
        mail = raw_input("\n\Ingrese el mail del proveedor: ")
        direccion = raw_input("\n\Ingrese la direccion del proveedor: ")
        #ingreso datos en lista
        listem.append(razon_social)
        listem.append(telefono)
        listem.append(mail)
        listem.append(direccion)
        listem.append(True)
            
        #Agregar producto al diccionario
        proveedores[cuit_proveedor] = listem

        #guardo el diccionario en el archivo
        saving_changes_to_the_file("proveedores.dat", proveedores)

    #validacion de producto existente
    if cuit_proveedor == True:
        print("\nEl producto con el ID: , " + str(cuit_proveedor) + ". ya esta registado.")
        print("\nSeleccione una opcion:")
        print("\n1.Visualizar el estado del producto.")
        print("\n2.Consultar los datos del producto.")
        print("\n3.Ingresar otro producto nuevo.")
        print("\n4.Volver al menu principal.")
        #opcion = raw_input(": ")
        #opcion = int(opcion)
        #if opcion == 1:
         #      consulta_producto()
        #elif opcion == 2:
            #   #llamar funcion
        #elif opcion == 3:
        #    #llamar funcion
        #elif opcion == 4:
            #llamar funcion
        #    print("salio con exito")

def consulta_proveedores():
    existencia = False
    cuit_proveedor = raw_input("\n\tIngrese el CUIT del proveedor: ")
    cuit_proveedor = int(cuit_proveedor)
    for cuit, datos in  proveedores.iteritems():
        if cuit == cuit_proveedor:
            existencia = True
            print("Producto encontrado, para el siguiente ID:", cuit_proveedor)
            print("\n")
            print("La razon social del proveedor es: ", datos[0])
            print("El teleno del proveedor es: ", datos[1])
            print("El Mail del Proveedor es: ", datos[2])
            print("La direccion del proveedor es: ", datos[3])
            if datos[4] == True:
                print("El estado del Proveedor es ACTIVO")
            else: 
                print("El estado del Proveedor es INACTIVO")
    if existencia == False:
        print("Proveedor no encontrado. ")
        print("Ingrese 1 para realizar otra consulta o 2 para ingresarlo como Proveedor nuevo: ")
        opcion_elegida = raw_input(": ")
        opcion_elegida = int(opcion_elegida)
        if opcion_elegida == 1:
            consulta_proveedores()
        elif opcion_elegida == 2:
            agregar_proveedor()
        else:
            print("opcion invalida")


def modificacion_proveedor():
    existencia = False
    cuit_proveedor = raw_input("\n\tIngrese el CUIT del proveedor: ")
    cuit_proveedor = int(cuit_proveedor)
    for cuit, datos in proveedores.iteritems():
        if cuit == cuit_proveedor :
            existencia = True
            print("Producto encontrado, para el siguiente ID:", cuit_proveedor)
            print("\n")
            print("La razon social del proveedor es: ", datos[0])
            print("El telefono del proveedor es: ", datos[1])
            print("El Mail del Proveedor es: ", datos[2])
            print("La direccion del proveedor es: ", datos[3])
            if datos[4] == True:
                print("El estado del Proveedor es ACTIVO")
            else: 
                print("El estado del Proveedor es INACTIVO")

            print("\nSeleccione el dato a modificar")
            print("\n1. Razon social")
            print("\n2. Telefono")
            print("\n3. Mail")
            print("\n4. Direccion")
            opciones_validas = (1, 2, 3, 4)
            opcion = raw_input(": ")
            opcion = int(opcion)
            while opcion in opciones_validas:
                if opcion == 1:
                    dato_modificar = raw_input("Ingrese la nueva razon social del proveedor: ")
                    datos[0] = dato_modificar
                    print("La nuevo razon social del proveedor es: ", dato_modificar)
                
                elif opcion == 2:
                    dato_modificar = raw_input("Ingrese el nuevo telefono del proveedor es: ")
                    datos[1] = dato_modificar
                    print("El nuevo telefono del proveedor es: ", dato_modificar)
                    
                elif opcion == 3:
                    dato_modificar = raw_input("Ingrese el nuevo mail del Proveedor es: ")
                    datos[2] = dato_modificar
                    print("el nuevo mail del proveedor es: ", dato_modificar)
                    
                elif opcion == 4:
                    dato_modificar = raw_input("Ingrese la nueva direccion del proveedor es: ")
                    datos[3] = dato_modificar
                    print("La nueva direccion del proveedor es: ", dato_modificar)
                    
                opcion = raw_input("Si desea realizar otra modificacion, seleccione el dato correspondiente, sino 0 para salir ")
                opcion = int(opcion)
            proveedores[cuit] = datos
    if existencia == False:
        print("\nEl producto no se encuentra registrado, ")
        print("si desea ingresar otro id de proucto ingrese 'si', sino ingrese 'no'")
        reingreso = raw_input(": ")
        if reingreso == "si":
            modificacion_proveedor()
    saving_changes_to_the_file("proveedores.dat", proveedores)
    print("Proveedor modificado con exito!")
    print(proveedores)

def activacion_producto():
    existencia = False
    cuit_proveedor = raw_input("\n\tIngrese el CUIT del proveedor: ")
    cuit_proveedor = int(cuit_proveedor)
    for cuit, datos in proveedores.items():
        if cuit == cuit_proveedor: 
            existencia = True
            print("\nproducto encontrado para el cuit: ", cuit_proveedor)
            if datos[4] == True:
                print("su estado actual es ACTIVO")
            else: 
                print("su estado actual es INACTIVO")
            opcion = raw_input("Ingrese 1 si quiere cambiar su estado, o 0 para salir")
            opcion = int(opcion)
            if opcion == 1:
                if datos[4] == True:
                    datos[4] = False
                    print("Su nuevo estado para el Proveedor es INACTIVO")
                else:
                    datos[4] = True
                    print("su nuevo estado para el Proveedor ES ACTIVO")
            else:
                print("Su estado no se modificara")
    if existencia == False:
        print("Proveedor no encontrado.")
        print("si quieren ingresar otro produto ingrese 'si', sino ingrese 'no' para salir")
        reintento = raw_input(": ")
        if reintento == "si":
            activacion_producto()
            
    saving_changes_to_the_file("proveedores.dat", proveedores)
    print("Proveedor modificado con exito!")
    print(proveedores)


print(proveedores)
activacion_producto()