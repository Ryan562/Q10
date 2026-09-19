menor = None
# (None) es como una variable vacia que espera su asignacion#

for i in range(1, 6):
    numero = float(input("Ingrese el número " + str(i) + ": "))

    if menor is None or numero < menor:
        menor = numero

    # aqui en el if al momento de la persona colocar
    # sus numero compara los numero colocandolos en variable
    # vacia y dando vueltas con los rangos a ver cual es el
    # numero menor final para imprimirlo

print("El número menor es:", menor)
