#GERSON ADILSON BOLVITO LOPEZ
#5TO BIPC
#Ejercicio4
#REALIAR EL PROMEDIOP DE N NOTAS UTILIZANDO EL FOR

n = 0
suma = 0
print("Bienvenido al programa:) ". center(50,"*"))
print("Ingrese la notas las notas que ruieras, Ingrese 1 para detener el programa: ")


cantidad = int(input("ingresa la cantidad de notas que pondra: "))
for i in range(cantidad):
      n = int(input("ingrese notas: ."))
      suma = suma + n
promedio = suma / cantidad
print("el promedio es:. {}".format(promedio))
