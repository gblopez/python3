#GERSON ADILSON BOLVITO LOPEZ 5TO BIPC
#Ejercicio 3
#REALISAR EL PROMEDIO DE 5  NOTAS UTILIZANDO EL SICLO FOR
print("bienvenidos al programa".center(50,"*"))
suma = 0
for i in range (5):
      nota = int(input("ingrese nota: "))
      suma = suma + nota
      promedio = suma / 5
print("el promedio es {}".format(promedio))
