A= int(input("Juegos ganados por A: "))
B= int(input("Juegos ganados por B: "))

if A == 6 and B < 5:
 print("Gano A")

elif A == 6 and B == 5:
 print("Aun no termina")

elif A == 7 and B <= 6: 
 print("Gano A")

elif B == 7 and A <= 6: 
 print("Gano B")

elif B == 6 and A < 5: 
  print("Gano B")

else: 
  print("Invalido")