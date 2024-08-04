# title: 'module taskManager'
# author: 'Elias Albuquerque'
# version: '0.2.1'
# created: '2024-08-02'
# update: '2024-08-04'


"""
Módulo de gerenciamento de tarefas com a funcionalidade de 
inicializar o banco de dados, editar tarefas e atualizar o 
cache.

Classe:
    TaskManager(cache, cache_file, db_file)
        Gerencia tarefas, incluindo criação, edição, exclusão, 
        marcação como concluída, desfazer a conclusão e 
        exibição de tarefas.
    Parâmetros:
        cache (LRUCache): Objeto de cache para armazenar 
                          tarefas.
        cache_file (str): Caminho para o arquivo do cache.
        db_file (str):    Caminho para o arquivo do banco de 
                          dados.
"""

import sqlite3
import os
import datetime


class TaskManager:
    """
    Gerencia tarefas, incluindo criação, edição, exclusão, 
    marcação como concluída, desfazer a conclusão e 
    exibição de tarefas.
    """

    def __init__(self, db_file):
        """
        Inicializa o gerenciador de tarefas.
        Parâmetros:
            cache (LRUCache): Objeto de cache para armazenar 
                              tarefas.
            cache_file (str): Caminho para o arquivo do cache.
            db_file (str):    Caminho para o arquivo do banco de 
                              dados.
        """
        self.db_file = db_file
        self.create_table()
        
        # Histórico de ações para o undo
        self.undo_history = []

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
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

    def add_task(self, task):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        self.undo_history.append(('add', task))

    def edit_task(self, old_task, new_task):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, old_task))
        conn.commit()
        conn.close()
        self.undo_history.append(('edit', old_task, new_task))

    def remove_task(self, task):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
        conn.commit()
        conn.close()
        self.undo_history.append(('remove', task))

    def done_task(self, task):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = TRUE, completed_at = ? WHERE task = ?", (datetime.datetime.now(), task))
        conn.commit()
        conn.close()
        self.undo_history.append(('done', task))

    def undo_task(self):
        if self.undo_history:
            action, *args = self.undo_history.pop()
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            if action == 'add':
                cursor.execute("DELETE FROM tasks WHERE task = ?", (args[0],))
            elif action == 'edit':
                old_task, new_task = args
                cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (old_task, new_task))
            elif action == 'remove':
                cursor.execute("INSERT INTO tasks (task) VALUES (?)", (args[0],))
            elif action == 'done':
                cursor.execute("UPDATE tasks SET completed = FALSE, completed_at = NULL WHERE task = ?", (args[0],))

            conn.commit()
            conn.close()
        else:
            print("Não há ações para desfazer.")

    def list_done_tasks(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE completed = 1;")
        tasks = cursor.fetchall()
        conn.close()
        print("")

        for task in tasks:
            completed_at = datetime.datetime.strptime(task[3], '%Y-%m-%d %H:%M:%S.%f')
            print(f"[x] {task[1]} - completed on {completed_at.strftime('%d/%m/%Y %H:%M')}")
        input("\nPressione Enter para continuar...")

    def list_undone_tasks(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE completed = 0;")
        tasks = cursor.fetchall()
        conn.close()

        for task in tasks:
            print(f"[ ] {task[1]}")

    def get_list_undone_tasks(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT task FROM tasks WHERE completed = 0;")
        tasks_from_db = [row[0] for row in cursor.fetchall()]
        conn.close()
        return tasks_from_db
        