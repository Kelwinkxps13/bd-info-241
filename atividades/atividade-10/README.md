# Atividade 10

### Proposta: 
- Crie um Banco de Dados envolvendo quatro tabelas. Uma tabela é um Cadastro (por exemplo TB_ALUNO), uma outra tabela é cadastro (por exempld TB_DISCIPLINA) e uma outra também é cadastro (por TB_PROFESSOR). A quarta tabela Matricula se relaciona com as tabelas Aluno, Professor e Disciplina. Na tabela Matricula existirão chaves estrangeiras para Aluno Professor e Disciplina. na tabela Matricula existirão atributos com as notas N1, N2 e Faltas. Criar instruções SQL com CRUD para as 4 tabelas. Implementar um código Python para ler a tabela Matricula e listar o status de aprovação dos alunos Matriculados

#### Segue abaixo o passo a passo:

- criar o arquivo .yml
  - faça **vim docker-compose.yml**
  - cole o script
    ~~~yml

    version: '3.8'

    services:
      mysql:
        image: mysql:8.0
        container_name: mysql_container
        environment:
          MYSQL_ROOT_PASSWORD: rootpassword
          MYSQL_DATABASE: mydatabase
          MYSQL_USER: myuser
          MYSQL_PASSWORD: mypassword
        volumes:
          - mysql_data:/var/lib/mysql
        ports:
          - "3306:3306"

      phpmyadmin:
        image: phpmyadmin/phpmyadmin
        container_name: phpmyadmin_container
        environment:
          PMA_HOST: mysql
          PMA_PORT: 3306
          PMA_USER: root
          PMA_PASSWORD: rootpassword
        ports:
          - "8080:80"
        depends_on:
          - mysql

    volumes:
      mysql_data:

    ~~~
  - feche o vim
- instale o connector do mysql para o python
  - faça **pip install mysql-connector-python**
- criando o container
  - faça **docker_compose up -d**
- abrindo o mysql
  - faça **docker exec -it mysql_container -u root -p**
  - ira solicitar a senha
    - coloque a senha **rootpassword**
  - apos isso, voce deve estar dentro do mysql
- entrando no database
  - faça **use mydatabase;**
- para criar as tabelas
  - cole o codigo abaixo pra criar as tabelas no banco de dados
    - segue o código:
      ~~~sql
      CREATE TABLE IF NOT EXISTS TB_ALUNOS (
          id INT PRIMARY KEY AUTO_INCREMENT,
          nome TEXT
      );
      CREATE TABLE IF NOT EXISTS TB_PROFESSOR (
          id INT PRIMARY KEY AUTO_INCREMENT,
          nome TEXT
      );
      CREATE TABLE IF NOT EXISTS TB_DISCIPLINA (
          id INT PRIMARY KEY AUTO_INCREMENT,
          nome TEXT
      );
      CREATE TABLE IF NOT EXISTS Matricula (
          id INT PRIMARY KEY AUTO_INCREMENT,
          nome_aluno INT,
          nome_professor INT,
          disciplina INT,
          nota_N1 FLOAT,
          nota_N2 FLOAT,
          faltas INT,
          Aprovado_SN BOOLEAN,
          FOREIGN KEY (nome_aluno) REFERENCES TB_ALUNOS(id),
          FOREIGN KEY (nome_professor) REFERENCES TB_PROFESSOR(id),
          FOREIGN KEY (disciplina) REFERENCES TB_DISCIPLINA(id)
      );
      ~~~
- antes de sair do mysql, voce deve fazer algumas inserçoes aleatorias para popular as tabelas
  - segue abaixo o codigo para popular as tabelas:
    ~~~sql
    -- Inserindo dados na tabela TB_ALUNOS
    INSERT INTO TB_ALUNOS (nome) VALUES ('João Silva');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Maria Oliveira');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Carlos Souza');

    -- Inserindo dados na tabela TB_PROFESSOR
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Ana Lima');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Pedro Santos');

    -- Inserindo dados na tabela TB_DISCIPLINA
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Matemática');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('História');

    -- Inserindo dados na tabela Matricula
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (1, 1, 1, 7.5, 8.0, 2, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (2, 2, 2, 6.0, 5.5, 5, FALSE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (3, 1, 1, 9.0, 8.5, 1, TRUE);

    -- Inserindo mais dados na tabela TB_ALUNOS
    INSERT INTO TB_ALUNOS (nome) VALUES ('Ana Paula');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Bruno Ferreira');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Clara Mendes');

    -- Inserindo mais dados na tabela TB_PROFESSOR
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Lucas Almeida');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Fernanda Costa');

    -- Inserindo mais dados na tabela TB_DISCIPLINA
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Física');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Química');

    -- Inserindo mais dados na tabela Matricula
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (4, 3, 3, 8.0, 7.5, 3, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (5, 4, 4, 5.5, 6.0, 4, FALSE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (6, 5, 5, 9.5, 9.0, 0, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (1, 3, 6, 7.0, 7.5, 2, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (2, 4, 6, 6.5, 6.0, 3, FALSE);

    ~~~

- criando o arquivo .py para realizar a tarefa
  - faça **vim main.py**
  - cole o script

    ~~~python
    import mysql.connector

    # Conexão com o banco de dados
    conn = mysql.connector.connect(
        host='localhost',
        user='myuser',
        password='mypassword',
        database='mydatabase'
    )

    cursor = conn.cursor()

    # Função para executar uma consulta e exibir os resultados
    def executar_consulta(query):
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    # 1. Listar todos os alunos reprovados
    query_reprovados = """
    SELECT 
        TB_ALUNOS.nome AS Nome_Aluno, 
        TB_DISCIPLINA.nome AS Nome_Disciplina, 
        TB_PROFESSOR.nome AS Nome_Professor, 
        Matricula.nota_N1, 
        Matricula.nota_N2, 
        (Matricula.nota_N1 + Matricula.nota_N2) / 2 AS Media, 
        Matricula.faltas, 
        CASE 
            WHEN (Matricula.nota_N1 + Matricula.nota_N2) / 2 < 6 THEN 'Reprovado por Média' 
            WHEN Matricula.faltas > 5 THEN 'Reprovado por Falta' 
        END AS Status_Reprovacao
    FROM Matricula
    JOIN TB_ALUNOS ON Matricula.nome_aluno = TB_ALUNOS.id
    JOIN TB_DISCIPLINA ON Matricula.disciplina = TB_DISCIPLINA.id
    JOIN TB_PROFESSOR ON Matricula.nome_professor = TB_PROFESSOR.id
    WHERE Matricula.Aprovado_SN = FALSE;
    """
    print("Alunos Reprovados:")
    executar_consulta(query_reprovados)

    # 2. Listar todos os alunos aprovados
    query_aprovados = """
    SELECT 
        TB_ALUNOS.nome AS Nome_Aluno, 
        TB_DISCIPLINA.nome AS Nome_Disciplina, 
        TB_PROFESSOR.nome AS Nome_Professor, 
        Matricula.nota_N1, 
        Matricula.nota_N2, 
        (Matricula.nota_N1 + Matricula.nota_N2) / 2 AS Media, 
        Matricula.faltas, 
        'Aprovado por Média' AS Status_Aprovacao
    FROM Matricula
    JOIN TB_ALUNOS ON Matricula.nome_aluno = TB_ALUNOS.id
    JOIN TB_DISCIPLINA ON Matricula.disciplina = TB_DISCIPLINA.id
    JOIN TB_PROFESSOR ON Matricula.nome_professor = TB_PROFESSOR.id
    WHERE Matricula.Aprovado_SN = TRUE;
    """
    print("\nAlunos Aprovados:")
    executar_consulta(query_aprovados)

    # 3. Listar a quantidade de alunos aprovados
    query_quantidade_aprovados = """
    SELECT COUNT(*) AS Quantidade_Aprovados
    FROM Matricula
    WHERE Matricula.Aprovado_SN = TRUE;
    """
    print("\nQuantidade de Alunos Aprovados:")
    executar_consulta(query_quantidade_aprovados)

    # 4. Listar a quantidade de alunos reprovados
    query_quantidade_reprovados = """
    SELECT COUNT(*) AS Quantidade_Reprovados
    FROM Matricula
    WHERE Matricula.Aprovado_SN = FALSE;
    """
    print("\nQuantidade de Alunos Reprovados:")
    executar_consulta(query_quantidade_reprovados)

    # Fechando a conexão
    cursor.close()
    conn.close()

    ~~~
    - feche o vim

- executando o script
  - faça **python3 main.py**
  - o resultado deverá retornar o que se pede na questao.