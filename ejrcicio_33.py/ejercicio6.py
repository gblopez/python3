print("bienvenido ingrese su salario".center(50,"*"))

INCREMENTO = 0.8
DESCUENTO = 0.25
sueldo = 0                      
aumento = 0
suma = 0
descuento = 0
total = 0
sueldos = int(input("ingrese su sueldo actual:. "))
aumento = sueldo * INCREMENTO
suma = aumento + sueldo
descuento = suma * DESCUENTO
total = suma - descuento
print("su sueldo es de:. {}".format(total))
              
