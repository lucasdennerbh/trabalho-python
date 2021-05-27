import csv
import sys
from livros import Livro

def main():
  
  opcao = "0";

  #Cria o menu e sai apenas quando selecionar a opção 6
  while opcao != "6":

    print()
    
    opcao = input("""Selecione uma das opções abaixo:
                    1 - Cadastrar livro
                    2 - Listar todos os livros em ordem alfabética
                    3 - Buscar livros pelo título
                    4 - Buscar livros pelo autor
                    5 - Listar todos os livros não lidos

                    6 - [x] Fechar """)
    
    if opcao == "1":

      titulo = input("Digite o título do livro: ")
      autor = input("Digite o autor do livro: ")
      editora = input("Digite a editora do livro: ")
      ano_publicacao = input("Digite o ano de publicação do livro: ")
      ano_aquisicao = input("Digite o ano de aquisição do livro: ")
      lido = input("Digite 1 se o livro foi lido e 0 caso contrário: ")
      data_lido = ''

      if(lido == '1'):
        data_lido = input("Digite a data de leitura do livro: ")

      livro = Livro(titulo, autor, editora, ano_publicacao, ano_aquisicao, lido, data_lido);

      Livro.cadastrar(livro)

    elif opcao == "2":
        Livro.listar()
        
    elif opcao=="3":
      titulo = input("Digite o título a pesquisar: ")
      Livro.buscarPeloTitulo(titulo)

    elif opcao=="4":
      autor = input("Digite o autor a pesquisar: ")
      Livro.buscarPeloAutor(autor)

    elif opcao=="5":
      Livro.listarNaoLidos()

main()