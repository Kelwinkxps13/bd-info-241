# Atividade-05
# Ricardo Duarte Taveira
# •
# 29 de jul. (editado: 29 de jul.)
# 100 pontos
# Data de entrega: Ontem
# Executar o programa em Python demonstrado na aula em 29-07-2024. 

# Evidenciar a execução printando a saída e postando no Google Classroom.

# Incluir o texto do programa no Github e ´postar do Google Classroom o caminho do Github.


import os
import sqlite3

all_id = []

script_dir = os.path.realpath(os.path.dirname(__file__))

db_path = os.path.join(script_dir, 'tasks.db')

conexao = sqlite3.connect(db_path)

conexao.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        description TEXT,
        completed INTEGER
    );
''')

def create_task(description):
    conexao.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))

def list_tasks():
    cursor = conexao.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    
    if not tasks:
        print("Não têm tarefas disponíveis.")
        return False
    else:
        print("######################")
        print()
        for task in tasks:
            print(f"ID: {task[0]}, Descrição: {task[1]}, Completada: {'Sim' if task[2] else 'Não'}")
            all_id.append(task[0])
        print()
        print("######################")
        return True

def mark_completed(task_id):
    conexao.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))

def delete_task(task_id):
    conexao.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

def pause():
    print("")
    input("pressione enter para continuar o exemplo...")
    print("")

def message(message):
    print("no proximo passo: ", message)
    pause()


# exemplo criado

message("o programa criará uma task chamada COMER PICANHA, marcará como concluida, e em seguida mostrará a lista")

create_task("comer picanha")
mark_completed(1)
list_tasks()


message("o programa criará uma task chamada BEBER CERVEJA, mostrará a lista, e em seguida excluirá a task COMER PICANHA")

create_task("beber cerveja")
list_tasks()
delete_task(1)

message("o programa mostrara a lista apos a exclusao da task COMER PICANHA")

list_tasks()

message("o programa marcara a task BEBER CERVEJA como concluida, e em seguida mostrará a tabela")

mark_completed(2)
list_tasks()

message("o programa exluirá a tabela e será fechado")

conexao.execute("DROP TABLE tasks")
conexao.close()