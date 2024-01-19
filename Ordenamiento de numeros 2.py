num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))

if num1 > num2 > num3: 
 print(f"{num1},{num2},{num3}")
 
elif num1 < num2 > num3: 
 print(f"{num2},{num1}, {num3}")
 
elif num3 > num2 > num1: 
 print(f"{num3},{num2}, {num1}")
 
elif num3 > num1 > num2: 
 print(f"{num3},{num1}, {num2}")
 
else: 
 print(f"{num1}, {num2} y {num3} son iguales ")