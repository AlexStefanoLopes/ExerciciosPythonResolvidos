from livro import Livro

livro1 = Livro('Curso de Py','saefafe','fsaefaf','feafaef', 2018)
livro2 = Livro('Python para','saefafe','fsaefaf','feafaef', 2018)

livros = [livro1, livro2]

for l in livros:
    print(l)