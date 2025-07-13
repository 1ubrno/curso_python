#Exercicio
# peca para o usuario digitar o seu nome
# peca para o usuario digitar sua idade
# Se o nome e usuario forem digitados:
    #exiba:
        #seu nome eh:
        #seu nome invertido eh
        #seu nome contem ou nao espacos:
        #seu nome tem n letras
        #A primeira letra do seu nome eh:
        #A ultima letra do seu nome eh:
    #se nada for exibido:
        #desculpe, voce deixou campos vazios

nome = input('Digite seu nome')
idade = input('Digite sua idade')

if nome and idade:
    print(f'seu nome eh {nome}')
    print(f'seu nome invertido eh {nome[::-1]}')
    
    if ' ' in nome:
        print('seu nome contem espacos')
    else: print('seu nome nao contem espacos')   

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome eh {nome[0]}')
    print(f'A primeira ulima letra do seu nome eh {nome[-1]}')
else:
    print('desculpe, voce deixou campos vazios')