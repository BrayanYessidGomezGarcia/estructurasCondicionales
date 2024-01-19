palabra1= input("Ingrese la primera palabra: ")
palabra2= input("Ingrese la segunda palabra: ")

Longitud_palabra1= len(palabra1)
Longitud_palabra2= len(palabra2)

if palabra1 > palabra2:
  diferencia= palabra1 - palabra2
  print(f"La palabra {palabra1} tiene {diferencia} letras mas que {palabra2}")
  
elif palabra1 < palabra2: 
  diferencia= palabra2 - palabra1
  print(f"La palabra {palabra2} tiene {diferencia} letras mas que {palabra2}")
  
else: 
 print(f" La palabra {palabra1} y {palabra2} tienen las mismas letras")


     