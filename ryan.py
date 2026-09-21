# - Cantidad de positivos
# - Cantidad de negativos
# - Suma total
# - Promedio

positivos = 0
negativos = 0
suma_total = 0

for i in range(1, 11):
    numero = float(input(f"Ingrese el número {i}: "))
    suma_total += numero

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

promedio = suma_total / 10

print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")