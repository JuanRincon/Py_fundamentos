def imprimir_mensaje(mensaje):
    print('hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3): ' ))

if opcion == 1:
    imprimir_mensaje('Elegiste la opción_1')
elif opcion == 2:
    imprimir_mensaje('Elegiste la opción_2')
else:
    imprimir_mensaje('Elegiste la opción_3')
