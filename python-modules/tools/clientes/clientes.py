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
     loop = True
     
     for id,datos in clientes.iteritems():
          if dni_consulta == id and loop == True:
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
               loop = False
     if loop == True:
          print("Usuario no encontrado")
          print("Ingrese 1 para registralo como cliente nuevo o 2 si quiere realizar otra consulta: ")
          opcion = raw_input(": ")
          opcion = int(opcion)
          if opcion == 1:
               ingreso_cliente()
          elif opcion == 2:
               consulta_cliente()

def modificacion_datos():
     dni_consulta = raw_input("Ingrese DNI del cliente que desea modificar: ")
     dni_consulta = int(dni_consulta)
     loop = True
     
     for id,datos in clientes.iteritems():
          if dni_consulta == id and loop == True:
               print("Cliente encontrado, para el siguiente D.N.I:", id)
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
               loop = False
               print("\n\tSeleccione el dato a modificar\n\t")
               print("\n\t1.Nombre completo")
               print("\n\t2.Direccion")
               print("\n\t3.Localidad")
               print("\n\t4.Codigo Postal")
               print("\n\t5.Numero de telefo")
               print("\n\t6.Correo Electronico")
               opcion = raw_input("Ingrese valor correspondiente al dato:")
               opcion = int(opcion)
               while opcion != 0:
                    if opcion == 1:
                         dato_modifar = raw_input("Ingrese nuevo nombre del cliente: ")
                         datos[0] = dato_modifar
                         print("Su nuevo Nombre completo seria: ", datos[0])
                    elif opcion == 2:
                         dato_modifar = raw_input("Ingrese la nueva direccion del cliente: ")
                         datos[2] = dato_modifar
                         print("Su nuevo Direccion seria: ", datos[2])
                    elif opcion == 3:
                         dato_modifar = raw_input("Ingrese la nueva Localidad de cliente: ")
                         datos[3] = dato_modifar
                         print("Su nueva Localidad seria: ", datos[3])
                    elif opcion == 4:
                         dato_modifar = raw_input("Ingrese el nuevo Codigo Postal del cliente: ")
                         datos[4] = dato_modifar
                         print("Su nuevo Codigo Postal seria: ", datos[4])
                    elif opcion == 5:
                         dato_modifar = raw_input("Ingrese el nuevo Numero de telefono del cliente: ")
                         datos[5] = dato_modifar
                         print("Su nuevo Numero de telefono seria: ", datos[5])
                    elif opcion == 6:
                         dato_modifar = raw_input("Ingrese el nuevo Correo Electronico del cliente: ")
                         datos[6] = dato_modifar
                         print("Su nuevo Correo Electronico seria: ", datos[6])
                         print("\n\tSeleccione el dato a modificar\n\t")
                    print("\n\tSeleccione el dato a modificar\n\t")
                    print("\n\t1.Nombre completo")
                    print("\n\t2.Direccion")
                    print("\n\t3.Localidad")
                    print("\n\t4.Codigo Postal")
                    print("\n\t5.Numero de telefo")
                    print("\n\t6.Correo Electronico")
                    opcion = raw_input("Desea ingresar una nueva modicacion, ingrese el valor correspondiente sino ingrese 0:")   
                    opcion = int(opcion)
                    clientes[id] = datos
     
     if loop == True:
          print("Usuario no encontrado")
          print("Vuelve Ingresar otro usuario")
          modificacion_datos()
     
     saving_changes_to_the_file("clientes.dat", clientes)
     print("\nCliente modificado con éxito!")
     print(clientes)

def activacion_cliente():
     dni_consulta = raw_input("Ingrese DNI del cliente, para ver su Estado: ")
     dni_consulta = int(dni_consulta)
     loop = True
     
     for id,datos in clientes.iteritems():
          if dni_consulta == id and loop == True:
               print("El estado del Clientes es: ")
               if datos[7] == True:
                    print("ACTIVO")
               else:
                    print("INACTIVO")
               
               opcion = raw_input("1.Para cambiar el estado: Activo o Inactivo ")
               opcion = int(opcion)
               while opcion == 1:
                    print("1.Activo o 2.Inactivo")
                    estado = raw_input(": ")
                    estado = int(estado)
                    if estado == 1:
                         datos[7] = True
                    elif estado == 2:
                         datos[7] = False
                    opcion = raw_input("1.Para volver cambiar el estado/ 0 pasa salir. ")
               loop = False
     if loop == True:
          print("Usuario no encontrado")
          print("Vuelve Ingresar otro usuario")
          activacion_cliente()
     
     clientes[id] = datos
     saving_changes_to_the_file("clientes.dat", clientes)
     print("\nCliente modificado con éxito!")
     print(clientes)
     
print(clientes)
activacion_cliente()
