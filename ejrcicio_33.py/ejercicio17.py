suelo = 0
EXTRA = 0.10
venta1 = 0
venta2 = 0
venta3 = 0
sueldo = int(input("ingrese su sueldo base"))
venta1 = int(input("ingrese cantidad de su venta"))
venta2 = int(input("ingrese cantidad de su venta"))
venta3 = int(input("ingrese cantidad de su venta"))
suma = (venta1 + venta2 + venta3) * EXTRA
total = sueldo + suma
print("pago de sus comiciones:{}".format(suma))
print("el total de su sueldo es de:{}".format(total))
