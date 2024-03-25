#Serviu para manipulação dos arquivos

from interface._init__ import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #O "rt" faz a leitura do arquio caso ele exista
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+') #O "wt" Grava o arquivo, o "+" Ele cria o arquivo caso ele não exista
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"Nome: {dado[0]:<30}{dado[1]:>3} anos")
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at') #O "at" Colocar coisas dentro do arquivo
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()