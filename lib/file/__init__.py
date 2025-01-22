from lib.interface import *

def consultProduct(arq, product):
    product_list = []
    with open(arq, 'r') as file:
        for line in file:
            line = line.replace(';', ' ')
            data = line.split()
            product_list.append(data[0])
        if product in product_list:
            showProduct(arq, product) 

def showProduct(arq, product):
    with open(arq, 'r') as file:
        for line in file:
            line = line.replace(';', ' ')
            data = line.split()
        linha()
        print(f'Produto: {data[0]} \nQuantidade: {data[1]}, \nID Produto: {data[2]}')
        linha()

def createProduct(arq, product_name, product_quantity, product_ID):
    with open(arq, 'a') as file:
        file.write(f'{product_name};{product_quantity};{product_ID}\n')
        linha()

def deleteProduct(arq, product_name):
    product_list = []
    with open(arq, 'r') as file:
        with open(arq, 'w') as wfile:
            for line in file:
                line = line.replace(';', ' ') # substitui o separador ; por um espaço vazio -> legibilidade da informação
                data = line.split() # splita a linha nos espaços vazios e retorna uma lista com cada string, ex: -> [jogo1, quantidade, id]
                product, quantity, product_ID = data[0], data[1], data[2]
                product_list.append(data[0])
                if product_name in product_list:
                    wfile.write((data[0].replace(data[0], '')))