
destino = input("Introduce el destino del envio: ").lower()
total_orden = float(input("Introduce el total de la orden: "))

if destino in ("españa", "espana"):
	costo_envio = 5, "US"
	
elif destino in ("portugal", "francia", "italia"):
	costo_envio = 13, "US"
	
elif destino in ("alemania", "holanda"):
	costo_envio = 15, "US"
	
else:
	costo_envio = 25, "US"


total_pagar = total_orden + costo_envio[0]

print(f"Costo del envio: ${costo_envio[0]:.2f} {costo_envio[1]}")
print(f"Total a pagar: ${total_pagar:.2f} {costo_envio[1]}")




                                            // Mejorado //

TASA_COP_A_USD = 0.00025  
TASA_EUR_A_USD = 1.08     


destino = input("Introduce el destino del envio: ").lower()
moneda_origen = input("¿En qué moneda vas a pagar? (COP / EUR / USD): ").upper()
total_orden_local = float(input(f"Introduce el total de la orden en {moneda_origen}: "))


if moneda_origen == "COP":
    total_orden_usd = total_orden_local * TASA_COP_A_USD
elif moneda_origen == "EUR":
    total_orden_usd = total_orden_local * TASA_EUR_A_USD
else:
    total_orden_usd = total_orden_local 

if destino in ("españa", "espana"):
	costo_envio = 5, "USD"
elif destino in ("portugal", "francia", "italia"):
	costo_envio = 13, "USD"
elif destino in ("alemania", "holanda"):
	costo_envio = 15, "USD"
elif destino in ("colombia"):
	costo_envio = 3, "USD"
else:
	costo_envio = 25, "USD"

total_pagar_usd = total_orden_usd + costo_envio[0]

print("\n--- RESUMEN DE COMPRA ---")
print(f"Total orden (en USD): ${total_orden_usd:.2f} USD")
print(f"Costo del envio: ${costo_envio[0]:.2f} {costo_envio[1]}")
print(f"Tu envio hacia {destino}: ${total_pagar_usd:.2f} USD", )


                                            // Mejorado //

