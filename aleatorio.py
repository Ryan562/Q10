import random
numero_secreto = random.randint(-11,11)

while numero_secreto == 0:
    numero_secreto = random.randint(-11,11)
    
numero_usuario = int(input("Adivina el numero: "))
print("Nada, casi, Sigue Intentando")
int(input("Adivina el numero: "))

print("Por fin, Acertaste!!")
print("Gracias por utilizar el programa")



import random
numero_secreto= random.randint(1,11)

while True:
    numero= int(input("Digite su numero: "))
    
    if numero < numero_secreto:
        print("el numero es mayor")
        
    elif numero > numero_secreto:
        print("el numero es menor")
        
    else:
        print("Adivinaste")
        break