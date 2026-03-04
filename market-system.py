# Sistema feito por: Ricardo de Carvalho

estoque = []

nome = input("Olá! Bem-vindo ao sistema do mercado. Qual é o seu nome? ")
print(f"\nBem-vindo, {nome}!")

while True:
    opcao = input(
        "\nEscolha uma opção:\n"
        "1 - Adicionar produto\n"
        "2 - Ver estoque\n"
        "0 - Sair\n"
        "Opção: "
    )

    if opcao == "1":
        produto = input("Digite o nome do produto: ").strip()

        if produto:
            estoque.append(produto)
            print(f"Produto '{produto}' adicionado com sucesso!")
        else:
            print("Nome inválido.")

    elif opcao == "2":
        if estoque:
            print("\nProdutos no estoque:")
            for item in estoque:
                print(f"- {item}")
        else:
            print("\nO estoque está vazio.")

    elif opcao == "0":
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")