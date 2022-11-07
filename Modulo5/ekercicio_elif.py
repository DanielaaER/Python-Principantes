#En Python, la palabra clave elif es la abreviatura de else if. 
# El uso de instrucciones elif permite agregar varias 
# expresiones de prueba al programa. Estas instrucciones se 
# ejecutan en el orden en que se escriben, por lo que el 
# programa escribirá una instrucción elif solo si la primera 
# instrucción if es False. Por ejemplo:

a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#La instrucción elif de este bloque de código no se ejecutará, 
# porque la instrucción if es True.

#La sintaxis de una instrucción if/elif siempre es la siguiente:

#if test_expression:
    # statement(s) to be run
#elif test_expression:
    # statement(s) to be run

