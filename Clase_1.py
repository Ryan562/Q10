def inventario(precio ,cantidad):
    return precio * cantidad

productos = []

cantidad = int(input("Cuantos Productos vas a Comprar? "))

nombre = input("Cual es tu Producto a comprar? ")

producto = {
    "nombre": "Mouse" "Teclado" "monitor",
    "precio": 30000, 60000: 500000,
    "cantidad": cantidad,

}

productos.append(producto)

for producto in productos:
    total= inventario(producto["precio"],producto["cantidad"])

print("===Tu compra===")
print(producto["nombre"])
print("Valor a pagar de ",total)

####################################################################################

monitor = 500000
teclado = 60000
mouse = 40000

productos_1 = {
    "precio": 500000
}

productos_2 = {
    "precio": 60000
}

productos_3 = {
    "precio": 40000
}

cantidad = int(input("Cuantos Productos vas a Comprar? "))

nombre = input("Cual es tu Producto a comprar? ").lower()


print("===Tu compra===")

if nombre == "Mouse":
    total= cantidad * productos_1["precio"]
    print("mouse")
    print(f"Valor a pagar de  ${total:,}")
    
elif nombre == "teclado":
    total= cantidad * productos_2["precio"]
    print("Teclado")
    print(f"Valor a pagar de  ${total:,}")
    
elif nombre =="monitor":
    total= cantidad * productos_3["precio"]
    print("Monitor")
    print(f"Valor a pagar de  ${total:,}")


