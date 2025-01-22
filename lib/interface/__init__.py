def linha():
    print('\033[0;33m=\033[m'*50)

def menu():
    text = 'LOJA DO MARCOS'
    linha()
    print(f'{text:^50}')
    linha()
    actions()
    linha()

def actions():
    options = ['Consultar Produto', 'Adicionar Produto', 'Remover Produto', 'Sair']
    for pos, choice in enumerate(options):
        print(f'{pos+1} - {choice}')
