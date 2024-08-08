# -*- coding: utf-8 -*-

# ---------------------------Modulos Importados---------------------------
import sys
sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *
# ------------------------------------------------------------------------
# Diccionario global para almacenar los clientes
validating_existence_file("clientes.dat")
clientes = loading_file_into_memory("clientes.dat")

# ---------------------------Fun. Agregar Cliente---------------------------
def ingreso_cliente():
    # --[Ingreso de datos]--
     listem = []
     documento_existe = False
     print("\nSistema de Facturacio del Supermercado.\n\nMenu Agregar nuevo cliente.")
     nro_documento = raw_input("\n\tIngrese el numero de D.N.I a agregar: ")              # P. N° 1 
     nro_documento = validate_length_int(nro_documento, 8)
     nro_documento = validate_integer(nro_documento)
     # --[Verifiacion de cliente existente]--
     for id in clientes.keys():
          if nro_documento == id:
               documento_existe = True
     # --[Ingreso de datos]--       
     if documento_existe == False:     
          nombre = raw_input("\n\tNombre Completo: ").title()       # P. N° 0
          dirrecion = raw_input("\n\tDireccion: ").capitalize()     # P. N° 2   
          localidad = raw_input("\n\tLocalidad: ").capitalize()     # P. N° 3
          cod_postal = raw_input("\n\tCodigo Postal: ")             # P. N° 4
          cod_postal = validate_integer(cod_postal)
          nro_tell = raw_input("\n\tNumero de Telefono: ")          # P. N° 5
          nro_tell = validate_length_int(nro_tell, 10)
          email = raw_input("\n\tCorreo Electronico: ")             # P. N° 6
          # --[Guardado de datos]--
          listem.append(nombre)
          listem.append(nro_documento)
          listem.append(dirrecion)
          listem.append(localidad)
          listem.append(cod_postal)
          listem.append(nro_tell)
          listem.append(email)
          listem.append(True)
          # --[Agregar el cliente al diccionario]--
          clientes[nro_documento] = listem
          saving_changes_to_the_file("clientes.dat", clientes)
          print("\nCliente agregado con éxito!")
     # --[Control de NO usuario existente]--
     if documento_existe == True:
          print("\nEl usuario con el DNI: , " + str(nro_documento) + ". Esta ya registado.")
          print("\nSeleccione una opcion:")
          print("\n1.Visualizar el estado del usuario.")
          print("\n2.Consultar los datos del DNI.")
          print("\n3.Ingresar otro usuario nuevo.")
          print("\n4.Volver al menu principal.")
          opcion = raw_input(": ")
          opcion = validate_integer(opcion)
          opcion = validate_range(opcion, 1, 4)
          if opcion == 1:
               activacion_cliente()
          elif opcion == 2:
               consulta_cliente()
          elif opcion == 3:
               ingreso_cliente()
          elif opcion == 4:
               #importar modulo
               print("salio con exito")
# ------------------------------------------------------------------------
# ---------------------------Fun. Cons. Cliente---------------------------
def consulta_cliente():
     # --[Ingreso de datos]--
     documento_existe = False
     print("\nSistema de Facturacio del Supermercado.\n\nMenu Agregar nuevo cliente.")
     nro_documento = raw_input("\n\tIngrese el numero de D.N.I a consultar: ")             # P. N° 1 
     nro_documento = validate_length_int(nro_documento, 8)
     nro_documento = validate_integer(nro_documento)
     # --[Verifiacion de cliente existente]--        
     for id, datos in clientes.iteritems():
          if nro_documento == id:
               # --[Imprime los datos buscados e existentes]-- 
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
               documento_existe = True
     # --[Control de NO usuario existente]--
     if documento_existe == False:
          print("Usuario NO encontrado")
          print("\nSeleccione una opcion:")
          print("\n1.Visualizar el datos de otro cliente.")
          print("\n2.Ingresar el nuevo Cliente.")
          print("\n3.Volver al menu principal.")
          opcion = raw_input(": ")
          opcion = validate_range(opcion, 1, 3)
          if opcion == 1:
               consulta_cliente()
          elif opcion == 2:
               ingreso_cliente()
          elif opcion == 3:
               #importar modulo
               print("salio con exito")
# ------------------------------------------------------------------------
# ---------------------------Fun. Modi. Cliente---------------------------
def modificacion_datos():
    # --[Ingreso de datos]--
     documento_existe = False
     print("\nSistema de Facturacio del Supermercado.\n\nMenu Agregar nuevo cliente.")
     nro_documento = raw_input("\n\tIngrese el numero de D.N.I a consultar: ")             # P. N° 1 
     nro_documento = validate_length_int(nro_documento, 8)
     nro_documento = validate_integer(nro_documento)
     # --[Verifiacion de cliente existente]--     
     for id,datos in clientes.iteritems():
          if nro_documento == id:
               # --[Imprime los datos buscados e existentes]--
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
               documento_existe = True
               print("\n\tSeleccione el dato a modificar\n\t")
               print("\n\t1.Nombre completo")
               print("\n\t2.Direccion")
               print("\n\t3.Localidad")
               print("\n\t4.Codigo Postal")
               print("\n\t5.Numero de telefono")
               print("\n\t6.Correo Electronico")
               print("\n\t7.Volver al Menu Principal.")
               opcion = raw_input(": ")
               opcion = validate_integer(opcion)
               opcion = validate_range(opcion, 1, 7)
               while opcion != 7:
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
                         datos[4] = validate_integer(dato_modifar)
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
                    print("\n\t1.Nombre completo")
                    print("\n\t2.Direccion")
                    print("\n\t3.Localidad")
                    print("\n\t4.Codigo Postal")
                    print("\n\t5.Numero de telefo")
                    print("\n\t6.Correo Electronico")
                    print("\n\t7.Volver al Menu Principal.")
                    opcion = raw_input(": ")
                    opcion = validate_integer(opcion)
                    opcion = validate_range(opcion, 1, 7)

     # --[Control de NO usuario existente]--
     if documento_existe == False:
          print("\nEl usuario con el DNI: , " + str(nro_documento) + ". No esta registado.")
          print("\nSeleccione una opcion:")
          print("\n1.Visualizar el estado del usuario.")
          print("\n2.Consultar los datos del DNI.")
          print("\n3.Ingresar otro usuario nuevo.")
          print("\n4.Volver al menu principal.")
          opcion = raw_input("\n: ")
          opcion = validate_range(opcion, 1, 4)
          opcion = validate_integer(opcion)
          if opcion == 1:
               activacion_cliente()
          elif opcion == 2:
               consulta_cliente()
          elif opcion == 3:
               ingreso_cliente()
          elif opcion == 4:
               #[Importar Modulo]
               print("salio con exito")
     # --[Guardo de datos modificados]--
     if documento_existe == True:
          clientes[id] = datos
          saving_changes_to_the_file("clientes.dat", clientes)
          print("\nCliente modificado con éxito!")
# ------------------------------------------------------------------------
# ---------------------------Fun. Acti. Cliente---------------------------
def activacion_cliente():
    # --[Ingreso de datos]--
     documento_existe = False
     print("\nSistema de Facturacio del Supermercado.\n\nMenu Agregar nuevo cliente.")
     nro_documento = raw_input("\n\tIngrese el numero de D.N.I a consultar: ")             # P. N° 1 
     nro_documento = validate_length_int(nro_documento, 8)
     nro_documento = validate_integer(nro_documento)
     # --[Verifiacion de cliente existente]--
     for id,datos in clientes.iteritems():
          if nro_documento == id:
               documento_existe = True
               print("\nCliente encontrado para el DNI: ", nro_documento)
               print("\n")
               if datos[7] == True:
                    print("su estado actual es ACTIVO")
               else:
                    print("su estado actual es INACTIVO")
               print("1.Para cambiar el estado: Activo o Inactivo.")
               print("2.Para conservar el estado actual.")
               opcion = raw_input(": ")
               opcion = validate_integer(opcion)
               opcion = validate_range(opcion, 1, 2)
               if opcion == 1:
                    if datos[7] == True:
                         datos[7] = False
                         print("Su nuevo estado para el producto es INACTIVO")
                    else:
                         datos[7] = True
                         print("Su nuevo estado para el producto ES ACTIVO")
               elif opcion == 2:
                    print("Su estado no se modificara")
               
     # --[Control de NO usuario existente]--
     if documento_existe == False:
          print("Usuario no encontrado")
          print("Vuelve Ingresar otro usuario")
          activacion_cliente()
     
     # --[Guardo de datos modificados]--
     if documento_existe == True:
          clientes[id] = datos
          saving_changes_to_the_file("clientes.dat", clientes)
          print("\nCliente modificado con éxito!")
          print(clientes)
# ------------------------------------------------------------------------     
print(clientes)
modificacion_datos()
