# Sistema-Caixa-Supermercado
Projeto M1: Sistema de Caixa de Supermercado
Autores: Daniel Henrique da Silva, Guilherme Melo, Leonardo Pinheiro de Souza

Este projeto foi desenvolvido como atividade da disciplina Introdução à Programação em Python.
O programa simula um sistema de caixa de supermercado, permitindo ao usuário adicionar produtos ao carrinho, visualizar o total da compra e finalizar a compra com emissão de um recibo formatado.
O sistema aplica regras de desconto tanto por quantidade quanto por valor total, reforçando conceitos de estruturas de decisão, repetição e manipulação de strings em Python.

**Como executar**
'python m1.py'

**Funcionalidades**
- Menu principal
  1. O usuário pode escolher entre:
    - Adicionar item ao carrinho
    - O programa solicita o nome do produto e a quantidade.
    - Aceita variações como "oleo" para "Oleo de soja".
  2. Garante que a quantidade seja um número inteiro positivo.
    - Ver total da compra
    - Exibe todos os itens adicionados ao carrinho com preço unitário, subtotal e total parcial.
    - Caso o carrinho esteja vazio, o sistema informa o usuário.
  3. Finalizar compra
    - Mostra o recibo completo com todos os produtos comprados.
    - Aplica desconto por volume:
      - 3% para produtos com mais de 3 unidades.
    - Aplica desconto geral:
      - 10% para compras entre R$ 100,00 e R$ 200,00.
      - 15% para compras acima de R$ 200,00.
    - Exibe o total bruto, descontos e valor final a pagar.
- Tratamento de entradas inválidas
    - Se o usuário digitar letras ou símbolos no menu → mensagem clara solicitando apenas números inteiros.
    - Se digitar número fora das opções (ex.: 7) → mensagem específica indicando opções válidas (1, 2 ou 3).

- Conceitos de Python aplicados
  - Estruturas de repetição (while, for)
  - Estruturas condicionais (if, elif, else)
  - Manipulação de strings (.lower(), .strip())
  - Listas e iteração com índices
  - Formatação de saída (f-strings, alinhamento e casas decimais)
  - Boas práticas de interação com o usuário (validações e mensagens claras)

Este trabalho consolidou os principais conceitos iniciais de Python, unindo teoria e prática em um projeto simples e funcional.
O sistema desenvolvido demonstra a importância da validação de entradas e do uso de estruturas básicas de programação para resolver problemas do dia a dia.
