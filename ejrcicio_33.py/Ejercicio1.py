
print("CANTITAD DE INTERES A PAGAR".center(50, "*"))

PRESTAMOS = 10.000
Años_a_pagar = 0
tasa_de_interes = 0.27


Años_a_pagar = int(input("ingrese los años a pagar: "))
if PRESTAMOS == 10.000:
    Interes = (10.000 * Años_a_pagar)
    aumento = Interes / tasa_de_interes
    print("el interes a pagar es de:",aumento)
