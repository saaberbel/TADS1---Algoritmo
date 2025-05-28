lista = []

for x in range(5):
    num = int(input('Digite um número: '))
    lista.append(num)
    
print('Maior número:', max(lista))
print('Menor número:', min(lista))