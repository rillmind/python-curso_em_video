import sys
sys.path.append('C:\\Users\\sackr\\dev\\python\\Curso em Vídeo\\Mundo3\\exceções')
from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

file = 'pessoas.txt'

if not fileExist(file):
    makeFile(file)

while True:
    response = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if response == 1:
        readFile(file)
        sleep(1)
        continue
    elif response == 2:
        header('Novo Cadastro')
        name = str(input('Nome: '))
        age = readInt('Idade: ')
        create(file, name, age)
        sleep(1)
        continue
    elif response == 3:
        header('Saindo...')
        break
    else:
        header('\033[0;31m         ERRO! Opção inválida!.\033[m')