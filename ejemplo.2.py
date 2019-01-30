##calcular la edad actual de una persona, previamente ingresado el año actualy el año actual y el año de nacimiento

print("Bienvenido al programa".center(50,"*"))

FEC_ACT = 2019
fec_nac = int(input("ingres tu año de nacimiento"))

edad = FAC_ACT - fec_nac
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

