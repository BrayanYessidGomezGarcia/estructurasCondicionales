caracter= input("Ingrese caracter: ")

if caracter.isdigit():
 print(f"{caracter} Es numero")
 
elif caracter.isupper():
 print(f"{caracter} Es letra mayuscula")
 
elif caracter.isalpha():
 print(f"{caracter} Es letra minuscula")
 
else: 
 print("No es letra ni numero")