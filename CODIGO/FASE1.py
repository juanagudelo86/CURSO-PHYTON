#BY JUAN AGUDELO
#import os
# EJERCICIO FASE 1 
"""Se realizará un proyecto de programación que permita gestionar los datos de los vendedores de la empresa XYZ la cual fue fundada el 23 de junio de 1990, y los
    datos a gestionar por cada empleado son los siguientes:
        Fase 1:        
            La empresa desea administrar los datos de sus empleados, los cuales son: Número de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Género, Estado
            Civil, Número de hijos, Estatura en metros, fecha de nacimiento (Día, mes y año), Sueldo básico y Días Laborados.
            Se desea:
            1. Obtener los datos por teclado para un único empleado (Tener en cuenta el tipo de dato adecuado para cada dato)
            2. Imprimir o mostrar los datos obtenidos por pantalla (mostrar la fecha de nacimiento en un formato de fecha adecuado)
"""
#INICIO 
print ("    \\\\\\\ EMPRESA XYZ ///////")
print ("       REGISTRO DE EMPLEADOS \n")

id= int(input("Digite numero de identificacion empleado : "))
nombre= input("Digite nombre empleado : ")
apellido= input("Digite apellido empleado : ")
direccion= input("Digite direccion empleado : ")
telefono= int(input("Digite telefono del empleado : "))
edad= int(input("Digite edad del empleado : "))
genero= input("Digite genero del empleado M= MASCULINO F= FEMENINO: ")
estado_civ= input("Digite estado civil del empleado : ")
hijos= int(input("Digite nuero de hijos del empleado : "))
estatura=input("Digite estatura en metros del empleado : ")
año_n= int(input("Digite año de nacimiento del empleado: "))   #año de nacimiento
mes_n= int(input("Digite mes de nacimiento del empleado: ")) #mes de nacimiento
dia_n= int(input("Digite dia de nacimiento del empleado: ")) #dia de nacimiento
sueldo= int(input("Digite sueldo del empleado: "))
dias_t= int(input("Digite dias laborados del empleado: "))
print ("    FIN CAPTURA DE DATOS DE EMPLEADOS \n")
#os.system ("cls")  #limpiar pantalla

print ("\t\t\t\\\\\\\ EMPRESA XYZ ///////")
print ("\tDATOS EMPLEADO  \n")

print (f"\tIDENTIFICACION #: {id} ")
print ( "\tNOMBRE COMPLETO : {} {}".format(nombre,apellido))
print (f"\tDIRECCION : {direccion} ")
print (f"\tTELEFONO : {telefono} ")
print (f"\tEDAD : {edad} AÑOS ")
print (f"\tGENERO: {genero} ")
print (f"\tESTADI CIVIL: {estado_civ} ")
print (f"\tNUMERO DE HIJOS: {hijos} ")
print (f"\tESTATURA EN METROS: {estatura} ")
print ( "\tFECHA DE NACIMIENTO: AÑO {}, MES {}, DIA {} ".format(año_n,mes_n,dia_n) + "\n")
print (f"\tSUELDO BASICO: $ {sueldo} ")
print (f"\tDIAS LABORADOS: {dias_t}  \n")
print ("\t\tFIN DEL REPORTE ")