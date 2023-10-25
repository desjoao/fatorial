#Lista 4 - Exercício 6

fatorial = 1
n = int(input('Informe um número inteiro e positivo: '))
while n <=0:
    print('Valor inválido.')
    n = int(input('Informe um número inteiro e positivo: '))
for i in range (1, n+1):
    fatorial *=i
print(f'O fatorial do número informado é de: {fatorial}')
