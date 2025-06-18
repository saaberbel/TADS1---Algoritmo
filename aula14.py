'''

def minha_funcao(*args, **kwargs):
    print('argumentos posicionais:', args)
    print("Argumentos  nomeados:", kwargs)

minha_funcao(1, 2, 8, "sexo", nome = "sarah", idade = 19)
'''

# kwargs vai retornar dicionario
# args retrorna tupla 
# PESQUISAR O QUE É TUPLA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def count_sublists(*args):
    count = 0
    for item in args:
        if isinstance(item, list):
            count += 1 + count_sublists(item)
    return count
count_sublists([244, 69, 157, 9136, 888, [8, 5, 6]], ['ana', 'laura', 'mattheus', 'sarah'])

# ESTUDAR ESSA MERDA FEDIDA