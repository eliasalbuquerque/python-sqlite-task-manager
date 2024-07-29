# """
# title: 'app'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-07-29'
# update: '2024-07-29'
# """


# import sqlite3
# import os
# import datetime

# # Função para limpar o terminal
# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Função para criar a tabela de tarefas no banco de dados
# def create_table():
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS tasks (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             task TEXT NOT NULL,
#             completed BOOLEAN DEFAULT FALSE,
#             completed_at DATETIME
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Função para adicionar uma tarefa
# def add_task(task):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
#     conn.commit()
#     conn.close()

# # Função para editar uma tarefa
# def edit_task(old_task, new_task):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, old_task))
#     conn.commit()
#     conn.close()

# # Função para remover uma tarefa
# def remove_task(task):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
#     conn.commit()
#     conn.close()

# # Função para marcar uma tarefa como concluída
# def complete_task(task):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE tasks SET completed = TRUE, completed_at = ? WHERE task = ?", (datetime.datetime.now(), task))
#     conn.commit()
#     conn.close()

# # Função para desfazer uma tarefa concluída
# def undo_task(task):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE tasks SET completed = FALSE, completed_at = NULL WHERE task = ?", (task,))
#     conn.commit()
#     conn.close()

# # Função para listar todas as tarefas
# def list_tasks():
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()
#     conn.close()

#     for task in tasks:
#         if task[2]:
#             print(f"[x] {task[1]} - completed on {task[3].strftime('%d/%m/%Y %H:%M')}")
#         else:
#             print(f"[ ] {task[1]}")

# # Função principal do aplicativo
# def main():
#     create_table()

#     while True:
#         clear_terminal()
#         list_tasks()
#         command = input("$ taskpy> ")

#         if command.strip() == "exit":
#             break

#         elif command.startswith("--add"):
#             task = command.split("--add")[0].strip()
#             add_task(task)

#         elif command.startswith("--edit"):
#             parts = command.split("--edit")
#             old_task = parts[0].strip()
#             new_task = parts[1].strip()
#             edit_task(old_task, new_task)

#         elif command == "--list":
#             list_tasks()

#         elif command.startswith("--remove"):
#             task = command.split("--remove")[0].strip()
#             remove_task(task)

#         elif command.startswith("--completed"):
#             task = command.split("--completed")[0].strip()
#             complete_task(task)

#         elif command.startswith("--undo"):
#             task = command.split("--undo")[0].strip()
#             undo_task(task)

#         elif command == "--help":
#             print("""
#     Ações do Gerenciador de Tarefas:
#         --add       : Adiciona nova tarefa: <task> --add
#                     : Ex: Tarefa do dia --add

#         --edit      : Edita uma tarefa existente: <task> --edit <task_edited>
#                     : Ex: Tarefa do dia --edit Atomatizar tudo

#         --list      : Listar todas as tarefas, concluídas: --list

#         --remove    : Remove uma tarefa existente: <task> --remove
#                     : Ex: Automatizar tudo --remove

#         --completed : Marcar uma tarefa como realizada: <task> --completed

#         --undo      : Desfazer uma tarefa realizada: <task> --undo

#         exit        : Finalizar a aplicação e fechar o terminal: exit
#             """)
#             input("Pressione Enter para continuar...")

#         else:
#             print("Comando inválido. Use --help para ver as opções.")
#             input("Pressione Enter para continuar...")

# if __name__ == "__main__":
#     main()
"""
title: 'app'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-07-29'
update: '2024-07-29'
"""


import sqlite3
import os
import datetime

# Função para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para criar a tabela de tarefas no banco de dados
def create_table():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            completed_at DATETIME
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar uma tarefa
def add_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

# Função para editar uma tarefa
def edit_task(old_task, new_task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, old_task))
    conn.commit()
    conn.close()

# Função para remover uma tarefa
def remove_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
    conn.commit()
    conn.close()

# Função para marcar uma tarefa como concluída
def complete_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = TRUE, completed_at = ? WHERE task = ?", (datetime.datetime.now(), task))
    conn.commit()
    conn.close()

# Função para desfazer uma tarefa concluída
def undo_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = FALSE, completed_at = NULL WHERE task = ?", (task,))
    conn.commit()
    conn.close()

# Função para listar todas as tarefas
def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    for task in tasks:
        if task[2]:
            # Converta a string para um objeto datetime
            completed_at = datetime.datetime.strptime(task[3], '%Y-%m-%d %H:%M:%S.%f')
            print(f"[x] {task[1]} - completed on {completed_at.strftime('%d/%m/%Y %H:%M')}")
        else:
            print(f"[ ] {task[1]}")

# Função principal do aplicativo
def main():
    create_table()

    while True:
        clear_terminal()
        list_tasks()
        command = input("$ taskpy> ")

        if command.strip() == "exit":
            break

        elif command.startswith("--add"):
            task = command.split("--add")[1].strip()  # Pega a tarefa após "--add"
            add_task(task)

        elif command.startswith("--edit"):
            parts = command.split("--edit")
            old_task = parts[0].strip()  # Pega a tarefa antes de "--edit"
            new_task = parts[1].strip()  # Pega a nova tarefa após "--edit"
            edit_task(old_task, new_task)

        elif command == "--list":
            list_tasks()

        elif command.startswith("--remove"):
            task = command.split("--remove")[1].strip()  # Pega a tarefa após "--remove"
            remove_task(task)

        elif command.startswith("--completed"):
            task = command.split("--completed")[1].strip()  # Pega a tarefa após "--completed"
            complete_task(task)

        elif command.startswith("--undo"):
            task = command.split("--undo")[1].strip()  # Pega a tarefa após "--undo"
            undo_task(task)

        elif command == "--help":
            print("""
    Ações do Gerenciador de Tarefas:
        --add       : Adiciona nova tarefa: <task> --add
                    : Ex: Tarefa do dia --add

        --edit      : Edita uma tarefa existente: <task> --edit <task_edited>
                    : Ex: Tarefa do dia --edit Atomatizar tudo

        --list      : Listar todas as tarefas, concluídas: --list

        --remove    : Remove uma tarefa existente: <task> --remove
                    : Ex: Automatizar tudo --remove

        --completed : Marcar uma tarefa como realizada: <task> --completed

        --undo      : Desfazer uma tarefa realizada: <task> --undo

        exit        : Finalizar a aplicação e fechar o terminal: exit
            """)
            input("Pressione Enter para continuar...")

        else:
            print("Comando inválido. Use --help para ver as opções.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()