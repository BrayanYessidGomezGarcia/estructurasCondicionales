num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))
num4= int(input("Ingrese el cuarto numero: "))

if num1 > num2 > num3 > num4: 
 print(f"{num1},{num2},{num3}, {num4}")
 
elif num2 > num1 > num3 > num4: 
 print(f"{num2},{num1}, {num3}")
 
elif num3 > num2 > num4 > num1: 
 print(f"{num3},{num2}, {num1}")
 
elif num3 > num4 > num1 > num2: 
 print(f"{num3},{num1}, {num2}")
 
elif num4 > num3 > num2 > num1 > num1: 
 print(f"{num4} {num3},{num2}, {num1}")
 
else: 
 print(f"{num1}, {num2}, {num3} y {num4} son iguales ")