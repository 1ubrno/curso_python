#exercicio de if elif else

primeiro_valor = input('Digite um valor: ')
segundo_valor =  input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor} eh maior que {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'O valor {primeiro_valor} eh igual {segundo_valor}')
else:
    print(f'O {primeiro_valor} eh menor que o {segundo_valor}')