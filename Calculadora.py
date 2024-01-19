N1= int(input("Ingrese numero "))
N2= int(input("Ingrese numero "))
Op= input("Ingrese el operador (suma, resta, multiplicacion, division y exponente) ")   
resultado= 0

if Op == "suma": 
    resultado= N1 + N2 
    print(f" {N1} + {N2} = {resultado}")

elif Op == "multiplicacion": 
    presultado= N1 * N2 
    print(f" {N1} * {N2} = {resultado}")

elif Op == "division": 
    resultado= N1 / N2 
    print(f" {N1} / {N2} = {resultado}")

elif Op == "resta": 
    resultado= N1 - N2 
    print(f" {N1} - {N2} = {resultado}")

elif Op == "exponente": 
    resultado= N1 ** N2 
    print(f" {N1} ** {N2} = {resultado}")

else: 
 print("El resultado no existe ")

