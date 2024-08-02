# title: 'app'
# author: 'Elias Albuquerque'
# version: '0.2.1'
# created: '2024-07-29'
# update: '2024-08-02'

# NOTE: alteraçoes realizadas nessa versao:
# * implementado modulos taskmanager e messages
# * implementado diretorio .\src para modulos, cache e banco de dados
# * implementado lista de comandos
# * implementado docstring inspirado no estilo Google
# * implementar iniciar com --help e desabilitar se quiser
# TODO:
# atualizar o arquivo readme.md
# implementar comando 'undo'

import sqlite3
import os
import datetime
import readline
from cachetools import LRUCache
import json
import src.messages as messages
import src.taskmanager as taskmanager

# Configuração do cache LRU com tamanho máximo de 100 itens
cache = LRUCache(maxsize=100)
cache_file = r'src\cache.json'
db_file = r'src\tasks.db'
config_file = r'src\config.json'

# Comandos disponíveis
commands = [
    "--add",
    "--edit",
    "--done",
    "--remove",
    "--list_done",
    "--commands",
    "--undo",
    "--help",
    "--message-disable",
    "--message-enable",
    "exit",
]

def completer(text, state):
    """
    Fornece sugestões de auto-complete para comandos e tarefas.
    Args:
        text (str): Texto digitado pelo usuário.
        state (int): Estado atual do auto-complete.
    Returns:
        str: Sugestão de auto-complete, se disponível.
    """

    options = [i for i in commands + list(cache.keys()) if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções de configuração de mensagem de inicializaçao
def create_config_file():
    """
    Cria o arquivo de configuração utilizado para habilitar ou desabilitar a 
    mensagem de uso da aplicação no inicio da execução.
    """

    config = {"show_startup_message": True}
    with open(config_file, 'w') as f:
        json.dump(config, f)

def load_config_file():
    if not os.path.exists(config_file):
        create_config_file()
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def disable_startup_message():
    config = load_config_file()
    config["show_startup_message"] = False
    with open(config_file, 'w') as f:
        json.dump(config, f)
    print("A mensagem de inicialização foi desabilitada.")
    input("Pressione Enter para continuar... ")

def enable_startup_message():
    config = load_config_file()
    config["show_startup_message"] = True
    with open(config_file, 'w') as f:
        json.dump(config, f)
    print("A mensagem de inicialização foi reabilitada.")
    input("Pressione Enter para continuar... ")

def startup_message(task_manager):
    config = load_config_file()
    if config.get("show_startup_message", True):
        clear_terminal()
        task_manager.list_undone_tasks()
        print("$ taskpy> ")
        print(messages.get_help_message())
        input("Pressione Enter para continuar... ")

def main():
    """
    Executa o loop principal do aplicativo de gerenciamento de tarefas.
    """

    task_manager = taskmanager.TaskManager(cache, cache_file, db_file)

    # Configurar auto-complete
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    # Mostrar mensagem na inicialização
    startup_message(task_manager)

    try:
        while True:
            clear_terminal()
            task_manager.list_undone_tasks()
            command = input("$ taskpy> ")

            if command.strip() == "exit":
                break

            elif " --add" in command:
                task = command.split(" --add")[0].strip()
                task_manager.add_task(task)

            elif " --edit " in command:
                parts = command.split(" --edit ")
                old_task = parts[0].strip()
                new_task = parts[1].strip()
                task_manager.edit_task(old_task, new_task)

            elif " --done" in command:
                task = command.split(" --done")[0].strip()
                task_manager.done_task(task)

            elif " --remove" in command:
                task = command.split(" --remove")[0].strip()
                task_manager.remove_task(task)

            elif command == "--list_done":
                task_manager.list_done_tasks()

            elif command == "--commands":
                print(messages.get_list_of_commands())
                input("Pressione Enter para continuar... ")

            elif command == " --undo":
                # print(">>> Ainda não implementado!")
                task_manager.undo_task(task)

            elif command == "--help":
                print(messages.get_help_message())
                input("Pressione Enter para continuar... ")

            elif command == "--message-disable":
                disable_startup_message()
                
            elif command == "--message-enable":
                enable_startup_message()

            else:
                print("Comando inválido. Use --help para ver as opções.")
                input("Pressione Enter para continuar... ")
    finally:
        task_manager.save_cache()

if __name__ == "__main__":
    main()
