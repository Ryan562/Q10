p= int(float(input("cual es tu peso: ")))
e= int(float(input("cual es tu estatura: ")))

imc= p*p
imc2= imc/p

if imc2 < 18.5:
    print("!!Te encuentras bajo de peso!!")
    
elif imc2 <= 24.9:
    print("Te encuentras en un peso normal")
    
elif imc2 <= 29.9:
    print("!!Te encuentras en sobrepeso!!")
    
elif imc2 >= 30:
    print("!!Estas Obeso (Peligro)!!")
    
else:
    print("!!Estas Obeso (Peligro)!!")
    
