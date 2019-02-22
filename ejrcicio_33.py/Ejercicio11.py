print("bienvenido al programa".center(50,"*"))


HORAS = 3600
INUTOS = 60
SEGUNDOS = 0.25
menu = int(input("1.tiempo en horas 2.tiempo en minutos 3.tiempo en segundos"))
if menu == 1:
      horas = int(input("ingrese cuantas horas necesita"))
      tiempo = horas * HORAS
      total = tiempo * SEGUNDOS
      print("el total a pagar por el tiempo es de:{}".format(total))
elif menu == 2:
      minutos = int(input("ingrese cuantas minutos necesita"))    
      tiempo = minutos * MINUTOS
      total = tiempo * SEGUNDOS
      print("el total a pagar por el tiempo es de:{}".format(total))
if menu == 3:
      segudnos = int(input("ingrese cuantos segudnos necesita"))
      total = segundos * SEGUNDOS
      print("el total a pagar por el tiempo es de:{}".format(total))
