from rich import print, inspect

from cassesex007 import Aluno, Professor, Funcionario, Pessoa


def main():
    a1 = Aluno('Jose', 17, "Informatica", "T01")
    a1.fazer_matricula()
    a1.fazer_aniversario()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.dar_aula()
    p1.fazer_aniversario()

    f1 = Funcionario('Danilo', 28, 'SEO', 'Desenvolvimento')
    f1.bater_ponto()
    f1.fazer_aniversario()

    a1.estudar()
    p1.estudar()
    f1.estudar()



if __name__ == '__main__':
    main()
