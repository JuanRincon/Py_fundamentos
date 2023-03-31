mon = input("Ingrese la moneda que quiera transformar COP o MXN")
val = input("Ingrese el valor  ")
val = int(val)
if mon == "COP":
    val = val * 4050
    val = str(val)
    print("El valor es: " + val)
else:
    mon == "MXN"
    val = val * 202
    val = str(val)
    print("El valor es: " + val)
