import sys
sys.path.append('C:\\Users\\sackr\\dev\\python\\Curso em Vídeo\\Mundo3\\exceções')
from desafio115.lib.interface import *

def fileExist(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def makeFile(name):
    try:
        file = open(name, 'wt+')
        file.close()
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')
        
def readFile(name):
    try:
        file = open(name, 'rt')
    except:
        header('Erro ao ler arquivo')
    else:
        header('Pessoas Cadastradas')
        for c in file:
            data = c.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>5} anos')
    finally:
        file.close()
        
def create(file, name = 'desconhecido', age = 0):
    try:
        file = open(file, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            file.write(f'{name};{age}\n')
        except:
            print('Houve um erro ao escrer no arquivo!')
        else:
            print(f'Novo registro: {name.upper()}!')
            file.close()