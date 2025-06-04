'''
Funções Lambda - Lambda Function

def nome(x, y, z)
    corpo da função
    
sintaxe: lambda argumentos: expressão
- não existem para que se crie funçoes de muitas linhas, são funlções expressas.

'''
#dobro de uma variável

dobro = lambda x: x * 2

print('Exemplo - 1: Dobro de 5 = ', dobro(5))

soma = lambda x, y: x + y
print('Exemplo - 2: Soma de 3 e 4 = ', soma(3, 4))


#hipotenusa de um triangulo
'''catop ** 2 + catadj ** 2 == hipotenusa'''

hipotenusa = lambda catop, catadj: (catop ** 2 + catadj ** 2) ** 0.5
print('Exemplo - 3: hipotenusa = ', hipotenusa(8, 6))

#filter, map

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''pares = filter(função, array)'''
pares = list(filter(lambda x: x % 2 == 0, numeros))
print('Exemplo - 4: Numeros Pares: ', pares(3, 4))

