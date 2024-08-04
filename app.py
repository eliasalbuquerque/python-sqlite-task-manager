# title: 'App TaskPy'
# author: 'Elias Albuquerque'
# version: '0.4.0'
# created: '2024-07-29'
# update: '2024-08-04'


import os
from prompt_toolkit import prompt
import src.messages as messages
import src.taskManager as taskManager
import src.startupMessage as startupMessage
import src.autoComplete as autoComplete


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_autocomplete(auto_complete, task_manager):
    get_tasks = task_manager.get_list_undone_tasks()
    auto_complete.update_tasks(get_tasks)

def main():
    """
    Executa o loop principal do aplicativo de gerenciamento de tarefas.
    """
    
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

    # Instâncias dos módulos:
    task_manager = taskManager.TaskManager(db_file)
    startup_manager = startupMessage.StartupMessage(config_file)

    # Carregar as tarefas do banco no cache de auto-complete
    get_tasks = task_manager.get_list_undone_tasks()
    auto_complete = autoComplete.AutoComplete(commands, get_tasks)

    # Mostrar mensagem na inicialização
    startup_manager.show_startup_message(task_manager)

    try:
        while True:
            clear_terminal()
            task_manager.list_undone_tasks()
            command = prompt('$ taskpy> ', completer=auto_complete)

            if command.strip() == "exit":
                break

            elif " --add" in command:
                task = command.split(" --add")[0].strip()
                task_manager.add_task(task)
                update_autocomplete(auto_complete, task_manager)

            elif " --edit " in command:
                parts = command.split(" --edit ")
                old_task = parts[0].strip()
                new_task = parts[1].strip()
                task_manager.edit_task(old_task, new_task)
                update_autocomplete(auto_complete, task_manager)

            elif " --done" in command:
                task = command.split(" --done")[0].strip()
                task_manager.done_task(task)
                update_autocomplete(auto_complete, task_manager)

            elif " --remove" in command:
                task = command.split(" --remove")[0].strip()
                task_manager.remove_task(task)
                update_autocomplete(auto_complete, task_manager)

            elif command == "--undo":
                task_manager.undo_task()
                update_autocomplete(auto_complete, task_manager)

            elif command == "--list_done":
                task_manager.list_done_tasks()

            elif command == "--commands":
                print(messages.get_list_of_commands())
                input("Pressione Enter para continuar... ")

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
        clear_terminal()

if __name__ == "__main__":
    main()
