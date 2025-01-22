import os
from lib.databases import *
from lib.interface import *
from lib.file import *
import random

menu()
arq = os.path.join('.', 'lib', 'databases', 'armazem.txt')
arq2 = os.path.join('.', 'lib', 'databases', 'compras.txt')

while True:
    decision = int(input('O que deseja fazer? Digite o número correspondente. '))
    
    if decision in [1, 2, 3, 4]:
        if decision == 1:
            produto = str(input('Qual produto você deseja consultar? ')).capitalize().strip()
            consultProduct(arq, produto)
            break

        elif decision == 2: # adicionar produto
            product_name = str(input('Nome do novo produto -> '))
            product_quantity = int(input('Unidades do novo produto -> '))
            product_ID = f'id' + str(random.randint(3000, 3999))
            createProduct(arq, product_name, product_quantity, product_ID)

        elif decision == 3: # remover produto
            produto = str(input('Qual produto você deseja remover? ')).capitalize().strip()
            deleteProduct(arq, produto)
            break

        elif decision == 4: # sair do programa 
            print('Encerrando o programa. Obrigado!')
            break
    else:
        print(f'Escolha inválida. Por favor, escolha entre as opções válidas: 1, 2, 3 ou 4.')
