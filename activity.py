x= int(float(input("digite su primera nota: ")))
y= int(float(input("digite su segunda nota: ")))
z= int(float(input("digite su tercera nota: ")))

prm= x+y+z/3

if prm <= 2.9:
    print("no aplicas beca")
    
elif prm >= 39:
    print("tu promedio es aceptable")
    
elif prm <= 4:
    print("tu promedio es bueno")
    
elif prm >= 4.5:
    print("Becado")
    
else:
    print("Becado")
    
