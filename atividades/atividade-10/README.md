# Atividade 10

## nota de observação: a screenshot está diferente do passo a passo, pois as palavras **matemática, história e João** estavam com acento, alem de que tem menos registros nas tabelas.

### Proposta: 
- Crie um Banco de Dados envolvendo quatro tabelas. Uma tabela é um Cadastro (por exemplo TB_ALUNO), uma outra tabela é cadastro (por exempld TB_DISCIPLINA) e uma outra também é cadastro (por TB_PROFESSOR). A quarta tabela Matricula se relaciona com as tabelas Aluno, Professor e Disciplina. Na tabela Matricula existirão chaves estrangeiras para Aluno Professor e Disciplina. na tabela Matricula existirão atributos com as notas N1, N2 e Faltas. Criar instruções SQL com CRUD para as 4 tabelas. Implementar um código Python para ler a tabela Matricula e listar o status de aprovação dos alunos Matriculados

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
    INSERT INTO TB_ALUNOS (nome) VALUES ('Fernanda Costa');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Bruno Almeida');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Luana Carvalho');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Ricardo Barbosa');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Sofia Martins');
    INSERT INTO TB_ALUNOS (nome) VALUES ('Paulo Ferreira');

    -- Inserindo dados na tabela TB_PROFESSOR
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Ana Lima');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Pedro Santos');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Carla Mendes');
    INSERT INTO TB_PROFESSOR (nome) VALUES ('Prof. Joao Souza');

    -- Inserindo dados na tabela TB_DISCIPLINA
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Matematica');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Historia');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Fisica');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Quimica');
    INSERT INTO TB_DISCIPLINA (nome) VALUES ('Biologia');

    -- Inserindo dados na tabela Matricula
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (1, 1, 1, 7.5, 8.0, 2, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (2, 2, 2, 6.0, 5.5, 5, FALSE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (3, 1, 1, 9.0, 8.5, 1, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (4, 3, 3, 6.5, 7.0, 3, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (5, 4, 4, 5.0, 6.0, 6, FALSE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (6, 1, 1, 8.5, 9.0, 0, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (7, 2, 5, 7.0, 7.5, 4, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (8, 3, 3, 9.0, 8.5, 1, TRUE);
    INSERT INTO Matricula (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, faltas, Aprovado_SN) 
    VALUES (9, 4, 4, 5.5, 6.0, 8, FALSE);
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

    # Função para listar o status de aprovação dos alunos
    def listar_status_alunos():
        query = """
        SELECT 
            TB_ALUNOS.nome AS Nome_Aluno, 
            TB_DISCIPLINA.nome AS Nome_Disciplina, 
            TB_PROFESSOR.nome AS Nome_Professor, 
            Matricula.nota_N1, 
            Matricula.nota_N2, 
            (Matricula.nota_N1 + Matricula.nota_N2) / 2 AS Media, 
            Matricula.faltas, 
            CASE 
                WHEN (Matricula.nota_N1 + Matricula.nota_N2) / 2 >= 6 AND Matricula.faltas <= 5 THEN 'Aprovado' 
                ELSE 'Reprovado'
            END AS Status
        FROM Matricula
        JOIN TB_ALUNOS ON Matricula.nome_aluno = TB_ALUNOS.id
        JOIN TB_DISCIPLINA ON Matricula.disciplina = TB_DISCIPLINA.id
        JOIN TB_PROFESSOR ON Matricula.nome_professor = TB_PROFESSOR.id;
        """
        
        cursor.execute(query)
        result = cursor.fetchall()
        
        print("Status de Aprovação dos Alunos:")
        for row in result:
            print(", ".join(str(item) for item in row))

    # Executar a função para listar os status
    listar_status_alunos()

    # Fechar a conexão
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
