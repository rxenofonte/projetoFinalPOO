from livro.livro_fisico import LivroFisico
from membro.membro import Membro


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        self.__membros.append(membro)
        print("Novo membro adicionado a biblioteca!")

    def deletarMembro(self, membro_id):
        for membro in self.__membros:
            if membro.membro_id == membro_id:
                self.__membros.remove(membro)
                print("Membro deletado com sucesso")

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print("Novo livro adicionado a biblioteca!")

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.livro_id == id:
                self.__livros.remove(livro)
                print("Livro deletado com sucesso")

    def listarLivros(self):
        print("------Livros Cadastrados --------")
        for livro in self.__livros:
            print("---- Dados do livro ----")
            print(f"Id:{livro.livro_id}")
            print(f"Titulo:{livro.titulo}")
            print(f"Autor:{livro.autor}")
            print(f"Ano:{livro.ano_publi}")
            print(f"Nº de páginas:{livro.numero_paginas} \n")

    def listarMembros(self):
        print("------Membros Cadastrados --------")
        for membro in self.__membros:
            print("---- Dados do livro ----")
            print(f"Id:{membro.membro_id}")
            print(f"Nome:{membro.endereco}")
            print(f"Telefone:{membro.telefone}")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    m1 = Membro(1,"Luis","Rua a", "88 888855-5555")
    m2 = Membro(2, "Carmen", "Rua C", "88 877855-5555")
    liv1 = LivroFisico(1, "Tolkien", "LOR",1970,700)
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(liv1)
    biblioteca.listarMembros()
    biblioteca.listarLivros()