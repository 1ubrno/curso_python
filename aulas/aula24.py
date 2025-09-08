'''
introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar
'''

numero = input('Vou dobrar o numero que voce digitar: ')

try:
    print('SRT:', numero)
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro de {numero} eh {numero_float * 2 }')

except:
   print('Isso nao eh um numero')