def boff(n1, n2): #se pueden guardar varios variables dentro de los ()
    return 'La suma es de', n1+n2


n1= int(input("Digita el primer numero: "))
n2= int(input("Digita el segundo numero: "))
igual=boff(n1,n2)

print(igual)

############################################################################

def boff(m1, m2): #se pueden guardar varios variables dentro de los ()
    return "Tu resultado es" , m1*m2

print("====Calculadora====")
n1= int(input("Digita su primer numero: "))
n2= int(input("Digite su segundo numero: "))
igual=boff(m1,m2)

return "Tu resultado es" , d1/d2

n1= int(input("Digita su primer numero: "))
n2= int(input("Digite su segundo numero: "))
igual=boff(d1,d2)

print(igual)

############################################################################

def boff(n1, n2, operacion):
    if operacion == "+":
        resultado = n1 + n2
    elif operacion == "-":
        resultado = n1 - n2
    elif operacion == "*":
        resultado = n1 * n2
    elif operacion == "/":
        if n2 == 0:
            return "No se puede dividir entre 0"
        resultado = n1 / n2
    else:
        return "Operación no válida"

    return "Tu resultado es:", resultado


print("==== Calculadora ====")

operacion = input("Operación: (/ * - +): ")
n1 = int(input("Digita tu primer número: "))
n2 = int(input("Digita tu segundo número: "))

igual = boff(n1, n2, operacion)

print(igual)

############################################################################

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


cantidad = int(input("¿Cuántos estudiantes se van a registrar? "))

estudiantes = []

for i in range(cantidad):

    nombre = input("Nombre del estudiante: ")

    nota1 = float(input("Primera nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Tercera nota: "))

    promedio = calcular_promedio(nota1, nota2, nota3)

    if promedio >= 3.0:
        print("==========================")
        print("APROBADO")
        print("==========================")
    else:
        print("==========================")
        print("REPROBADO")
        print("==========================")

    
    estudiantes.append([nombre, promedio])

print("Estudiantes registrados:")

for estudiante in estudiantes:
    print(estudiante[0], estudiante[1])
    print("==========================")

############################################################################