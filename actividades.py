# Q10
Actividades de Combarranquilla

                                            // IA //


num1 = int(input("Numero 1: "))

num2 = int(input("Numero 2: "))

operacion = input("Operacion: (/ * - +) ")

v1 = int(input("Quieres que te muestre el resultado con todas las operaciones ? (1=si / 0=no) "))

if v1 == 1:

    print("El resultado de {num1}{operacion}{num2} es {result}".
          format(num1=num1, operacion=operacion, num2=num2,
                 result=eval(f"{num1}{operacion}{num2}")))

    print("El resultado de {num1}-{num2} es {result}".20
    
          format(num1=num1, num2=num2, result=num1 - num2))

    print("El resultado de {num1}/{num2} es {result}".
          format(num1=num1, num2=num2, result=num1 / num2))

    print("El resultado de {num1}*{num2} es {result}".
          format(num1=num1, num2=num2, result=num1 * num2))

else:

    if operacion == "+":
        result = num1 + num2

    elif operacion == "-":
        result = num1 - num2

    elif operacion == "/":
        result = num1 / num2

    elif operacion == "*":
        result = num1 * num2

    print("El resultado de {num1}{operacion}{num2} es {result}".
          format(num1=num1, operacion=operacion, num2=num2, result=result))


                                            // IA //
    


                                            // IA //


num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
operacion = input("Operacion: (/ * - +) ")

# Guardamos la opción del usuario
v1 = int(input("Quieres que te muestre el resultado con todas las operaciones ? (1=si / 0=no) "))

print("\n--- RESULTADOS ---")

# 1. Siempre muestra la operación que el usuario eligió originalmente
# Usamos eval de forma segura para calcular la operación dinámica
resultado_elegido = eval(f"{num1}{operacion}{num2}")
print(f"El resultado de {num1} {operacion} {num2} es {resultado_elegido}")

# 2. SI EL USUARIO ELIGE 1 (SÍ), se ejecuta este bloque con el resto de operaciones
if v1 == 1:
    print("\n--- Otras operaciones posibles ---")
    print(f"El resultado de {num1} + {num2} es {num1 + num2}")
    print(f"El resultado de {num1} - {num2} es {num1 - num2}")
    print(f"El resultado de {num1} * {num2} es {num1 * num2}")
    
    # Evitamos error de división por cero
    if num2 != 0:
        print(f"El resultado de {num1} / {num2} es {num1 / num2}")
    else:
        print("El resultado de la división es: No se puede dividir entre cero")
        

                                            // IA //






sueldo = int(input("Ingrese su sueldo: "))

p=sueldo * 0.04
s=sueldo * 0.125
caja=sueldo * 0.06
aux= 2490000

he = int(input("cuantas horas extras trabajastes"))

horas_extras = he * 10422

salario = sueldo - p - s - caja + aux + horas_extras
    
print("El salario total es: ", salario)




n1= float(input("Ingrese nota parcial1: "))
nsub1= float(input("Ingrese nota subparcial1: "))

n2= float(input("Ingrese nota parcial2: "))
nsub2= float(input("Ingrese nota subparcial2: "))

n3= float(input("Ingrese nota parcialFinal: "))
nsub3= float(input("Ingrese nota subparcialFinal: "))

n1=n1 * nsub1
n2=n2 * nsub2
n3=n3 * nsub3

nota_final= n1+n2+n3
print("Su nota final es: ",nota_final)



producto=input("Que le gustaria: ")
precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad de productos: "))
total=precio*cantidad
print("El total a pagar es: ", total)




producto=input("Que le gustaria: ")
precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad de productos: "))
total=precio*cantidad
print("El total a pagar es: ", total)


celsius=float(input("Ingrese su temperatura en Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("La temperatura en Fahrenheit es: ", fahrenheit, "°")

fahrenheit=float(input("Ingrese su temperatura en Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("La temperatura en Celsius es: ", celsius, "°")


while True:
    respuesta = input("¿Qué prefieres?\n1) Celsius a Fahrenheit\n2) Fahrenheit a Celsius\nEscribe 1 o 2: ")

    if respuesta == "1":
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("La temperatura en Fahrenheit es:", fahrenheit, "°F")
    elif respuesta == "2":
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("La temperatura en Celsius es:", celsius, "°C")
    else:
        print("Opción no válida")

    seguir = input("¿Quieres hacer otra operación? (s/n): ")
    if seguir != "s":
        print("Bye")
        break




x = int(input("Ingrese un número: "))

if x >= 20:
    print("El numero es mayor que 20")
elif x < 20:
    print("El numero es menor que 20")
else:
    print("El numero es igual a 20")





while True:
    x = int(input("Ingrese un número: "))

    if x > 20:
        print("El numero es mayor que 20")
    elif x < 20:
        print("El numero es menor que 20")
    else:
        print("El numero es igual a 20")

    continuar = input("¿Quieres ingresar otro número? (s/n): ")
    if continuar != "s":
        break




    edad= int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
elif edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")



+
num=int(input("digite un numero: "))

if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
        print("El numero es cero")
