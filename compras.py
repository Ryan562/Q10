valor=float(input("cual es el valor de tu compra? "))

if valor < 100000:
    print("tu compra no contiene descuento")
    
elif valor <= 199999:
    descuento = valor*0.05
    total1= valor-descuento
    print("El valor de tu compra es", total1 ,"con el 5% de descuento")
    
elif valor >= 200000:
    descuento = valor*0.10
    total2= valor-descuento
    print("El valor de tu compra es", total2, "con el 10% de descuento")
else:
    total = valor