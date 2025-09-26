print('+-+-Calculadora deIMC-+-+')  #Titulo
repetir = 'SI' #Inicio la variable para el bucle while
while repetir == 'SI': #mientras while sea SI se repetira el proceso
    nombre = input('Introduzca su nombre: ') #Nombre del Ususario
    peso = float(input('Introduzca su peso en kilogramos: ')) #Peso para el calculo
    altura = float(input('Introduzca su peso en centimetros: '))/100 #Alturo en centimetros mas la divicion para convertir en metros 
    imc = peso/(altura*altura) #Formula para calcular
    if imc >= 0 and imc <= 18.5: #condiciones if elif para determinar la composicion
        composicion = 'Peso inferior al normal'
    elif imc >= 18.5 and imc <= 24.9 :
        composicion = 'Peso normal'
    elif imc >= 25.00 and imc <= 29.9:
        composicion = 'Sobrepeso'
    elif imc >= 40.00:
        composicion = 'Obecidad'

    print('Hola '+ nombre + ' su indice de masa corporal es de: ' + str(imc)) #impreion en pantalla del resultado del imc y el nombre
    print('Usted tiene '+ composicion) # impresion de cual es la composicion

    repetir = input('¿Desea calcular otro vez?SI/NO:') # preguta si desea repetir o no

