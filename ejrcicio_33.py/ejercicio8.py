monedas1 = 0
monedas2 = 0
monedas3 = 0
monedas4 = 0
monedas5 = 0
monedas6 = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total = 0

monedas1 =int(input("ingrese monedas de 5:."))
total1 = monedas1 * 0.05
monedas2 =int(input("ingrese monedas de 10:."))
total2 = monedas2 * 0.10
monedas3 =int(input("ingrese monedas de 12,5:."))
total3 = monedas3 * 0.125
monedas4 =int(input("ingrese monedas de 25:."))
total4 = monedas4 * 0.25
monedas5 =int(input("ingrese monedas de 50:."))
total5 = monedas5 * 0.50
monedas6 =int(input("ingrese monedas de 1 Bolivar:."))
total6 = monedas6 * 1

total = total1 + total2 + total3 + total4 + total5 + total6
print("La cantidad total de dinero que se tiene es de: ".format(total))
