from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():
    a1 = Aluno('Gael', 5, "Informatica", "Pré 2")
    a1.fazer_matricula()
    a1.fazer_aniversario()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.dar_aula()
    p1.fazer_aniversario()

    f1 = Funcionario('Danilo', 28, 'SEO', 'Desenvolvimento')
    f1.bater_ponto()
    f1.fazer_aniversario()

if __name__ == '__main__':
    main()
