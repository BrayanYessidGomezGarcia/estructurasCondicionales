dividendo=int(input("Ingrese el numero dividendo: "))
divisor= int(input("Ingrese el numero divisor: "))
resultado= dividendo / divisor
resto= dividendo % divisor 

if resto ==0:
    print("La division es exacta")

else: 
    print("La division no es exacta ")

print(f"el resultado es {resultado}")
print(f"El resto es {resto}")

