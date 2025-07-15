'''
introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar
'''

numero_str = print('Vou dobrar o numero que voce digitar')

try:
    numero_float = float(numero_str)
    print(f'Float: {numero_float}')
    print(f'O dobro de {numero_str} eh {numero_float * 2}')
except:
    print('Nao eh um numero')
