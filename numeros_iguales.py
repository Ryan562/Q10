numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
numero3 = float(input("Introduce el tercer numero: "))

if numero1 == numero2 == numero3:
	print("Los 3 numeros son iguales.")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
	print("Hay 2 numeros iguales.")
else:
	print("Los 3 numeros son distintos.")
