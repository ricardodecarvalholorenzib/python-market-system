# ---------------------------------------------------------
# Sistema de Gerenciamento de Estoque de Mercado
# Desenvolvido por: Ricardo de Carvalho
# Atualizações: Adicionar preço e estoque nos produtos; Interface melhorada
# ---------------------------------------------------------

import os

def limpar_tela():
    # Função simples para manter o terminal organizado
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = []

nome_usuario = input("Olá! Bem-vindo ao sistema. Qual é o seu nome? ")
limpar_tela()
print(f"--- Sistema de Mercado | Operador: {nome_usuario} ---")

while True:
    print("\n[MENU PRINCIPAL]")
    print("1 - Cadastrar Novo Produto")
    print("2 - Listar Estoque Atual")
    print("0 - Sair do Sistema")
    
    opcao = input("\nSelecione uma opção: ").strip()

    if opcao == "1":
        limpar_tela()
        print("--- CADASTRO DE PRODUTO ---")
        nome_prod = input("Nome do produto: ").strip().capitalize()
        
        if nome_prod:
            # Captura de preço e quantidade com valores padrão caso o usuário não digite nada
            preco_input = input(f"Preço de {nome_prod} (ex: 5.50): ").replace(',', '.')
            preco = float(preco_input) if preco_input else 0.0
            
            qtd_input = input(f"Quantidade em estoque de {nome_prod}: ")
            qtd = int(qtd_input) if qtd_input else 0

            # Estrutura de Dicionário: Mantém os dados relacionados e organizados
            novo_produto = {
                "nome": nome_prod, 
                "quantidade": qtd, 
                "preco": preco
            }
            
            estoque.append(novo_produto)
            print(f"\n✅ Sucesso: {nome_prod} foi adicionado ao sistema!")
        else:
            print("\n❌ Erro: O nome do produto não pode estar vazio.")

    elif opcao == "2":
        limpar_tela()
        print(f"--- ESTOQUE ATUAL ({len(estoque)} itens) ---")
        
        if not estoque:
            print("O estoque está vazio no momento.")
        else:
            # Exibição formatada dos itens
            for item in estoque:
                print(f"📦 Produto: {item['nome']:<15} | Qtd: {item['quantidade']:^5} | Preço: R${item['preco']:.2f}")
        
        input("\nPressione ENTER para voltar ao menu...")
        limpar_tela()

    elif opcao == "0":
        print(f"\nEncerrando sistema... Até logo, {nome_usuario}!")
        break
    
    else:
        print("\n⚠️ Opção inválida! Tente novamente.")
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
