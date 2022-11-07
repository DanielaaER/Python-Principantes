# program.py
sum = 1 + 2
print(sum)


# FUNCION PRINT
#la funcion print sirve para mostrar un dato en consola
#la ocnsola es una palicacion de linea de comandos ue permite
#interactuar con el sistema operativoo


#para usar print debemos asignar un argumento
print("show this in the console")



#VARIABLESS
sum = 1 + 2 # 3
product = sum * 2
print(product)

#Tipos de datosss
#Una variable asume un tipo de dato, en el programa anteriori, sum 
#obtiene el tipo int, sin embargo hay mas tipos de datos

# Numericos : int, float, no=3
# Texto     : str = " a literal string"
# Boolean   : continue = true;


#Fragmento de codigo que muestra los tipos anteriores

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string


#Para saber el tipo de dato se usa la funcion type

distance_to_alpha_centauri = 4.367 # looks like a float
type(distance_to_alpha_centauri) ## <class 'float'>
print(type(distance_to_alpha_centauri))



#OPERADOREESS
# Los operadores nos permiten realizar varias operaciones en
#  las variables siguiendo la estructura:
# <left side> <operator> <right side>

left_side = 10
right_side = 5
left_side / right_side # 2

# Operadores aritmeticos
#   +    suma
#   -    resta  
#   /    division 
#   *    multiplicacion


# Operadores de asignacion
#   =   asigna el valor 
#   +=  incrementa
#   -=  reduce
#   /=  dividido por
#   */  multiplicado por




# FECHAAS
# Para trabajar con fechas debemor importar el moduloo date
from datetime import date

#podemos llamar la funcion con today()
date.today()

print(date.today())


#CONVERSION DE TIPO DE DATOS

# si ejecutamos

#print("Today's date is: " + date.today())

#obtenemos un errror debido a que dat.today() nos devuelve un 
# valor de tipo fecha y no string, por ello lo convertimos 
# usando la funcion str()
print("Today's date is: " + str(date.today()))