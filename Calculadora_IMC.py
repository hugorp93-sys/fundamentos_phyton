print('+-+-Calculadora deIMC-+-+')
repetir = 'SI'
while repetir == 'SI':
    nombre = input('Introduzca su nombre: ')
    peso = float(input('Introduzca su peso en kilogramos: '))
    altura = float(input('Introduzca su peso en centimetros: '))/100
    imc = peso/(altura*altura)
    if imc >= 0 and imc <= 18.5:
        composicion = 'Peso inferior al normal'
    elif imc >= 18.5 and imc <= 24.9 :
        composicion = 'Peso normal'
    elif imc >= 25.00 and imc <= 29.9:
        composicion = 'Sobrepeso'
    elif imc >= 40.00:
        composicion = 'Obecidad'

    print('Hola '+ nombre + ' su indice de masa corporal es de: ' + str(imc))
    print('Usted tiene '+ composicion)

    repetir = input('¿Desea calcular otro vez?SI/NO:')
