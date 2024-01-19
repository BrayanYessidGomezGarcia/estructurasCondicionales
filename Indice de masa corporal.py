altura = float(input('Ingrese su altura en cms: '))
peso = float(input('Ingrese su peso en kilos: '))
edad = int(input('Ingrese su edad: '))
IMC = (peso)/((altura/100)**2)

if edad >= 45:
    if IMC >= 22:
        print('Riesgo alto')
    else:
        print('Riesgo medio')
elif 0 < edad < 45:
    if IMC >= 22:
        print('Riesgo medio')
    else:
        print('Riesgo bajo')
else:
    print('Ingrese una edad valida')