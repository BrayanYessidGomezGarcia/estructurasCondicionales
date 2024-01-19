ladoa= float(input("Ingrese lado A: "))
ladob= float(input("Ingrese lado B: "))
ladoc= float(input("Ingrese lado C: "))

if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa +  ladob:
   if ladoa == ladob and ladob ==ladoc:
      print("El triangulo es equilatero ")

   elif ladoa == ladob or ladob == ladoc or ladoa == ladoc: 
      print("El triangulo es Isoceles ") 
   else: 
    print("El triangulo es Escaleno")
else: 
 print("No es un triangulo valido")