URGENCIA = 0.37
PEDIATRIA = 0.42
TRAUMATOLOGIA = 0.21
print("desea calcular presupuesto")
salida = input("ingresar presupuesto 1-si \n 2-no")
while salida != 2:
    presupuesto = int(input("ingresar el cantidad"))
    print("la cantidad en Urgencia es:. {}".format(presupuesto * URGENCIA))
    print("la cantidad en Pediatria es:. {}".format(presupuesto * PEDIATRIA))
    print("la cantidad en Traumatologia es:. {}".format(presupuesto * TRAUMATOLOGIA))
    salida = input("ingresar presupuesto 1-si \ 2-no")

