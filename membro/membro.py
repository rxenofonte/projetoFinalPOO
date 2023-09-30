from livro.livro_fisico import LivroFisico


class Membro:
    def __init__(self, membro_id, nome, endereco, telefone):
        self.__membro_id = membro_id
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__livros_emprestados = []

    def emprestarLivro(self, livro: LivroFisico):
        if livro.estaDisponivel():
            self.__livros_emprestados.append(livro)
            livro.emprestar()
        else:
            print("Livro indiponível!")

    def devolverLivro(self, livro: LivroFisico):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            livro.devolver()
        else:
            print("Livro não encontrado!")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def membro_id(self):
        return self.__membro_id

    @membro_id.setter
    def membro_id(self, value):
        self.__membro_id = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def livros_emprestados(self):
        return self.__livros_emprestados

    @livros_emprestados.setter
    def livros_emprestados(self, value):
        self.__livros_emprestados = value

if __name__ == "__main__":
    membroBiblioteca = Membro(1, "Luana", "Rua a", "88888888")
    livro1 = LivroFisico(1, "Tolkien", "LOR", "1960", 1000)
    livro2 = LivroFisico(2, "HP", "Fulana", "1990", 300)
    membroBiblioteca.emprestarLivro(livro1)
    membroBiblioteca.emprestarLivro(livro2)
    membroBiblioteca.devolverLivro(livro2)