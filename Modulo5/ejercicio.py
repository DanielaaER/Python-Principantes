# LOGICA BOOLEANA

#Para expresar la lógica condicional en Python, 
# se usan instrucciones if. Al escribir una instrucción if, 
# se basa en otro concepto que se describe en este módulo, 
# el de los operadores matemáticos. Python admite los operadores
# lógicos comunes de matemáticas: igual, no igual, menor que, 
# menor o igual que, mayor que y mayor o igual que. 
# 
# Probablemente esté acostumbrado a ver que estos operadores 
# se muestran mediante símbolos, que también es la forma en que 
# se representan en Python.

#   Es igual que: a == b
#   No es igual a: a != b
#   Menor que: a < b
#   Menor o igual que: a <= b
#   Mayor que: a > b
#   Mayor o igual que: a >= b


a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)


#Escritura de instrucciones if
#Use una instrucción if si quiere ejecutar código solo si se 
# cumple una condición concreta. La sintaxis de una instrucción 
# if siempre es la siguiente:

a = 93
b = 27
if a >= b:
    print(a)

#En Python, se debe aplicar sangría al cuerpo de una instrucción 
# if. Siempre se ejecutará cualquier código que siga a una 
# expresión de prueba que no tenga sangría:
a = 24
b = 44
if a <= 0:
    print(a)
print(b)

#Salida: 44

#En este ejemplo, la salida es 44 ya que la expresión de prueba 
# es False y la instrucción print(b) no tiene sangría en el 
# mismo nivel que la instrucción if.