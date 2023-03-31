# menu = """Bienvenido al conversor de monedas 💲

# 1 - Pesos colombianos
# 2 - Pesos argentions
# 3 - Pesos mexicanos

# Elige una opción:  """

# opcion = int(input(menu))

# if opcion == 1:
#     pesos = input("¿cuántos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 2875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares,2)               //el comando round sirve para redondear decimales a la cantidad que le especifiquemos       
#     dolares = str(dolares)                    
#     print("Tienes $" + dolares + " dólares")    
# elif opcion == 2:
#     pesos = input("¿cuántos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 64
#     dolares = pesos / valor_dolar
#     dolares = round(dolares)
#     dolares = str(dolares)   
#     print("Tienes $" + dolares + " dólares") 
# elif opcion == 3:
#     pesos = input("¿cuántos pesos mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos / valor_dolar
#     dolares = round(dolares)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dólares") 
# else:
#     print("Ingresa una opción correcta por favor")    

def conversor(nacionalidad, valor_dolar):

    pesos = input("¿cuántos pesos " + nacionalidad + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / int(valor_dolar)
    dolares = round(dolares)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares") 

menu = """Bienvenido al conversor de monedas 💲

1 - Pesos colombianos
2 - Pesos argentions
3 - Pesos mexicanos

Elige una opción:  """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", "2875") 
elif opcion == 2:
    conversor("argentinos", "64") 
elif opcion == 3:
    conversor("mexicanos", "24")
else:
    print("Ingresa una opción correcta por favor") 
 




