from interface._init__ import * #O "*" serve p/ importar tudo que tem dentro do arquivo
from interface.arquivo import *
from time import sleep

arq = 'Felipinho.txt'

#Verifica se o arquivo existe, se não existir cria o arquivo com a função "CriarArquivo"
if not arquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoas", "Sair do Sistema"])

    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
        #Opção para sair do sistema
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mErro! Digite uma opção válida!\033[m")
    sleep(2)