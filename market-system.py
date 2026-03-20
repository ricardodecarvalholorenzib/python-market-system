# ---------------------------------------------------------
# Sistema de Gerenciamento de Estoque de Mercado
# Desenvolvido por: Ricardo de Carvalho
# Atualizações: Persistência, Edição de Produtos e Perfil
# ---------------------------------------------------------

import os
import json

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função auxiliar para evitar repetição de código ao salvar
def salvar_dados(operador, produtos):
    pacote_dados = {
        "operador": operador,
        "produtos": produtos
    }
    with open('estoque.json', 'w', encoding='utf-8') as f:
        json.dump(pacote_dados, f, indent=4, ensure_ascii=False)

# --- INÍCIO DA PERSISTÊNCIA (CARREGAR DADOS) ---
try:
    with open('estoque.json', 'r', encoding='utf-8') as f:
        dados_salvos = json.load(f)
        if isinstance(dados_salvos, dict):
            estoque = dados_salvos.get("produtos", [])
            nome_usuario = dados_salvos.get("operador", "")
        else:
            estoque = dados_salvos # Compatibilidade caso o arquivo antigo ainda exista
            nome_usuario = ""
except (FileNotFoundError, json.JSONDecodeError):
    estoque = []
    nome_usuario = ""
# -----------------------------------------------

# Se o sistema não lembrou o nome, pergunta agora
if not nome_usuario:
    nome_usuario = input("Olá! Bem-vindo ao sistema. Qual é o seu nome? ")
    salvar_dados(nome_usuario, estoque)
else:
    print(f"Bem-vindo de volta, {nome_usuario}!")
    input("Pressione ENTER para entrar no sistema...")

while True:
    limpar_tela()
    print(f"--- Sistema de Mercado | Operador: {nome_usuario} ---")
    print("\n[MENU PRINCIPAL]")
    print("1 - Cadastrar Novo Produto")
    print("2 - Listar Estoque Atual")
    print("3 - Editar/Remover Produto")
    print("4 - Editar Perfil (Nome do Operador)")
    print("0 - Sair do Sistema")
    
    opcao = input("\nSelecione uma opção: ").strip()

    # -----------------------------------------
    # OPÇÃO 1: CADASTRAR NOVO PRODUTO
    # -----------------------------------------
    if opcao == "1":
        limpar_tela()
        print("--- CADASTRO DE PRODUTO ---")
        nome_prod = input("Nome do produto: ").strip().capitalize()
        
        if nome_prod:
            preco_input = input(f"Preço de {nome_prod} (ex: 5.50): ").replace(',', '.')
            preco = float(preco_input) if preco_input else 0.0
            
            qtd_input = input(f"Quantidade em estoque de {nome_prod}: ")
            qtd = int(qtd_input) if qtd_input else 0

            novo_produto = {
                "nome": nome_prod, 
                "quantidade": qtd, 
                "preco": preco
            }
            
            estoque.append(novo_produto)
            salvar_dados(nome_usuario, estoque)

            print(f"\n✅ Sucesso: {nome_prod} foi adicionado e salvo!")
            input("Pressione ENTER para continuar...")
        else:
            print("\n❌ Erro: O nome do produto não pode estar vazio.")
            input("Pressione ENTER para continuar...")

    # -----------------------------------------
    # OPÇÃO 2: LISTAR ESTOQUE ATUAL
    # -----------------------------------------
    elif opcao == "2":
        limpar_tela()
        print(f"--- ESTOQUE ATUAL ({len(estoque)} itens) ---")
        
        if not estoque:
            print("O estoque está vazio no momento.")
        else:
            for i, item in enumerate(estoque):
                print(f"[{i}] 📦 Produto: {item['nome']:<15} | Qtd: {item['quantidade']:^5} | Preço: R${item['preco']:.2f}")
        
        input("\nPressione ENTER para voltar ao menu...")

    # -----------------------------------------
    # OPÇÃO 3: EDITAR OU REMOVER PRODUTO
    # -----------------------------------------
    elif opcao == "3":
        limpar_tela()
        print("--- GERENCIAR PRODUTOS ---")
        
        if not estoque:
            print("O estoque está vazio! Não há nada para editar.")
            input("\nPressione ENTER para voltar ao menu...")
            continue

        # Lista os produtos com seus índices
        for i, item in enumerate(estoque):
            print(f"[{i}] {item['nome']} (Qtd: {item['quantidade']} | Preço: R${item['preco']:.2f})")
        
        try:
            indice_input = input("\nDigite o número do produto que deseja gerenciar (ou ENTER para cancelar): ").strip()
            if not indice_input:
                continue
            
            indice = int(indice_input)
            
            if 0 <= indice < len(estoque):
                produto_alvo = estoque[indice]
                print(f"\nSelecionado: {produto_alvo['nome']}")
                print("1 - Alterar Nome")
                print("2 - Alterar Quantidade")
                print("3 - Alterar Preço")
                print("4 - ❌ Remover Produto")
                
                acao = input("O que deseja fazer? ").strip()
                
                if acao == "1":
                    novo_nome = input(f"Novo nome (atual: {produto_alvo['nome']}): ").strip().capitalize()
                    if novo_nome:
                        produto_alvo['nome'] = novo_nome
                        print("✅ Nome atualizado!")
                elif acao == "2":
                    nova_qtd = input(f"Nova quantidade (atual: {produto_alvo['quantidade']}): ").strip()
                    if nova_qtd.isdigit():
                        produto_alvo['quantidade'] = int(nova_qtd)
                        print("✅ Quantidade atualizada!")
                elif acao == "3":
                    novo_preco = input(f"Novo preço (atual: {produto_alvo['preco']:.2f}): ").replace(',', '.').strip()
                    try:
                        produto_alvo['preco'] = float(novo_preco)
                        print("✅ Preço atualizado!")
                    except ValueError:
                        print("❌ Erro: Valor inválido.")
                elif acao == "4":
                    confirmacao = input(f"Tem certeza que deseja remover '{produto_alvo['nome']}'? (s/n): ").strip().lower()
                    if confirmacao == 's':
                        estoque.pop(indice)
                        print("🗑️  Produto removido com sucesso!")
                else:
                    print("⚠️ Opção inválida.")
                
                # Salva as alterações, não importa qual tenha sido feita
                salvar_dados(nome_usuario, estoque)
                input("\nPressione ENTER para continuar...")
                
            else:
                print("❌ Erro: Produto não encontrado (índice inválido).")
                input("Pressione ENTER para continuar...")
                
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido.")
            input("Pressione ENTER para continuar...")

    # -----------------------------------------
    # OPÇÃO 4: EDITAR PERFIL
    # -----------------------------------------
    elif opcao == "4":
        limpar_tela()
        print("--- EDITAR PERFIL ---")
        print(f"Nome atual: {nome_usuario}")
        novo_nome = input("Digite o novo nome de operador (ou deixe em branco para cancelar): ").strip()
        
        if novo_nome:
            nome_usuario = novo_nome
            salvar_dados(nome_usuario, estoque)
            print(f"✅ Nome alterado para {nome_usuario} com sucesso!")
        
        input("\nPressione ENTER para voltar ao menu...")

    # -----------------------------------------
    # OPÇÃO 0: SAIR
    # -----------------------------------------
    elif opcao == "0":
        print(f"\nEncerrando sistema... Até logo, {nome_usuario}!")
        break
    
    else:
        print("\n⚠️ Opção inválida! Tente novamente.")
        input("Pressione ENTER para continuar...")
