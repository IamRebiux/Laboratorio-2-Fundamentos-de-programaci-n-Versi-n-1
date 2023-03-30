#Suma de cantidades igresadas y vuelto de pago ingresado

#Datos pedidos al usuario
costo= float(input("\nIngrese el costo de su producto: \n ----->"))
pago= float(input("Ingresse el efectivo con el que pagara: \n ----->"))

#Evaluacion del efectivo pagado
while pago < costo: 
    costoFaltante = costo - pago
    print(f"Usted debe ${costoFaltante.round} ¡por favor pagar completo!").
    pagofaltante = float(input("Ingrese el pago Restante \n --> "))
    pago += pagofaltante

if pago > costo:
        vuelto = pago - costo 
        print(f"Su cambio es de: $ {vuelto}\n")

if costo == pago:
        print(f"La cantidad es exacta (No tiene cambio) \n ¡Gracias por su compra!\n")
        
print("FIN")
