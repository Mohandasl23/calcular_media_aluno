# Desafio 01 — Cálculo da média dos alunos

Este projeto contém um script em Python para ler o nome e as três notas de cada aluno, calcular a média e classificar a situação final:

- Aprovado: média >= 7.0
- Recuperação: 5.0 <= média < 7.0
- Reprovado: média < 5.0

A estrutura do código foi organizada em funções para facilitar a leitura e reutilização, além de usar a construção `if __name__ == "__main__":` para garantir que o programa execute somente quando o arquivo for executado diretamente.

Arquivo principal

- `desafio_01.py`

Requisitos

- Python 3.8 ou superior
- Biblioteca padrão do Python

Como executar

1. Abra o terminal na pasta do projeto.
2. Execute:

```bash
python desafio_01.py
```

3. Siga as instruções do programa.

Estrutura do código

O programa agora está dividido em funções:

- `obter_nome()`: valida o nome do aluno.
- `obter_notas()`: lê e valida as três notas.
- `calcular_media_aluno()`: controla o fluxo principal do programa.

A execução principal fica assim:

```python
if __name__ == "__main__":
    calcular_media_aluno()
```

Isso significa que:

- se o arquivo for executado diretamente, o programa roda;
- se o arquivo for importado em outro arquivo Python, a função principal não será executada automaticamente.

Exemplo de execução

```text
Digite a quantidade de alunos: 2
Digite o nome do aluno: Maria Silva
Digite a 1ª nota: 8
Digite a 2ª nota: 7
Digite a 3ª nota: 9
Maria Silva, Situação Aprovado 8.00
Digite o nome do aluno: João
Digite a 1ª nota: 5
Digite a 2ª nota: 4
Digite a 3ª nota: 6
João, Situação Recuperação 5.00

Alunos aprovados: 1
Maria Silva: 8.00

Alunos em recuperação: 1
João: 5.00

Alunos reprovados: 0
```

Validações incluídas

- Quantidade de alunos: deve ser um número inteiro maior que zero.
- Nome do aluno: aceita apenas letras e espaços.
- Notas: devem estar entre 0 e 10.
- Em caso de entrada inválida, o programa solicita novamente.

Autor

- Mohandas Leandro
