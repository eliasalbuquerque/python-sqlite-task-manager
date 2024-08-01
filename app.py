"""
title: 'app'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-07-29'
update: '2024-08-01'
"""


# TODO:
# [x] Add tab completion for command line
# [x] Fix the bug in the --list of tasks: must show all completed and uncompleted tasks 
# [ ] Show --help on the first time of the app open
# [ ] Select for remove --help of the first time app executed

# --- bug na hora de remover tarefas e editar tarefas --------------------------
# ---- alteracao das funcoes list_tasks_undone() e list_tasks ------------------
# ----- adicionando o cache com persistencia -----------------------------------
import sqlite3
import os
import datetime
import readline
from cachetools import LRUCache
import json

# Configuração do cache LRU com tamanho máximo de 100 itens
cache = LRUCache(maxsize=100)
cache_file = 'cache.json'

# Comandos disponíveis
commands = [
    "--add",
    "--edit",
    "--list",
    "--remove",
    "--completed",
    "--undo",
    "exit",
    "--help"
]

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
    update_cache(task.split())

# Função para editar uma tarefa
def edit_task(old_task, new_task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, old_task))
    conn.commit()
    conn.close()
    update_cache(new_task.split())

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

# Função para listar todas as tarefas salvas no banco de dados
def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    for task in tasks:
        if task[2]:
            # Converte a string para um objeto datetime
            completed_at = datetime.datetime.strptime(task[3], '%Y-%m-%d %H:%M:%S.%f')
            print(f"[x] {task[1]} - completed on {completed_at.strftime('%d/%m/%Y %H:%M')}")
    input("\nPressione Enter para continuar...")

# Função para listar todas as tarefas ainda não concluídas
def list_tasks_undone():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE completed = 0;")
    tasks = cursor.fetchall()
    conn.close()

    for task in tasks:
        print(f"[ ] {task[1]}")

# Função para obter todas as tarefas salvas no banco de dados
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks")
    tasks = [task[0] for task in cursor.fetchall()]
    conn.close()
    return tasks

# Função para atualizar o cache de auto-complete
def update_cache(words):
    for word in words:
        cache[word] = None 

# Função para auto-complete
def completer(text, state):
    options = [i for i in commands + list(cache.keys()) if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Função para carregar o cache do arquivo
def load_cache():
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf8') as file:
            cache_data = json.load(file)
            for key in cache_data:
                cache[key] = None

# Função para salvar o cache no arquivo
def save_cache():
    with open(cache_file, 'w', encoding='utf8') as file:
        json.dump(list(cache.keys()), file)

# Configurar auto-complete
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

# Função principal do aplicativo
def main():
    create_table()
    load_cache()

    try:
        while True:
            clear_terminal()
            list_tasks_undone()
            command = input("$ taskpy> ")

            if command.strip() == "exit":
                break

            elif " --add" in command:
                task = command.split(" --add")[0].strip()  # Pega a tarefa antes de "--add"
                add_task(task)

            elif " --edit " in command:
                parts = command.split(" --edit ")
                old_task = parts[0].strip()  # Pega a tarefa antes de "--edit"
                new_task = parts[1].strip()  # Pega a nova tarefa após "--edit"
                edit_task(old_task, new_task)

            elif command == "--list":
                list_tasks()

            elif " --remove" in command:
                task = command.split(" --remove")[0].strip()  # Pega a tarefa antes de "--remove"
                remove_task(task)

            elif " --completed" in command:
                task = command.split(" --completed")[0].strip()  # Pega a tarefa antes de "--completed"
                complete_task(task)

            elif " --undo" in command:
                task = command.split(" --undo")[0].strip()  # Pega a tarefa antes de "--undo"
                undo_task(task)

            elif command == "--help":
                print("""
    Ações do Gerenciador de Tarefas:
        --add           : Adiciona nova tarefa: <task> --add
                        : Ex: Tarefa do dia --add

        --edit          : Edita uma tarefa existente: <task> --edit <new_task>
                        : Ex: Tarefa do dia --edit Automatizar tudo

        --list          : Listar todas as tarefas, concluídas: --list

        --remove        : Remove uma tarefa existente: <task> --remove
                        : Ex: Automatizar tudo --remove

        --completed     : Marcar uma tarefa como realizada: <task> --completed

        --undo          : Desfazer uma tarefa realizada: <task> --undo

        exit            : Finalizar a aplicação e fechar o terminal: exit
            """)
                input("Pressione Enter para continuar... ")

            else:
                print("Comando inválido. Use --help para ver as opções.")
                input("Pressione Enter para continuar... ")
    finally:
        save_cache()

if __name__ == "__main__":
    main()
