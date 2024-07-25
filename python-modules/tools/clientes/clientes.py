# -*- coding: utf-8 -*-


import sys
sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

# Diccionario global para almacenar los clientes
validating_existence_file("clientes.dat")
clientes = loading_file_into_memory("clientes.dat")

def ingreso_cliente():
    # Ingreso de datos
     listem = []
     print("\nSistema de Facturacio del Supermercado.\n\nMenu Agregar nuevo cliente.")
     dato = raw_input("\n\tNombre Completo: ") # dato N° 0
     listem.append(dato)
     dato = raw_input("\n\tNumero de D.N.I: ") # dato N° 1
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tDireccion: ") # dato N° 2
     listem.append(dato)
     dato = raw_input("\n\tLocalidad: ") # dato N° 3
     listem.append(dato)
     dato = raw_input("\n\tCodigo Postal: ") # dato N° 4
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tNumero de Telefono: ") # dato N° 5
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tCorreo Electronico: ") # dato N° 6
     listem.append(dato)
     dato = True # dato N° 7 
     listem.append(dato) 
     
# Usar el DNI como ID único para el cliente
     id_cliente = listem[1]

    # Agregar el nuevo cliente al diccionario
     clientes[id_cliente] = listem
    
    # Mostrar el diccionario de clientes
     print(clientes)
    
     # Guardar los cambios en el archivo
     saving_changes_to_the_file("clientes.dat", clientes)
     print("\nCliente agregado con éxito!")


def consulta_cliente():
     dni_consulta = raw_input("Ingrese DNI del cliente a consultar:")
     dni_consulta = int(dni_consulta)
     loop = False
     
     for id,datos in clientes.iteritems():
          if dni_consulta in id:
               datos = clientes[dni_consulta]
               print("Cliente existente, para el siguiente D.N.I:", id)
               print("\n")
               print("Su Nombre completo es: ", datos[0])
               print("Su Direccion es: ", datos[2])
               print("Su Localidad es: ", datos[3])
               print("Su Codigo Postal es: ", datos[4])
               print("Su Numero de telefo es: ", datos[5])
               print("Su Correo Electronico es: ", datos[6])
               if datos[7] == True:
                    print("Su estado es ACTIVO")
               else:
                    print("Su estado es INACTIVO")
               loop = True
          else:
               print("Usuario no encontrado, Ingrese 1 para registralo como cliente nuevo o 2 si quiere realizar otra consulta: ")
               opcion = raw_input(": ")
               if opcion == 1:
                    ingreso_cliente()
               else:
                    consulta_cliente()
print(clientes)
consulta_cliente()
