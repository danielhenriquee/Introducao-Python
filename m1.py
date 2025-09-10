# Daniel Henrique da Silva - 8109346 - 2020
# Guilherme Melo - 26.1.0379 - 8576076
# Leonardo

# Produtos
produtos = {
    "arroz": 25.50,
    "feijao": 8.90,
    "oleo de soja": 7.00,
    "cafe": 50.00,
    "leite": 4.50
}

while True :
    print("**** Supermercado Python ****")
    print("1. Adicionar item ao carrinho")
    print("2. Ver total da compra")
    print("3. Finalizar compra")

    opcao = input("Escolha: ")

    if opcao == "1": # Adicionar item ao carrinho
        print("Itens em estoque: Arroz, Feijao, Oleo, Cafe, Leite.")
        produto = input("Digite o nome do item e a quantidade (ex: Arroz 4): ")
        
    elif opcao == "2": # Ver total da compra

    elif opcao == "3": # Finalizar compra

        break
    else:
        print("Opção inválida!")
