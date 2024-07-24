# -*- coding: utf-8 -*-
import pickle
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
     dato = raw_input("\n\tNombre Completo: ")
     listem.append(dato)
     dato = raw_input("\n\tNumero de D.N.I: ")
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tDireccion: ")
     listem.append(dato)
     dato = raw_input("\n\tLocalidad: ")
     listem.append(dato)
     dato = raw_input("\n\tCodigo Postal: ")
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tNumero de Telefono: ")
     dato = int(dato)
     listem.append(dato)
     dato = raw_input("\n\tCorreo Electronico: ")
     listem.append(dato)
     dato = True
     listem.append(dato)
     
    # Generar un ID único para el cliente
     if clientes:
          id_cliente = (clientes.keys(listem[1]))
     else:
          id_cliente = listem[1]
    
     clientes[id_cliente] = listem
    
     saving_changes_to_the_file("clientes.dat", clientes)

ingreso_cliente()