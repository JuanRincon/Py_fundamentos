"""En este código es puesto a modo de comentario código que se
repite de diferentes maneras para llevar a ejecutar la misma
acción, són diferentes formas y ejemplos desde antes de aplicar
la función, y varias alternativas, unas más eficientes que otras
para ejecutar una función de la misma aplicación"""


# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

"""La siguiente secuencia de código es muy interesante, porque
permite preguntar (Elige una opción) antes de (Elegiste una opción)
sin necesidad de haberla puesto antes, además que permite imprimir
exactamente el imput que puso el usuario, optimizando gran cantidad
de líneas en el algorítmo"""
# def imprimir_mensaje():
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opción ' + str(input('Elige una opción (1, 2, 3 )  ')))
#     print('Adios')
    # imprimir_mensaje()

"""Acá tenemos otros ejemplos, donde acomodamos a condicionales
la función planteada, para este primer caso, ingresando el 
parametro (mensaje)"""

def imprimir_mensaje(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3 )  '))
if opcion == 1:
    imprimir_mensaje('Elige una opción 1')
elif opcion == 2:
    imprimir_mensaje('Elige una opción 2')
elif opcion == 3:
    imprimir_mensaje('Elige una opción 3')
else:
    print('Escribe la opción correcta')

"""En las siguientes líneas podemos observar similitud al
anterior pero se optimizan líneas sumando a (Elegiste la opción) 
la variable (opción) como str(string), de esta manera no
habría que escribir cada una de la opciones como parametro"""

# def imprimir_mensaje():
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opción ' + str(opcion))
#     print('Adios')

# opcion = int(input('Elige una opción (1, 2, 3 )  '))
# if opcion == 1:
#     imprimir_mensaje()
# elif opcion == 2:
#     imprimir_mensaje()
# elif opcion == 3:
#     imprimir_mensaje()
# else:
#     print('Escribe la opción correcta')

"""Por último acá podemos ver la forma original
donde gastamos más líneas de código sin usar ningúna función"""

# opcion = int(input('Elige una opción (1, 2, 3 )  '))
# if opcion == 1:
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opción 1')
#     print('Adios')
# elif opcion == 2:
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opción 2')
#     print('Adios')
# elif opcion == 3:
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opción 3')
#     print('Adios')
# else:
#     print('Escribe la opción correcta')

