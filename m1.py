# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

# Lista de produtos, preços e carrinho # Itens são associados pelos índices
produtos = ["Arroz", "Feijao", "Oleo de soja", "Cafe", "Leite"]
precos   = [25.50, 8.90, 7.00, 50.00, 4.50]
carrinho = [0, 0, 0, 0, 0] # Carrinho começa vazio
carrinho_vazio = True

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

        item_encontrado = False
        for i in range(len(produtos)):
            if item == produtos[i].lower(): # Compara as strings, ambas em minúsculas
                while True:
                    qtd_string = input("Digite a quantidade: ")
                    if qtd_string.isdigit(): # Verifica se é dígito
                        quantidade = int(qtd_string)
                        if quantidade > 0: # Verifica se é maior que 0
                            break
                        else:
                            print("A quantidade deve ser maior que zero!")
                    else:
                        print("Digite apenas números inteiros positivos.")

                carrinho[i] += quantidade
                carrinho_vazio = False
                print(quantidade, "unidade(s) de", produtos[i], "adicionada(s) ao carrinho.")
                item_encontrado = True
        if not item_encontrado:
            print("Item não encontrado.")

    elif opcao == "2": # Ver total da compra
        total = 0
        print("\nItens no carrinho:")
        for i in range(len(produtos)): # Itera por todos itens
            if carrinho[i] > 0: # Se há unidades do item
                subtotal = precos[i] * carrinho[i]
                print(carrinho[i], "x", produtos[i], "(R$", f"{precos[i]:.2f}", "/un) = R$", f"{subtotal:.2f}")
                total += subtotal
        if carrinho_vazio:
            print("Carrinho vazio.")
        else:
            print("Total parcial: R$", f"{total:.2f}")

    elif opcao == "3": # Finalizar compra
        if carrinho_vazio:
            print("Carrinho vazio.")
            break

        print("\n======================== RECIBO ======================")
        print("------------------- ITENS COMPRADOS ------------------")
        print(f"{'Qtd.':<8} {'Produto':<14} {'Preço Un.':<15} {'Subtotal':>14}")
        print("------------------------------------------------------")

        total_bruto = 0

        for i in range(len(produtos)):
            if carrinho[i] > 0:
                subtotal = precos[i] * carrinho[i]

                if carrinho[i] > 3: # Desconto por volume a partir de 3 unidades
                    subtotal *= 0.97
                    total_bruto += subtotal
                    print(f"{carrinho[i]:>4} {'x':^3} {produtos[i]:<14} (R$ {precos[i]:>7.2f}/un) {('R$ ' + format(subtotal, '.2f')):>14}")
                    print(f"{'':<9}-> Desconto de 3% por volume aplicado.")
                else:
                    total_bruto += subtotal
                    print(f"{carrinho[i]:>4} {'x':^3} {produtos[i]:<14} (R$ {precos[i]:>7.2f}/un) {('R$ ' + format(subtotal, '.2f')):>14}")

        # Desconto geral: 10% para compras de R$100,00 a R$200,00; 20% para compras acima de R$200,00
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

        print("------------------------------------------------------")
        print(f"{'Total Bruto:':<40}R$ {total_bruto:>11.2f}")
        if percentual > 0:
            print(f"{'Desconto da Compra (' + str(percentual) + '%):':<40}R$ {desconto_geral:>11.2f}")
        print("------------------------------------------------------")
        print(f"{'Valor Final a Pagar:':<40}R$ {valor_final:>11.2f}")
        print("======================================================")
        print("Obrigado pela sua compra!")
        break

    else:
        print("Opção inválida!")
