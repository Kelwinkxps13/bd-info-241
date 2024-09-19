# Atividade 10

### Proposta: 
- Crie um Banco de Dados envolvendo quatro tabelas. Uma tabela é um Cadastro (por exemplo TB_ALUNO), uma outra tabela é cadastro (por exempld TB_DISCIPLINA) e uma outra também é cadastro (por TB_PROFESSOR). A quarta tabela Matricula se relaciona com as tabelas Aluno, Professor e Disciplina. Na tabela Matricula existirão chaves estrangeiras para Aluno Professor e Disciplina. na tabela Matricula existirão atributos com as notas N1, N2 e Faltas. Criar instruções SQL com CRUD para as 4 tabelas. Implementar um código Python para ler a tabela Matricula e listar o status de aprovação dos alunos Matriculados

#### Segue abaixo o passo a passo:

- criar o arquivo .yml
  - faça **vim docker-compose.yml**
  - cole o script
    ~~~yml

    

    ~~~
  - feche o vim
- instale o connector do mysql para o python
  - faça **pip instal mysql-connector-python**
- crie um .py para criar as tabelas
  - faça **vim create_tables.py**
  - cole o codigo arquivo pra criar as tabelas no banco de dados
    - segue o código:
      ~~~python
      ~~~
