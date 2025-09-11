"""
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
"""
contador = 0

while contador <= 100:
    #contador += 1

    if contador >= 10 and contador <= 7:
        print('Nao vou mostrar o 6')
        continue

    print(contador)
    if contador == 40:
        break
print('Acabou')

