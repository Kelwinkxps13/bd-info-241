import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",  # Endereço do servidor MySQL (pode ser 'localhost')
        user="myuser",       # Nome de usuário MySQL
        password="mypassword",       # Senha do MySQL
        database="mydatabase"  # Nome do banco de dados
    )

def exibir_dados_tabela(conexao, tabela):
    cursor = conexao.cursor()
    query = f"SELECT * FROM {tabela}"
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    if resultados:
        colunas = [desc[0] for desc in cursor.description]
        largura_colunas = [len(coluna) for coluna in colunas]

        # Ajustar largura das colunas baseado no conteúdo da tabela
        for linha in resultados:
            for i, valor in enumerate(linha):
                largura_colunas[i] = max(largura_colunas[i], len(str(valor)))

        # Exibir cabeçalho formatado
        print(f"\nDados da tabela {tabela}:\n")
        cabecalho = " | ".join([colunas[i].ljust(largura_colunas[i]) for i in range(len(colunas))])
        print(cabecalho)
        print("-" * len(cabecalho))

        # Exibir os dados da tabela formatados
        for linha in resultados:
            linha_formatada = " | ".join([str(linha[i]).ljust(largura_colunas[i]) for i in range(len(linha))])
            print(linha_formatada)
    else:
        print(f"\nA tabela {tabela} está vazia.\n")
    
    cursor.close()

def menu():
    print("\nMenu:")
    print("1 - Exibir dados da tabela TB_ALUNOS")
    print("2 - Exibir dados da tabela TB_PROFESSOR")
    print("3 - Exibir dados da tabela TB_DISCIPLINA")
    print("4 - Exibir dados da tabela Matricula")
    print("5 - Sair")

def main():
    conexao = conectar_banco()
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            exibir_dados_tabela(conexao, "TB_ALUNOS")
        elif opcao == "2":
            exibir_dados_tabela(conexao, "TB_PROFESSOR")
        elif opcao == "3":
            exibir_dados_tabela(conexao, "TB_DISCIPLINA")
        elif opcao == "4":
            exibir_dados_tabela(conexao, "Matricula")
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conexao.close()

if __name__ == "__main__":
    main()
