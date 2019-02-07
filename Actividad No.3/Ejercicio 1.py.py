#GERSON ADILSON BOLVITO LOPEZ 5TO BIPC

#1ER EJERCICIO

#SOLiCITAR AL USUARIO QUE SELECCIONE UNA OPCION
#OPCION 1 SOLICITAR 2 NUMEROS Y ELEBAR EL PRIMER NUMERO AL SEGUNDO
#OPCION 2 SOLICITAR 3 NUMEROS Y ELEVAR POR EL PRIMERO AL SEGUNDO Y EL RESULTADO Y ELEVARLO AL TERCERO

elevacion = 0
print("bienvenido al promgrama".center(50,"-"))
opcion=input("1.elevar dos numeros el primero por el segundo 2.elevar 3 numeros y elevar el primero por el segundo: ")

if opcion == "1":
    V1 = int(input("ingrese un valor: "))
    V2 = int(input("ingrese un valor: "))
    elevacion = V1 ** V2
    print ("la elevacion es {}".format(elevacion))
elif opcion == "2":
    V1 = int(input("ingrese un valor: "))
    V2 = int(input("ingrese un valor: "))
    V3 = int(input("ingrese un valor: "))
    elevacion = (V1 ** V2) ** V3 
    print ("la elevacion es {}".format(elevacion))
else:
    print("opcion invalida")
    
