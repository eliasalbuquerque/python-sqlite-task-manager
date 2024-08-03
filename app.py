# title: 'App TaskPy'
# author: 'Elias Albuquerque'
# version: '0.3.0'
# created: '2024-07-29'
# update: '2024-08-03'


import os
import datetime
from cachetools import LRUCache
import src.messages as messages
import src.taskManager as taskmanager
import src.startupMessage as startupMessage
import src.autoComplete as autoComplete


cache = LRUCache(maxsize=100) # Config do cache com tamanho máximo de 100 itens
cache_file = r'src\cache.json'
db_file = r'src\tasks.db'
config_file = r'src\config.json'
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

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Executa o loop principal do aplicativo de gerenciamento de tarefas.
    """

    # Instâncias dos módulos:
    task_manager = taskmanager.TaskManager(cache, cache_file, db_file)
    startup_manager = startupMessage.StartupMessage(config_file)
    auto_complete = autoComplete.AutoComplete(commands, cache)

    # Configurar auto-complete
    auto_complete.setup()

    # Mostrar mensagem na inicialização
    startup_manager.show_startup_message(task_manager)

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

            elif command == "--undo":
                task_manager.undo_task()

            elif command == "--help":
                print(messages.get_help_message())
                input("Pressione Enter para continuar... ")

            elif command == "--message-disable":
                startup_manager.disable_startup_message()
                
            elif command == "--message-enable":
                startup_manager.enable_startup_message()

            else:
                print("Comando inválido. Use --help para ver as opções.")
                input("Pressione Enter para continuar... ")
    finally:
        task_manager.save_cache()
        clear_terminal()

if __name__ == "__main__":
    main()
