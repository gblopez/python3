DOLARES_EUROS = 2.150
EUROS_DOLARES = 1.45
CANTIDAD = 0
TOTAL = 0
print("vienvenido al programa".center(50, "-"))
opcion=input("1.dolares a euros 2.euros a dolares a: ")

if opcion == "1":
    dolares = input("cantidad en dolares: ")
    saldo = float(dolares) / DOLARES_EUROS
    print ("la conversion es: ",saldo)
elif opcion == "2":
    euros = input ("cantidad en euros: ")
    saldo = float (euros) / EUROS_DOLARES
    print ("la conversion es: ",saldo)
else:
    print ("opcion no valida")
