def valor_inventario(precio, cantidad):
    return precio * cantidad


productos = []

cantidad_productos = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad_productos):
    print("\nProducto", i + 1)

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad disponible: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)


print("\n--- INVENTARIO DE LA TIENDA ---")

for producto in productos:
    total = valor_inventario(producto["precio"], producto["cantidad"])

    print("\nProducto:", producto["nombre"])
    print("Precio:", producto["precio"])
    print("Cantidad:", producto["cantidad"])
    print("Valor total del inventario:", total)

    if producto["cantidad"] < 5:
        print("Stock bajo")

######################################################

def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


while True:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Programa terminado.")
        break

    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = sumar(num1, num2)
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = restar(num1, num2)
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print("Resultado:", resultado)

        elif opcion == "4":
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                resultado = dividir(num1, num2)
                print("Resultado:", resultado)

    else:
        print("Opción no válida.")

######################################################

def calcular_total(ventas):
    total = 0

    for venta in ventas:
        total = total + venta["valor"]

    return total


def venta_mayor(ventas):
    mayor = ventas[0]

    for venta in ventas:
        if venta["valor"] > mayor["valor"]:
            mayor = venta

    return mayor


ventas = []

cantidad_ventas = int(input("¿Cuántas ventas desea registrar? "))

for i in range(cantidad_ventas):

    print("\nVenta", i + 1)

    producto = input("Nombre del producto: ")
    valor = float(input("Valor de la venta: "))

    venta = {
        "producto": producto,
        "valor": valor
    }

    ventas.append(venta)


total = calcular_total(ventas)

promedio = total / cantidad_ventas

mayor = venta_mayor(ventas)


print("\n--- RESUMEN DE VENTAS ---")

print("Total vendido:", total)
print("Promedio de ventas:", promedio)

print("Venta de mayor valor:")
print("Producto:", mayor["producto"])
print("Valor:", mayor["valor"])


if total > 500000:
    print("Meta alcanzada")
else:
    print("Meta no alcanzada")

######################################################

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


def clasificar_estudiante(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def registrar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))

    nota1 = float(input("Primera nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Tercera nota: "))

    promedio = calcular_promedio(nota1, nota2, nota3)
    estado = clasificar_estudiante(promedio)

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "promedio": promedio,
        "estado": estado
    }

    estudiantes.append(estudiante)

    print("\nEstudiante registrado correctamente.")


def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")

        for estudiante in estudiantes:
            print("\nNombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Nota 1:", estudiante["nota1"])
            print("Nota 2:", estudiante["nota2"])
            print("Nota 3:", estudiante["nota3"])
            print("Promedio:", estudiante["promedio"])
            print("Estado:", estudiante["estado"])


def buscar_estudiante(estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante: ")

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre_buscar.lower():
            print("\n--- ESTUDIANTE ENCONTRADO ---")
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Nota 1:", estudiante["nota1"])
            print("Nota 2:", estudiante["nota2"])
            print("Nota 3:", estudiante["nota3"])
            print("Promedio:", estudiante["promedio"])
            print("Estado:", estudiante["estado"])

            encontrado = True

    if encontrado == False:
        print("\nEstudiante no encontrado.")


def promedio_general(estudiantes):
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
    else:
        suma = 0

        for estudiante in estudiantes:
            suma = suma + estudiante["promedio"]

        promedio = suma / len(estudiantes)

        print("\nPromedio general:", promedio)


estudiantes = []

while True:

    print("\n--- SISTEMA DE ESTUDIANTES ---")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio general")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante(estudiantes)

    elif opcion == "2":
        mostrar_estudiantes(estudiantes)

    elif opcion == "3":
        buscar_estudiante(estudiantes)

    elif opcion == "4":
        promedio_general(estudiantes)

    elif opcion == "5":
        print("\nPrograma terminado.")
        break

    else:
        print("\nOpción no válida.")

######################################################



######################################################



######################################################
