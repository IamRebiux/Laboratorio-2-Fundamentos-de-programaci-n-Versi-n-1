costo= float(input("Ingrese el costo de su producto: \n ----->"))
pago= float(input("Ingresse el efectivo con el que pagara: \n ----->"))

while pago < costo:

    if pago > costo:
        vuelto = pago - costo 
        print(f"Su cambio es de: $ {vuelto}")

    elif costo == pago:
        print(f"La cantidad es exacta (No tiene cambio) \n ¡Gracias por su compra!")

    elif costo > pago: 
        costoFaltante = costo - pago
        print(f"Usted debe ${costoFaltante} ¡por favor pagar completo!")
        pagofaltante = int(input())
        pago = pagofaltante + pago

if pago > costo:
        vuelto = pago - costo 
        print(f"Su cambio es de: $ {vuelto}")

if costo == pago:
        print(f"La cantidad es exacta (No tiene cambio) \n ¡Gracias por su compra!")
if costo == pago:
        print(f"La cantidad es exacta (No tiene cambio) \n ¡Gracias por su compra!")
        
print("FIN")
