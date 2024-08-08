# -*- coding: utf-8 -*-

# ---------------------------Modulos Importados---------------------------
import sys
sys.path.append("python-modules")
from tools.validate.validate import *
from tools.view.view import *
# ------------------------------------------------------------------------
# Carga de diccionario global para almacenar los datos
validating_existence_file("productos.dat")
productos = loading_file_into_memory("productos.dat")

# ---------------------------Fun. Agregar Productos---------------------------
def agregar_producto():
    # --[Ingreso de Producto]--
    listem = []
    id_existe = False
    print("\nSistema de Facturacion del Supermercado.\n\nMenu Agregar nuevo producto.")
    id_producto = raw_input("\n\tIngrese el ID del product: ")
    id_producto = int(id_producto)
    # --[Verifiacion de Producto existente]--
    for id in productos.keys():
        if id_producto == id:
            id_existe = True
    # --[Ingreso de datos]--       
    if id_existe == False:
        nombre_producto = raw_input("\nIngrese el nombre del producto: ")
        cantidad_producto = raw_input("\nIngrese la cantidad de productos: ")
        cantidad_producto = int(cantidad_producto)
        precio_unitario = raw_input("\nIngrese el precio unitario del producto: ")
        precio_unitario = float(precio_unitario)
        costo_unitario = raw_input("\nIngrese el costo unitario del producto: ")
        costo_unitario = float(costo_unitario)
        id_proveedor = raw_input("\nIngrese el id del proveedor del producto: ")
        id_proveedor = int(id_proveedor)
        # --[Guardado de datos]--
        listem.append(nombre_producto)
        listem.append(cantidad_producto)
        listem.append(precio_unitario)
        listem.append(costo_unitario)
        listem.append(id_proveedor)
        listem.append(True)
            
        # --[Agregar el Producto al diccionario]--
        productos[id_producto] = listem
        saving_changes_to_the_file("productos.dat", productos)
        print("\Producto agregado con éxito!")
    #validacion de producto existente
    if id_existe == True:
        print("\nEl producto con el ID: , " + str(id_producto) + ". ya esta registado.")
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
# ------------------------------------------------------------------------
# ---------------------------Fun. Cons. Productos---------------------------
def consulta_producto():
    # --[Ingreso de datos]--
    existencia = False
    id_consulta = raw_input("\n\Ingrese el ID del producto a consultar:")
    id_consulta = int(id_consulta)
    # --[Verifiacion de cliente existente]--     
    for id, datos in productos.iteritems():
        if id == id_consulta:
            # --[Imprime los datos buscados e existentes]--
            print("Producto encontrado, para el siguiente ID:", id_consulta)
            print("\n")
            print("El Nombre del producto es: ", datos[0])
            print("La cantidad de unidades que hay en stock es: ", datos[1])
            print("El precio unitario de venta es: ", datos[2])
            print("El costo unitario es: ", datos[3])
            print("El id del proveedor es: ", datos[4])
            if datos[5] == True:
                print("El estado del producto es ACTIVO")
            else: 
                print("El estado del producto es INACTIVO")
            existencia = True
    # --[Control de NO usuario existente]--
    if existencia == False:
        print("Producto no encontrado.")
        print("\nSeleccione una opcion:")
        print("\n1.Visualizar el datos de otro Producto.")
        print("\n2.Ingresar el nuevo Producto.")
        print("\n3.Volver al menu principal.")
        opcion = raw_input(": ")
        opcion = validate_range(opcion, 1, 3)
        if opcion == 1:
            consulta_producto()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            #importar modulo
            print("salio con exito")
# ------------------------------------------------------------------------

# ---------------------------Fun. Modi. Cliente---------------------------
def modificacion_productos():
   # --[Ingreso de datos]--
    existencia = False
    id_consulta = raw_input("\n\Ingrese el id del producto a modificar:")
    id_consulta = int(id_consulta)
    # --[Verifiacion de cliente existente]--
    for id, datos in productos.iteritems():
        # --[Imprime los datos buscados e existentes]--
        if id == id_consulta:  
            print("Producto encontrado, para el siguiente ID:", id_consulta)
            print("\n")
            print("El Nombre del producto es: ", datos[0])
            print("La cantidad de unidades que hay en stock es: ", datos[1])
            print("El precio unitario de venta es: ", datos[2])
            print("El costo unitario es: ", datos[3])
            print("El id del proveedor es: ", datos[4])
            if datos[5] == True:
                print("El estado del producto es ACTIVO")
            else: 
                print("El estado del producto es INACTIVO")
            existencia = True
            print("\nSeleccione el dato a modificar")
            print("\n1. Nombre")
            print("\n2. Cantidad de unidades")
            print("\n3. precio unitario")
            print("\n4. Costo unitario")
            print("\n5. id proveedor")
            opciones_validas = (1, 2, 3, 4, 5)
            opcion = raw_input(": ")
            opcion = int(opcion)
            while opcion in opciones_validas:
                if opcion == 1:
                    dato_modificar = raw_input("Ingrese el nuevo nombre del producto: ")
                    datos[0] = dato_modificar
                    print("el nuevo nombre del producto es: ", dato_modificar)
                elif opcion == 2:
                    dato_modificar = raw_input("Ingrese la cantidad de unidades nuevas del producto: ")
                    datos[1] =  validate_integer(dato_modificar)
                    print("La cantidad de unidades del producto es: ", dato_modificar)
                elif opcion == 3:
                    dato_modificar = raw_input("Ingrese el nuevo precio del producto: ")
                    datos[2] = dato_modificar
                    print("el nuevo precio del producto es: ", dato_modificar)
                elif opcion == 4:
                    dato_modificar = raw_input("Ingrese el nuevo costo del producto: ")
                    datos[3] = dato_modificar
                    print("el nuevo costo nombre del producto es: ", dato_modificar)
                elif opcion == 5:
                    dato_modificar = raw_input("Ingrese el nuevo id proveedor del producto: ")
                    datos[4] = dato_modificar
                    print("el nuevo id proveedor del producto es: ", dato_modificar)
                opcion = raw_input("Si desea realizar otra modificacion, seleccione el dato correspondiente, sino 0 para salir ")
                opcion = int(opcion)
            productos[id] = datos
    # --[Control de NO usuario existente]--
    if existencia == False:
        print("\nEl producto no se encuentra registrado, ")
        print("si desea ingresar otro id de proucto ingrese 'si', sino ingrese 'no'")
        reingreso = raw_input(": ")
        if reingreso == "si":
            modificacion_productos()
    saving_changes_to_the_file("productos.dat", productos)
    print("Producto modificado con exito!")
    print(productos)
# ------------------------------------------------------------------------
# ---------------------------Fun. Acti. Cliente---------------------------
def activacion_producto():
   # --[Ingreso de datos]--
    existencia = False
    id_consulta = raw_input("\n\Ingrese el id del producto a consultar:")
    id_consulta = int(id_consulta)
    for id, datos in productos.items():
        # --[Verifiacion de cliente existente]--
        if id == id_consulta: 
            existencia = True
            print("\nproducto encontrado para el id: ", id_consulta)
            print("\n")
            if datos[5] == True:
                print("su estado actual es ACTIVO")
            else: 
                print("su estado actual es INACTIVO")
            print("1.Para cambiar el estado: Activo o Inactivo.")
            print("2.Para conservar el estado actual.")
            opcion = raw_input(": ")
            opcion = validate_range(opcion, 1, 2)
            if opcion == 1:
                if datos[5] == True:
                    datos[5] = False
                    print("Su nuevo estado para el producto es INACTIVO")
                else:
                    datos[5] = True
                    print("su nuevo estado para el producto ES ACTIVO")
            else:
                print("Su estado no se modificara")
    if existencia == False:
        print("Producto no encontrado.")
        print("si quieren ingresar otro produto ingrese 'si', sino ingrese 'no' para salir")
        reintento = raw_input(": ")
        if reintento == "si":
            activacion_producto()
            
    saving_changes_to_the_file("productos.dat", productos)
    print("Producto modificado con exito!")
    print(productos)
# ------------------------------------------------------------------------

print(productos)
modificacion_productos()                