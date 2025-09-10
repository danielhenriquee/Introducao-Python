# Sistema-Caixa-Supermercado
Projeto M1: Sistema de Caixa de Supermercado

RASCUNHO
# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

# Lista de produtos, preços e carrinho (itens associados pelos índices)
produtos = ["Arroz", "Feijao", "Oleo de soja", "Cafe", "Leite"]
precos   = [25.50, 8.90, 7.00, 50.00, 4.50]
carrinho = [0, 0, 0, 0, 0]
carrinho_vazio = True

# Larguras para formatação
WIDTH = 56
COL_QTD = 6
COL_PROD = 20
COL_PRICE = 15
COL_SUB = 10

while True:
    print("\n**** Supermercado Python ****")
    print("1. Adicionar item ao carrinho")
    print("2. Ver total da compra")
    print("3. Finalizar compra")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        print("Itens em estoque: Arroz, Feijao, Oleo de soja, Cafe, Leite.")
        item = input("Digite o nome do item que deseja adicionar: ").strip().lower()
        if item == "oleo":
            item = "oleo de soja"

        item_encontrado = False
        for i in range(len(produtos)):
            if item == produtos[i].lower():
                while True:
                    qtd_string = input("Digite a quantidade: ")
                    if qtd_string.isdigit():
                        quantidade = int(qtd_string)
                        if quantidade > 0:
                            break
                        print("A quantidade deve ser maior que zero!")
                    else:
                        print("Digite apenas números inteiros positivos.")
                carrinho[i] += quantidade
                carrinho_vazio = False
                print(quantidade, "unidade(s) de", produtos[i], "adicionada(s) ao carrinho.")
                item_encontrado = True
                break
        if not item_encontrado:
            print("Item não encontrado.")

    elif opcao == "2":
        total = 0
        print("\nItens no carrinho:")
        for i in range(len(produtos)):
            if carrinho[i] > 0:
                subtotal = precos[i] * carrinho[i]
                print(carrinho[i], "x", produtos[i], "(R$", f"{precos[i]:.2f}", "/un) = R$", f"{subtotal:.2f}")
                total += subtotal
        if carrinho_vazio:
            print("Carrinho vazio.")
        else:
            print("Total parcial: R$", f"{total:.2f}")

    elif opcao == "3":
        if carrinho_vazio:
            print("Carrinho vazio.")
            break

        # Cabeçalho
        print("=" * WIDTH)
        print("RECIBO".center(WIDTH))
        print("-" * WIDTH)
        print("ITENS COMPRADOS".center(WIDTH))
        print("-" * WIDTH)
        print(f"{'Qtd.':<6}{'Produto':<20}{'(Preco Un.)':<15}{'Subtotal':>10}")
        print("-" * WIDTH)

        total_bruto = 0.0

        # Itens
        for i in range(len(produtos)):
            if carrinho[i] > 0:
                qtd = carrinho[i]
                preco = precos[i]
                subtotal = preco * qtd

                houve_volume = False
                if qtd > 3:           # desconto de 3% por volume
                    subtotal *= 0.97
                    houve_volume = True

                total_bruto += subtotal

                qtd_txt = f"{qtd} x"
                price_txt = f"(R$ {preco:>5.2f}/un)"
                sub_txt = f"R$ {subtotal:>7.2f}"
                print(f"{qtd_txt:<{COL_QTD}}{produtos[i]:<{COL_PROD}}{price_txt:<{COL_PRICE}}{sub_txt:>{COL_SUB}}")
                if houve_volume:
                    # linha explicativa logo abaixo do item
                    print(f"{'':<8}-> Desconto de 3% por volume aplicado.")

        # Desconto geral
        if total_bruto > 200:
            desconto_geral = total_bruto * 0.15
            percentual = 15
        elif total_bruto >= 100:
            desconto_geral = total_bruto * 0.10
            percentual = 10
        else:
            desconto_geral = 0.0
            percentual = 0

        valor_final = total_bruto - desconto_geral

        print("-" * WIDTH)
        print(f"{'Total Bruto:':<43}R$ {total_bruto:>10.2f}")
        if percentual > 0:
            print(f"{'Desconto da Compra (' + str(percentual) + '%):':<43}R$ {desconto_geral:>10.2f}")
        print("-" * WIDTH)
        print(f"{'Valor Final a Pagar:':<43}R$ {valor_final:>10.2f}")
        print("=" * WIDTH)
        print("Obrigado pela sua compra!")
        break

    else:
        print("Opção inválida!")
