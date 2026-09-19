suma = 0

for i in range(1, 6):
    numero = float(input("Ingrese el número " + str(i) + ": "))
    suma = suma + numero

promedio = suma / 5

print("El promedio es:", promedio)
