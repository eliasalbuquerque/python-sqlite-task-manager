# title: 'startupMessage'
# author: 'Elias Albuquerque'
# version: '0.1.0'
# created: '2024-08-03'
# update: '2024-08-03'


"""
Módulo para gerenciar a mensagem de inicialização da aplicação.

Este módulo fornece funcionalidades para controlar a exibição da 
mensagem de inicialização da aplicação, incluindo:

- Limpar o terminal antes de exibir a mensagem de inicialização.
- Exibir a mensagem de inicialização com informações sobre a 
  aplicação e instruções básicas.
- Habilitar/desabilitar a mensagem de inicialização através de um 
  arquivo de configuração.

Para utilizar este módulo, importe a classe `StartupMessage` e 
instancie-a com o caminho do arquivo de configuração. 
"""

import os
import json
import src.messages as messages

class StartupMessage:
    """
    Classe para gerenciar a mensagem de inicialização da aplicação.
    """

    def __init__(self, config_file):
        """
        Inicializa a classe com o caminho do arquivo de configuração.
        Args:
            config_file (str): Caminho para o arquivo de configuração.
        """

        self.config_file = config_file

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def create_config_file(self):
        """
        Cria o arquivo de configuração utilizado para habilitar ou desabilitar 
        a mensagem de uso da aplicação no inicio da execução.
        """

        config = {"show_startup_message": True}
        with open(self.config_file, 'w') as f:
            json.dump(config, f)

    def load_config_file(self):
        """
        Carrega as configurações do arquivo de configuração.
        Returns:
            dict: Dicionário com as configurações.
        """

        if not os.path.exists(self.config_file):
            self.create_config_file()
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        return config

    def disable_startup_message(self):
        """
        Desabilita a mensagem de inicialização.
        """

        config = self.load_config_file()
        config["show_startup_message"] = False
        with open(self.config_file, 'w') as f:
            json.dump(config, f)
        print("A mensagem de inicialização foi desabilitada.")
        input("Pressione Enter para continuar... ")

    def enable_startup_message(self):
        """
        Habilita a mensagem de inicialização.
        """

        config = self.load_config_file()
        config["show_startup_message"] = True
        with open(self.config_file, 'w') as f:
            json.dump(config, f)
        print("A mensagem de inicialização foi reabilitada.")
        input("Pressione Enter para continuar... ")

    def show_startup_message(self, task_manager):
        """
        Exibe a mensagem de inicialização se estiver habilitada.
        Args:
            task_manager: Objeto TaskManager para acessar a lista de tarefas.
        """

        config = self.load_config_file()
        if config.get("show_startup_message", True):
            self.clear_terminal()
            task_manager.list_undone_tasks()
            print("$ taskpy> ")
            print(messages.get_help_message())
            print("Para desabilitar essa mensagem de inicialização, \nuse o comando `--message-disable` no terminal.")
            input("Pressione Enter para continuar... ")
