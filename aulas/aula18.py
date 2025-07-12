#Operadores logicos 
#and or not
#and - todas as condicoes precisam ser verdadeiras
#se qualquer valor for considerado falso,
#a expressao inteira sera avaliada naquele valor
#sao considerados falsy
# 0.00 '' False
# tambem existe o tipo nome que serve para representar nenhum valor

entrada = input('[E] entrar [S] sair: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
elif entrada == 'S':
    print('Saiu')
else:
    print('valor incorreto')
    