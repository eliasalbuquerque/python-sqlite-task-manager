# title: 'module messages for menu and help commands'
# author: 'Elias Albuquerque'
# version: '0.2.1'
# created: '2024-08-02'
# update: '2024-08-04'


"""
Módulo que fornece funções para gerar mensagens de ajuda e 
listas de comandos para o gerenciador de tarefas.

Funções:
    get_help_message(): Retorna uma string com uma mensagem 
                        detalhada de ajuda, explicando os 
                        comandos disponíveis e seu uso.

    get_list_of_commands(): Retorna uma string com uma lista 
                            concisa dos comandos do 
                            gerenciador de tarefas.
"""


def get_help_message():
	"""
    Retorna uma string com uma mensagem detalhada de ajuda, explicando os comandos disponíveis e seu uso.
	"""
    
	return """
    Ações do Gerenciador de Tarefas:

      Tecla <TAB>  : O app possui auto-complete para os comandos utilizados no 
                     app e para as tarefas criadas no app.
                   : Como usar: Inicie a palavra e aperte <TAB>.
                   : Ex: $ taskpy> Ta+<TAB>  =>  $ taskpy> Tarefa

      --add        : Adiciona nova tarefa.
                   : Como usar: <tarefa> --add
                   : Ex: $ taskpy> Tarefa do dia --add

      --edit       : Edita uma tarefa existente.
                   : Como usar: <tarefa> --edit <tarefa_atualizada>
                   : Ex: $ taskpy> Tarefa do dia --edit Automatizar tudo

      --done       : Marca uma tarefa como realizada.
                   : Como usar: <tarefa> --done
                   : Ex: $ taskpy> Automatizar tudo --done

      --remove     : Remove uma tarefa existente do banco de dados.
                   : Como usar: <tarefa> --remove
                   : Ex: Automatizar tudo --remove

      --undo       : Desfaz uma ação realizada.
                   : Ex: $ taskpy> --undo

      --list_done  : Lista todas as tarefas concluídas.
                   : Ex: $ taskpy> --list_done

      --commands   : Lista todos os comandos.
                   : Ex: $ taskpy> --commands

      --help       : Mostra os comandos do app e como utilizar cada um.
                   : Ex: $ taskpy> --help

      exit         : Finalizar a aplicação e fechar o terminal.
                   : Ex: $ taskpy> exit

      --message-disable  : Desabilita mensagem inicial da aplicação que mostra 
                           como utilizar a aplicação.
                         : Ex: $ taskpy> --message-disable
      
      --message-enable   : Reabilita mensagem inicial da aplicação que mostra 
                           como utilizar a aplicação (habilitada por padrão).
                         : Ex: $ taskpy> --message-enable

      [Tip] Busque uma tarefa por qualquer palavra contida na tarefa e use o 
            autocomplete para selecionar a tarefa desejada.
    """

def get_list_of_commands():
	"""
	Retorna uma string com uma lista concisa dos comandos do gerenciador de tarefas.
	"""

	return """
    EDITANDO TAREFAS:                         COMANDOS DIRETOS NO TERMINAL
    --add    : <tarefa> --add                 $ taskpy> --list_done
    --edit   : <tarefa> --edit <new_tarefa>   $ taskpy> --commands 
    --done   : <tarefa> --done                $ taskpy> --undo 
    --remove : <tarefa> --remove              $ taskpy> --help 
                                              $ taskpy> exit

    * Desabilitar/habilitar mensagem de inicialização:
      --message-disable / --message-enable
    """
