# -*- coding: utf-8 -*-

#  Función que valida, que el valor ingresado sea entero
def validate_integer(opcion):
    loop = True
    while loop:
        try:
            opcion = int(opcion)
            loop = False
        except ValueError:
            print ("\n\n\tERROR. Debe ingresar sólo valores ENTEROS.")
            opcion = raw_input("\n\n\t\tIngrese nuevamente una opción: ")
            loop = True
    return opcion

#  Función que valida, que el valor ingresado sea strings
def validating_strings(dato):
    loop = True
    while loop:
        try:
            dato = str(dato) 
            loop = False
        except ValueError:
            print ("\n\n\tERROR. Debe ingresar sólo CARACTERES correspondientes.")
            dato = raw_input("\n\n\t\tIngrese nuevamente el dato solicitado: ")
            loop = True
    return dato  


#  Función que valida, que el valor ingresado pertenezca a un rango de valores que estará determinado por las variables start y end
def validate_range(opcion, start, end):
    while opcion < start or opcion > end:
        print ("\n\n\tERROR. Debe ingresar sólo valores VÁLIDOS.")
        print ("\n\n\tLos valores deben estar comprendidos entre", start, "y", end, "para considerarse una opción válida.")
        opcion = raw_input("\n\n\t\tIngrese nuevamente una opción: ")
        opcion = validate_integer(opcion)
    return opcion


# Función que valida, que el valor ingresado pertenezca a un rango de limite de digitos
def validate_length_int(dato, limit):
    while not (limit <= len(str(dato)) and len(str(dato)) <= limit):
        print("\n\n\tERROR. Debe ingresar sólo valores VÁLIDOS.")
        print("\n\n\tLos valores deben estar comprendidos entre  el rango de "+ str(limit) + " Digitos.")
        dato = raw_input("\n\n\t\tIngrese nuevamente el dato solicitado: ")
        dato = validate_integer(dato)
    return dato

#  Función que valida la existencia de un archivo
def validating_existence_file(file_name):
    try:
        object_type_file = open(file_name, "r+")
    except IOError:
        object_type_file = open(file_name, "w+")
    object_type_file.close()