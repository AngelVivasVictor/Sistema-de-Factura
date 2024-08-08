import sys
sys.path.append("python-modules")
from tools.validate.validate import *
from tools.view.view import *

# Diccionario global para almacenar los proveedores
validating_existence_file("forma_pago.dat")
forma_pago = loading_file_into_memory("forma_pago.dat")
        
"""--Formas_pago = {id_pago: "Tipo de pago", activo}"""

def agregar_formas_pago():
    listem = []
    existencia = False
    print("\nSistema de Facturacion del Supermercado.\n\nMenu Agregar nuevo  forma de pago.")
    id_pago = raw_input("\n\tIngrese el ID de la forma de pago: ")
    id_pago = int(id_pago)
    for id in forma_pago.keys():
        if id == id_pago:
            existencia = True
    if existencia == False:
        tipo_pago = raw_input("\n\Ingrese la forma de pago: ")
        #ingreso datos en lista
        listem.append(tipo_pago)
        listem.append(True)
        #Agregar producto al diccionario
        forma_pago[id_pago] = listem

        #guardo el diccionario en el archivo
        saving_changes_to_the_file("forma_pago.dat", forma_pago)



def consulta_formas_pago():
    existencia = False
    print("\nSistema de Facturacion del Supermercado.\n\nMenu Consulta de forma de pago.")
    id_pago = raw_input("\n\tIngrese el ID de la forma de pago: ")
    id_pago = int(id_pago)
    for id, datos in  forma_pago.iteritems():
        if id == id_pago:
            existencia = True
            print("Producto encontrado, para el siguiente ID:", id_pago)
            print("\n")
            print("La forma de pago es: ", datos[0])
            if datos[1] == True:
                print("El estado del Proveedor es ACTIVO")
            else: 
                print("El estado del Proveedor es INACTIVO")
    if existencia == False:
        print("Forma de pago no encontrado. ")
        print("Ingrese 1 para realizar otra consulta o 2 para ingresarlo como la forma de pago nueva: ")
        opcion_elegida = raw_input(": ")
        opcion_elegida = int(opcion_elegida)
        if opcion_elegida == 1:
            agregar_formas_pago()
        elif opcion_elegida == 2:
            consulta_formas_pago()
        else:
            print("opcion invalida")

def activacion_forma_pago():
    existencia = False
    print("\nSistema de Facturacion del Supermercado.\n\nMenu activacion de forma de pago.")
    id_pago = raw_input("\n\tIngrese el ID de la forma de pago: ")
    id_pago = int(id_pago)
    for id, datos in forma_pago.items():
        if id_pago == id: 
            existencia = True
            print("\nproducto encontrado para el cuit: ", id_pago)
            if datos[1] == True:
                print("su estado actual es ACTIVO")
            else: 
                print("su estado actual es INACTIVO")
            opcion = raw_input("Ingrese 1 si quiere cambiar su estado, o 0 para salir")
            opcion = int(opcion)
            if opcion == 1:
                if datos[1] == True:
                    datos[1] = False
                    print("Su nuevo estado de la Forma de Pago es INACTIVO")
                else:
                    datos[1] = True
                    print("su nuevo estado de la Forma de Pago ES ACTIVO")
            else:
                print("Su estado no se modificara")
    if existencia == False:
        print("Proveedor no encontrado.")
        print("si quieren ingresar otro produto ingrese 'si', sino ingrese 'no' para salir")
        reintento = raw_input(": ")
        if reintento == "si":
            activacion_forma_pago()
            
    saving_changes_to_the_file("forma_pago.dat", forma_pago)
    print("Forma de pago modificado con exito!")
    print(forma_pago)

print(forma_pago)
agregar_formas_pago()
print(forma_pago)