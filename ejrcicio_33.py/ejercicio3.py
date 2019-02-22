
print ("bienvenido al internet".center(50,"*"))
print ("la hora tiene un valor de 1.5 Quetzales")

hora = 0
PAGO_POR_HORA = 1.5

hora = int(input("ingrese el numero de horas que solicito el servido de internet"))
if PAGO_POR_HORA  <= 5:
    total = hora * PAGO_POR_HORA
    print("su total a pagar es: ",total)
else:
    total = hora * PAGO_POR_HORA
    print("tienes una hora totalmente gratis")
    
    
