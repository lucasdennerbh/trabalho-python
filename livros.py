import csv
import sys
import sqlite3

class Livro: 

	def __init__(self, titulo, autor, editora, ano_publicacao, ano_aquisicao, lido, data_lido):
		self.titulo = titulo
		self.autor = autor
		self.editora = editora
		self.ano_publicacao = ano_publicacao
		self.ano_aquisicao = ano_aquisicao
		self.lido = lido
		self.data_lido = data_lido

	def cadastrar(livro):

		conn = sqlite3.connect('livros.db')
		cursor = conn.cursor()

		# inserindo dados na tabela
		cursor.execute("""
		INSERT INTO livro (titulo, autor, editora, ano_publicacao, ano_aquisicao, lido, data_lido)
		VALUES (?,?,?,?,?,?,?)
		""", (livro.titulo, livro.autor, livro.editora, livro.ano_publicacao, livro.ano_aquisicao, livro.lido, livro.data_lido))

		conn.commit()

		print('Dados inseridos com sucesso.')

		conn.close()

	def listar():

		print('Listando todos os livros')

		conn = sqlite3.connect('livros.db')
		cursor = conn.cursor()

		# lendo os dados
		cursor.execute("""
		SELECT * FROM livro ORDER BY titulo;
		""")

		for linha in cursor.fetchall():
		    print(linha)

		conn.close()

	def buscarPeloTitulo(titulo):

		print('Buscando livros com o título: ', titulo)

		conn = sqlite3.connect('livros.db')
		cursor = conn.cursor()

		# lendo os dados
		cursor.execute("""
		SELECT * FROM livro WHERE titulo = ?;
		""", (titulo,))

		for linha in cursor.fetchall():
		    print(linha)

		conn.close()

	def buscarPeloAutor(autor):

		print('Buscando livros do autor: ', autor)

		conn = sqlite3.connect('livros.db')
		cursor = conn.cursor()

		# lendo os dados
		cursor.execute("""
		SELECT * FROM livro WHERE autor = ?;
		""", (autor,))

		for linha in cursor.fetchall():
		    print(linha)

		conn.close()

	def listarNaoLidos():

		print('Buscando livros não lidos: ')

		conn = sqlite3.connect('livros.db')
		cursor = conn.cursor()

		# lendo os dados
		cursor.execute("""
		SELECT * FROM livro WHERE lido = ?;
		""", ('0',))

		for linha in cursor.fetchall():
		    print(linha)

		conn.close()
