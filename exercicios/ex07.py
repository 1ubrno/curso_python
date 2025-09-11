#Calculadora com while

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Dite outro numero: ')
    operador = input('Digite um operador (+-/*): ')

    numeros_valido = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_valido = True
    except:
        numeros_valido = None

    if numeros_valido is None:
        print('Os numeros digitados sao invalidos')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print('Realizando sua conta. Confira o resultado abaixo')
    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
         print(numero_1_float - numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    else:
        print('Nunca deveria chegar aqui')
    

    sair = input('quer sair? [s]').lower().startswith('s')
    if sair is True:
        break
    