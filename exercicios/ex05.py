"""
Faca um programa que peca ao usuario para digirar um nuemro inteiro. informe se este numero e par ou impar/ Caso o usuario nao digite um numero inteiro, infprme que nao eh um numero inteiro.

try:
    numero_inteiro = int(input('Digite um numero'))
    if numero_inteiro % 2 == 0:
        print(f'O numero {numero_inteiro} eh Par')
    else:
        print(f'O numero {numero_inteiro} eh impar')
except ValueError:
    print('Voce nao digitou um numero inteiro!')
"""



"""
faca um programa que pergunta a hora ao usuario e, baseando-se no horario 23descrito, exiba a saudadacao apropriada. Ex
Bom dia 0-11, boa tarde 12-17 e Boa noite 18-23


try:
    hora = int(input('Digite um horario no formato 24h (0-23): '))
    if 0 < hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    elif 18 <= hora <= 23:
        print('Boa Noite')
except ValueError():
    print('Digite um valor valido!')


"""

"""
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreve "Seu nome eh curto" se tiver entre 5 e 6 letras, escreva "seu nome eh normal". Se for maior que 6 letras escreava "seu nome eh grande"
"""

nome = input('Digite seu nome: ')

if not nome.isalpha():
    print('Por favor, digite apenas letras, sem números ou símbolos.')
else:
    tamanho = len(nome)
    if tamanho <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
