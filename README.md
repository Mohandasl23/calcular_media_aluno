# Desafio 01 — calcular_media_aluno

Descrição

Este repositório contém o script `desafio_01.py`, que lê informações de alunos (nome e três notas), calcula a média de cada aluno e classifica-os em:
- Aprovado: média >= 7.0
- Recuperação: 5.0 <= média < 7.0
- Reprovado: média < 5.0

O programa valida entradas do usuário (quantidade de alunos, nome e notas) e exibe um resumo com a lista de alunos por situação.

Arquivo principal

- [desafio_01.py](C:/Users/mohan/Desktop/TESTE PYTHON/desafio_01.py)

Requisitos

- Python 3.6 ou superior
- Não há dependências externas (apenas a biblioteca padrão do Python)

Como executar

1. Abra um terminal (Prompt de Comando ou PowerShell) na pasta do projeto:

   cd "C:\\Users\\mohan\\Desktop\\TESTE PYTHON"

2. Execute o script com Python:

   python desafio_01.py

3. Siga as instruções interativas:
- Informe a quantidade de alunos (deve ser um inteiro maior que 0).
- Para cada aluno, digite o nome (apenas letras e espaços) e as três notas (valores numéricos entre 0 e 10).

Exemplo de execução

(Exemplo de interação — entradas do usuário precedidas por `>`):

Digite a quantidade de alunos: > 3

Aluno 1:
Digite o nome do aluno: > Maria Silva
Digite a primeira nota: > 8
Digite a segunda nota: > 7.5
Digite a terceira nota: > 6.5
Maria Silva, Situação Aprovado 7.33

Aluno 2:
Digite o nome do aluno: > João
Digite a primeira nota: > 5
Digite a segunda nota: > 4.5
Digite a terceira nota: > 6
João, Situação Recuperação 5.17

Aluno 3:
Digite o nome do aluno: > Ana
Digite a primeira nota: > 3
Digite a segunda nota: > 4
Digite a terceira nota: > 2
Ana, Situação Reprovado 3.00

Saída resumida:

Alunos aprovados: 1
Maria Silva: 7.33

Alunos em recuperação: 1
João: 5.17

Alunos reprovados: 1
Ana: 3.00

Comportamento e validações

- Quantidade de alunos: somente aceita inteiros maiores que zero. Em caso de valor inválido, solicita novamente.
- Nome do aluno: exige que a entrada contenha apenas letras e espaços. Strings vazias ou com caracteres inválidos são rejeitadas.
- Notas: cada nota deve ser um número entre 0 e 10 (inclusive). Entradas não numéricas ou fora do intervalo fazem o programa pedir novamente.
- As médias são calculadas como a média aritmética simples das três notas e são exibidas com duas casas decimais nos relatórios.

Possíveis melhorias

- Separar a lógica de entrada/saída da lógica de cálculo para facilitar testes automatizados.
- Adicionar opção para carregar dados de um arquivo CSV/JSON em vez de entrada interativa.
- Suportar nomes com caracteres acentuados e validação mais robusta (por exemplo, permitir hífens ou apóstrofos quando apropriado).
- Adicionar testes unitários para validar regras de classificação e validação de entrada.

Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

Licença

Este projeto está disponível sem uma licença específica — adicione uma licença se desejar compartilhá-lo publicamente.
