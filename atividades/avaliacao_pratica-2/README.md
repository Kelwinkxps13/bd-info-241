# Atividade-Pratica-2

## nota de observação: a screenshot está diferente do passo a passo, pois as palavras **matemática, história e João** estavam com acento. alem disso, na screenshot tem mais pessoas e mais materias como química

### Proposta: 
- Terminar a avaliação-10 fazer consultas a tabela Matricula. 
- Criar scripts sql para para prova Prática
  1) Listar todos os aluno reprovados. Nome do Aluno, Nome da Disciplina, Nome do Professor, N1,N2,Média,Faltas, Status da reprovação("Reprovado por Média", "Reprovado por Falta") 
  2) Listar todos os alunos aprovados. Nome Aluno, Nome da Disciplina, Nome do Professor, N1,N2,Média,Faltas, Status da reprovação("Aprovado por Média"); 
  3) Listar a Quantidade de alunos aprovados;
  4) Listar a Quantidade de alunos reprovados;

1) Uso do PlaywithDocker com as seguintes operações: Instalação dos containers MYsql e PhpMyAdmin usando  o Docker Compose como definido na Avaliação-10;
2) Execução de Scripts similares aos scripts citados acima. 
3) Captura da imagem da saida do script;
4) Gerar no repositorio do GitHub a pasta avaliacao_pratica-2 e nela gravar as imagens dos resultados da execução dos scripts.
5) Copiar o link do github especificamente da pasta avaliacao_pratica_2 na Avaliação que será criada no GoogleClassrom.

#### Segue abaixo o passo a passo:

OBS: para colar os scripts no terminal do docker é **Control + Shift + V** (no meu caso)

- entrando em sua conta
    - faça **docker login**
    - digite seu nome de usuario e senha
- criar o arquivo .yml
  - faça **vim docker-compose.yml**
  - pressione a tecla **i** para entrar no modo INSERT do vim
  - cole o script usando **Control + Shift + V** (no meu caso é assim que cola)
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
  - fechando o vim
    - pressione **esc**
    - pressione **:** (dois pontos)
    - digite **wq** e aperte **enter**
      - o que o **wq** faz?
        - ele salva o arquivo
- instale o connector do mysql para o python
  - faça **pip install mysql-connector-python**
- criando o container
  - faça **docker-compose up -d**
- abrindo o mysql
  - faça **docker exec -it mysql_container mysql -u root -p**
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
      - pressione **enter** para confirmar, caso ele não o faça automaticamente
- antes de sair do mysql, voce deve fazer algumas inserçoes aleatorias para popular as tabelas
  - segue abaixo o codigo para popular as tabelas:
    ~~~sql
    -- Inserindo dados na tabela TB_ALUNOS
    INSERT INTO TB_ALUNOS (nome) VALUES ('Joao Silva');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Maria Oliveira');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Carlos Souza');

    -- Inserindo dados na tabela TB_PROFESSOR
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Ana Lima');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Pedro Santos');

    -- Inserindo dados na tabela TB_DISCIPLINA
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Matematica');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Historia');

    -- Inserindo dados na tabela Matricula
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (1, 1, 1, 7.5, 8.0, 2, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (2, 2, 2, 6.0, 5.5, 5, FALSE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (3, 1, 1, 9.0, 8.5, 1, TRUE);

    ~~~
    - pressione **enter** para confirmar, caso ele não o faça automaticamente
- saindo do mysql
  - faça **exit**

- criando o arquivo .py para realizar a tarefa
  - faça **vim main.py**
  - pressione a tecla **i** para entrar no modo INSERT do vim
  - cole o script usando **Control + Shift + V** (no meu caso é assim que cola)

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
    # Função para executar uma consulta e exibir os resultados
    def executar_consulta(query):
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            # Usar 'join' para formatar a saída sem parênteses ou vírgulas
            print(", ".join(str(item) for item in row))


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
  - fechando o vim
    - pressione **esc**
    - pressione **:** (dois pontos)
    - digite **wq** e aperte **enter**
      - o que o **wq** faz?
        - ele salva o arquivo

- executando o script
  - faça **python3 main.py**
  - o resultado deverá retornar o que se pede na questao.
- saindo de sua conta
    - faça **docker logout**
