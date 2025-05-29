def menu_cadastro():
    print('=============== MENU ================')
    print('(1)Cadastrar')
    print('(2)Consultar')
    print('(3) - Matricular')
    print('(4) - Solicitar Histórico ')
    print('(0) - Sair')

def menu_consulta():
    print('=============== MENU ================')
    print('(1) - Aluno')
    print('(2) - Professorr')
    print('(0) - Sair')
    
op = input('Digite uma opção:')

# Validar se foi digitado um numero ? (if)
op = int(op)

if op >= 0 and op <= 0:
    if op == 1:
        menu_cadastro()
    elif op == 2:
        menu_consulta()
else : 
    print('Erro na escolha das opções!')