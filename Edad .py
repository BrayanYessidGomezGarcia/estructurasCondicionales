from time import localtime
t= localtime () 
t.tm_mday 
18
t.tm_mon 
1
t. tm_year 
2024

diact= t.tm_mday 
mesact= t.tm_mon 
añoact= t.tm_year

print("ingrese su fecha de nacimiento: ")
Dia= int(input("Dia: "))
Mes= int(input("Mes: "))
Año= int(input("Año: "))

fecha= añoact - Año 

if mesact < Mes or (mesact == Mes and diact < Dia):
  print(f"Usted tiene {fecha -1}" )
