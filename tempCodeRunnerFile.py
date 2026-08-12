def obter_nome():
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            if nome.strip() and all(caractere.isalpha() or caractere.isspace() for caractere in nome):
                return nome
            else:
                print("Nome inválido. Digite apenas letras e espaços.")
        except:
            print("Entrada inválida. Por favor, digite um nome válido.")


def obter_notas():
    notas = []
    while True:
        try:
            for nota in range(1, 4):
                notas.append(float(input(f"Digite a {nota}ª nota: ")))

            if all(0 <= nota <= 10 for nota in notas):
                return notas
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except:
            print("Entrada inválida. Por favor, digite um número.")


def calcular_media_aluno():
    alunos_aprovados = []
    alunos_recuperacao = []
    alunos_reprovados = []

    quantidade_alunos = 0

    while quantidade_alunos <= 0:

        try:
            quantidade_alunos = int(input("Digite a quantidade de alunos: "))
            if quantidade_alunos <= 0:
                print("Digite um numero maior que 0, tente novamente.")

        except:
            print("Entrada inválida. Por favor, digite um numero maior que 0.")

    for _ in range(quantidade_alunos):

        nome = obter_nome()

        notas = obter_notas()

        media = sum(notas) / len(notas)
        if media >= 7:
            alunos_aprovados.append((nome, media))
            print(f"{nome}, Situação Aprovado {media:.2f}")
        elif media >= 5:
            alunos_recuperacao.append((nome, media))
            print(f"{nome}, Situação Recuperação {media:.2f}")
        else:
            alunos_reprovados.append((nome, media))
            print(f"{nome}, Situação Reprovado {media:.2f}")

    print(f"\nAlunos aprovados: {len(alunos_aprovados)}")
    for nome, media in alunos_aprovados:
        print(f"{nome}: {media:.2f}")

    print(f"\nAlunos em recuperação: {len(alunos_recuperacao)}")
    for nome, media in alunos_recuperacao:
        print(f"{nome}: {media:.2f}")

    print(f"\nAlunos reprovados: {len(alunos_reprovados)}")
    for nome, media in alunos_reprovados:
        print(f"{nome}: {media:.2f}")

if __name__ == "__main__":
    calcular_media_aluno()