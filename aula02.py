'''a = 2
b = 3
print(a>b)
print(a<b)
print(a!=b)

a = int(input("digite um número: "))
b = int(input("digite outro número: "))

print(f'O resultado de {a} > {b} é {a > b}')
print(f'O resultado de {a} < {b} é {a< b}')
print(f'O resultado de {a} == {b} é {a == b}')
print(f'O resultado de {a} != {b} é {a != b}')
print(f'O resultado de {a} >= {b} é {a >= b}')
print(f'O resultado de {a} <= {b} é {a <= b}')
'''
'''
a = int(input('digite um número: '))
b = int(input('digite outro número: '))

print(f'o resultado de {a}"={b} or {a}<{b}, ou seja, {a!=b} or {a<b} é {a!=b or a<b}')

#No or qualquer uma das condições pode valer. A pergunta "esse ou esse" é para verificar se pelo menos um dos dois é verdadeiro.
'''

'''
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = a+b
print(f'A soma de {a} e {b} é C: {c}')

print(f'{a} é maior e diferente de {b}? {a>b and a!=b}')
print(f'{a} é maior que {c} e que {b}? {a>c and a>b}')
print(f'{c} é maior que {a} e que {b}? {c>a and c>b}')
#O and é a mesma coisa que o or: Uma verificação. Dessa vez verifica-se se ambas as condições são atendidas.
'''
'''
yrs = int(input('Digite a sua idade: '))
if yrs >= 18:
    print('pode dirigir')
if yrs < 18:
    print('não pode dirigir')
'''
'''
y = int(input('Digite a sua idade: '))
if y >= 18:
    print('pode dirigir')
else:
    print('não pode dirigir')
#else funciona bem para condições mutualmente excludentes.
'''
