# Daniel Henrique da Silva - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo           - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

# Lista de produtos e seus preços associados
produtos = {
    "arroz": 25.50,
    "feijao": 8.90,
    "oleo de soja": 7.00,
    "cafe": 50.00,
    "leite": 4.50
}

carrinho = {}

while True :
    print("\n**** Supermercado Python ****")
    print("1. Adicionar item ao carrinho")
    print("2. Ver total da compra")
    print("3. Finalizar compra")

    opcao = input("Escolha: ").strip()

    if opcao == "1": # Adicionar item ao carrinho
        print("Itens em estoque: Arroz, Feijao, Oleo de soja, Cafe, Leite.")
        item = input("Digite o nome do item que deseja adicionar: ").strip().lower() # Formata todos as letras como minúsculas e remove espaços

        if item == "oleo": # Tratamento especial para aceitar "oleo" como "oleo de soja"
            item = "oleo de soja"

        if item in produtos: # Verifica se o item está na lista de produtos
            quantidade = int(input("Digite a quantidade: "))
            if item in carrinho: # Se o item já estiver no carrinho, soma a quantidade adicionada
                carrinho[item] += quantidade
            else: # Se o item não estiver no carrinho, adiciona com a quantidade informada
                carrinho[item] = quantidade

            print(f"{quantidade} unidade(s) de {item} adicionada(s) ao carrinho.")
        else:
            print("Item não encontrado.")

    elif opcao == "2": # Ver total da compra
        if not carrinho: # Verifica se o carrinho está vazio
            print("Carrinho vazio.")
        else: # Mostra os itens no carrinho e o total parcial
            total = 0 
            print("\nItens no carrinho:")
            for item, quantidade in carrinho.items(): 
                preco = produtos[item]
                subtotal = preco * quantidade
                total += subtotal
                print(f"{quantidade} x {item.capitalize()} (R${preco:.2f}/un) = R${subtotal:.2f}")
            print(f"Total parcial: R${total:.2f}")

    elif opcao == "3": # Finalizar compra
        if not carrinho:
            print("Carrinho vazio.")
            break

        print("\n==================== RECIBO ===================")
        print("--------------- ITENS COMPRADOS ---------------")
        print(f"{'Qtd.':<6}{'Produto':<15}{'(Preco Un.)':<20}{'Subtotal':>10}")
        print("------------------------------------------------")

        total_bruto = 0

        for item, quantidade in carrinho.items():
            preco = produtos[item]
            subtotal = preco * quantidade
            desconto_volume = 0

            if quantidade > 3:  # Desconto de 3% no item
                desconto_volume = subtotal * 0.03
                subtotal -= desconto_volume

            total_bruto += subtotal

            # Linha principal do item (alinhado em colunas fixas)
            print(f"{str(quantidade)+' x':<6}{item.capitalize():<15}(R$ {preco:>6.2f}/un){subtotal:>15.2f}")

            # Mensagem de desconto logo abaixo do item
            if desconto_volume > 0:
                print(f"{'':<8}-> Desconto de 3% por volume aplicado.")

        # Desconto geral
        if total_bruto > 200:
            desconto_geral = total_bruto * 0.15
            percentual = 15
        elif total_bruto >= 100:
            desconto_geral = total_bruto * 0.10
            percentual = 10
        else:
            desconto_geral = 0
            percentual = 0

        valor_final = total_bruto - desconto_geral

        print("------------------------------------------------")
        print(f"{'Total Bruto:':<35}R$ {total_bruto:>7.2f}")
        if percentual > 0:
            print(f"Desconto da Compra ({percentual}%):{'':<11}R$ {desconto_geral:>7.2f}")
        print("------------------------------------------------")
        print(f"{'Valor Final a Pagar:':<35}R$ {valor_final:>7.2f}")
        print("================================================")
        print("Obrigado pela sua compra!")


        break
    else:
        print("Opção inválida!")
