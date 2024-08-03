# title: 'autoComplete'
# author: 'Elias Albuquerque'
# version: '0.1.0'
# created: '2024-08-03'
# update: '2024-08-03'


import readline

class AutoComplete:
    """
    Classe para gerenciar o auto-complete de comandos e 
    tarefas no terminal.

    Esta classe fornece funcionalidades para:

    - Sugerir auto-complete para comandos e tarefas 
      armazenadas no cache.
    - Configurar o auto-complete para o módulo `readline`.
    """
    
    def __init__(self, commands, cache):
        self.commands = commands
        self.cache = cache

    def completer(self, text, state):
        """
        Fornece sugestões de auto-complete para comandos e tarefas.
        Args:
            text (str): Texto digitado pelo usuário.
            state (int): Estado atual do auto-complete.
        Returns:
            str: Sugestão de auto-complete, se disponível.
        """

        options = [i for i in self.commands + list(self.cache.keys()) if i.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    def setup(self):
        """
        Configura o auto-complete para o readline.
        """
        
        readline.set_completer(self.completer)
        readline.parse_and_bind("tab: complete")