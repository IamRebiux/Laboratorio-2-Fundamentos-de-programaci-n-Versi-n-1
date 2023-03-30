print("A continuacion se le pediran 3 numeros a evaluar \n")

#Datos ingresados por el usuario
num1 = int(input("Ingrese el valor de su primer numero \n ----->"))
num2 = int(input("Ingrese el valor de su segundo numero \n ----->"))
num3 = int(input("Ingrese el valor de su tercer numero \n ----->"))

print(f"Los numero ingresado son {num1}, {num2}, {num3}")

#Evaluacion de numero mayor
if num1 > num2:
    if num1 > num3:
        print(f"El numero mas grande ingresado es {num1}")
if num2 > num1:
    if num2 > num3:
        print(f"El numero mas grande ingresado es {num2}")
if num3 > num1:
    if num3 > num2:
        print(f"El numero mas grande ingresado es {num3}")

#Evaluacion de numero menor
if num1 < num2:
    if num1 < num3:
        print(f"El numero inferior ingresado es {num1}")
if num2 < num1:
    if num2 < num3:
        print(f"El numero inferior ingresado es {num2}")
if num3 < num1:
    if num3 < num2:
        print(f"El numero inferior ingresado es {num3}")
    

#Evaluacion del numero mediano
if num1 > num2:
    if num1 < num3:
        print(f"El numero de en medio ingresado es {num1}")
if num2 > num1:
    if num2 < num3:
        print(f"El numero de en medio ingresado es {num2}")
    else:
        print("")
if num3 > num1:
    if num3 < num2:
        print(f"El numero de en medio ingresado es {num3}")
    else:
        print("")

print("Fin")
