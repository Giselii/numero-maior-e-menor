#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite outro número: '))
#print('O maior número é {}'.format(max(n1, n2, n3)))
#print('O menor número é {}'.format(min(n1, n2, n3)))
if (n1 < n2) & (n1 < n3):
    print('{} é o menor '.format(n1))
if (n2 < n3) & (n2 < n1):
    print('{} é o menor'. format(n2))
if (n3 < n1) & (n3 < n2):
    print('{} é o menor'.format(n3))
if (n1 == n2) & (n1 < n3):
    print('{} e {} são menores'.format(n1, n2))
if (n1 == n3) & (n1 < n2):
    print('{} e {} são menores'.format(n1, n3))
if (n2 == n3) & (n2 < n1):
    print('{} e {} sáo menores'.format(n2, n3))
if (n1 == n2 == n3):
    print('Os números são iguais')

if (n1 > n2) & (n1 > n3):
    print('{} é maior'.format(n1))
if (n2 > n1) & (n2 > n3):
    print('{} é maior'.format(n2))
if (n3 > n1) & (n3 > n2):
    print('{} é maior'.format(n3))
if (n1 == n2) & (n1 > n3):
    print('{} e {} são maiores'.format(n1, n2))
if (n1 == n3) & (n1 > n2):
    print('{} e {} são maiores'.format(n1, n3))
if (n2 == n3) & (n2 > n1):
    print('{} e {} são maiores'.format(n2, n3))



