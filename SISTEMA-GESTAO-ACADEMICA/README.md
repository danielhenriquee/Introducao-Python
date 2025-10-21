# SISTEMA-GESTAO-ACADEMICA
Projeto M2: Sistema de Gestão Acadêmica

Autores: Daniel Henrique da Silva, Guilherme Melo, Leonardo Pinheiro de Souza

Este projeto foi desenvolvido como atividade da disciplina Introdução à Programação em Python.
O programa simula um sistema de gestão acadêmica, permitindo ao usuário cadastrar alunos, disciplinas, gerenciar matrículas e gerar relatórios acadêmicos detalhados.
O sistema reforça conceitos de estruturas de dados, validações, relações entre entidades e manipulação de listas e dicionários em Python.

**Como executar**
```
cd SISTEMA-GESTAO-ACADEMICA
python m2.py
```

**Funcionalidades**
- Menu principal - O usuário pode escolher entre:
  1) Gestão de Alunos
      - Cadastrar novos alunos (matrícula e nome).
      - Listar todos os alunos cadastrados.
      - Buscar aluno por matrícula.
      - Valida matrícula no formato correto (7 dígitos, primeiros 4 correspondendo ao ano de ingresso).
  2) Gestão de Disciplinas
      - Cadastrar novas disciplinas (código, nome e vagas).
      - Listar todas as disciplinas cadastradas.
      - Buscar disciplina por código.
      - Valida código no formato LLNNN (L = letra maiúscula, N = número) e quantidade de vagas (inteiro ≥ 0).
  3) Gestão de Matrículas
      - Realizar inscrições de alunos em disciplinas.
      - Lista todas as inscrições realizadas.
      - Verifica duplicidade de inscrição e disponibilidade de vagas.
  4) Geração de Relatórios
      - Listar alunos por disciplina (ordenados por matrícula).
      - Listar disciplinas por aluno (ordenadas por código).
      - Listar disciplinas com vagas esgotadas.
  5) Sair
      - Encerra o programa.
- Tratamento de entradas inválidas
    - Matrículas, códigos de disciplina e vagas são validados antes de aceitar o cadastro ou inscrição.
    - Se o usuário digitar valores inválidos ou fora do formato esperado → mensagem clara orientando sobre a entrada correta.
    - Todos os menus apresentam opções de “voltar” (digitar -1) para permitir navegação flexível.

**Conceitos de Python aplicados**
- Estruturas de repetição (while, for)
- Estruturas condicionais (if, elif, else)
- Funções com parâmetros e retornos claros
- Listas e dicionários, iteração e manipulação de dados
- Validação de entrada de usuário
- Ordenação de listas usando sorted() e lambda
- Formatação de saída para relatórios e tabelas
- Boas práticas de modularização e organização de código

Este trabalho consolida conceitos intermediários de Python, combinando validação de dados, relações entre estruturas, menus interativos e geração de relatórios, proporcionando um sistema funcional e próximo de uma aplicação real de gestão acadêmica.
