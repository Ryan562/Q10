mayores= 0
menores= 0

for i in range(1, 11):
    edad = int(input("Ingrese su edad " + str(i) + ": "))
    
    if edad >= 18:
     mayores= mayores + 1
    else:
     menores = menores + 1
    
print("Usted no parte bocato todavia: ", mayores)
print("Usted parte bocato y esta poderoso: ", menores)