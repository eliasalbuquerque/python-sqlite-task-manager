# title: 'autoComplete'
# author: 'Elias Albuquerque'
# version: '0.2.0'
# created: '2024-08-03'
# update: '2024-08-04'


from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from typing import List

class AutoComplete(Completer):
    """
    Classe para gerenciar o auto-complete de comandos e 
    tarefas no terminal.
    """
    
    def __init__(self, commands: List[str], get_tasks):
        self.commands = commands
        self.get_tasks = get_tasks

    def get_completions(self, document: Document, complete_event):
        """
        Fornece sugestões de auto-complete para comandos, tarefas 
        do cache e tarefas completadas.
        Args:
            document (Document): Documento do prompt_toolkit.
            complete_event (CompleteEvent): Evento de completamento.
        Yields:
            Completion: Sugestão de auto-complete, se disponível.
        """

        # Obter o texto antes do cursor, incluindo espaços
        text_before_cursor = document.text_before_cursor
        words = text_before_cursor.split() 

        # Obter o último termo (última palavra)
        last_term = words[-1]

        # Sugerir auto-complete para comandos
        for command in self.commands:
            if last_term == '' or command.startswith(last_term):
                yield Completion(command, start_position=-len(last_term))

        # Sugerir auto-complete com base em tarefas completas
        for option in self.get_tasks:
            if last_term in option:
                yield Completion(option, start_position=-len(last_term))

    def update_tasks(self, new_tasks: List[str]):
        """
        Atualiza a lista de tarefas para auto-complete.
        Args:
            new_tasks (List[str]): Nova lista de tarefas.
        """
        self.get_tasks = new_tasks
