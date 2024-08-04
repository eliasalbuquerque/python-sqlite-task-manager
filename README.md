<!--
title: 'README: Gerenciador de Tarefas - TaskPy'
author: 'Elias Albuquerque'
created: '2024-08-03'
update: '2024-08-04'
-->


# Gerenciador de Tarefas - TaskPy

O TaskPy é um utilitário de linha de comando que auxilia no gerenciamento de 
suas tarefas. A aplicação oferece uma interface simples e direta, e utiliza um 
banco de dados SQLite para armazenar suas tarefas, garantindo persistência e 
facilidade de uso.

## Funcionalidades

* **Adicionar tarefas:** Adicione tarefas novas facilmente com o comando 
  `--add`.
* **Marcar tarefas como concluídas:** Utilize o comando `--done` para marcar 
  uma tarefa como realizada.
* **Editar tarefas:** Modifique tarefas existentes usando o comando `--edit`.
* **Remover tarefas:** Exclua tarefas indesejadas com o comando `--remove`.
* **Listar tarefas concluídas:** Visualize suas tarefas concluídas com o 
  comando `--list_done`.
* **Desfazer ações:** Utilize o comando `--undo` para reverter a última ação 
  realizada.
* **Auto-complete:** O TaskPy oferece auto-complete para comandos e tarefas.
* **Banco de dados SQLite:** As tarefas são armazenadas em um banco de dados 
  SQLite para persistência.
* **Mensagens de ajuda:** Use o comando `--help` para acessar um guia de 
  comandos e sua funcionalidade.
* **Desabilitar mensagens de inicialização:** Personalize sua experiência 
  desabilitando a mensagem de inicialização do aplicativo com 
  `--message-disable`.

### Vídeo do app em funcionamento

* https://youtu.be/0XbgVExjCRk

## Como usar

### Download e execução:

O TaskPy já está disponível como um executável. 
Basta fazer o download da versão mais recente 
[aqui](https://github.com/eliasalbuquerque/python-sqlite-task-manager/tree/main/download), 
e executar o arquivo.

### Modo desenvolvedor:

Se você deseja explorar o código do TaskPy ou contribuir com o projeto, siga 
estas instruções:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/eliasalbuquerque/python-sqlite-task-manager
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o script:**
   ```bash
   python app.py
   ```
   * O app iniciará com uma mensagem indicando todas as funções para edição das 
     tarefas e outras funções de comando de terminal.
   * Para adicionar uma tarefa, `digite a tarefa` e no final use o comando 
     `--add` para adicionar a tarefa.
   * Todos os comandos de edição de tarefa são executados da mesma forma:
     `tarefa` + `comando`
   * Use a lista de comandos `--commands` para listar os comandos do app, ou 
     use `--help` para uma visualização completa das funções.

## Comandos

**Comandos de edição de tarefas** permite você a criar, editar, concluir ou 
remover tarefas e o modo de uso é simples, basta digitar a tarefa e em seguida 
o comando relacionado a ação para a tarefa.

**Comandos diretos no terminal** permite listar tarefas concluídas, listar os 
comandos do app, desfazer ações, listar um menu de ajuda onde contém tudo o que 
precisa saber para a utilização do app e finalizar a execução da aplicação.

```
    EDITANDO TAREFAS:                         COMANDOS DIRETOS NO TERMINAL
    --add    : <tarefa> --add                 $ taskpy> --list_done
    --edit   : <tarefa> --edit <new_tarefa>   $ taskpy> --commands 
    --done   : <tarefa> --done                $ taskpy> --undo 
    --remove : <tarefa> --remove              $ taskpy> --help 
                                              $ taskpy> exit

    * Desabilitar/habilitar mensagem de inicialização:
      --message-disable / --message-enable
```

## Notas

* Este aplicativo é uma ferramenta útil para gerenciamento de tarefas simples.
* Ele oferece uma interface de linha de comando e armazena seus dados 
  localmente utilizando SQLite.
* Este script em Python contempla tratamento de entrada e saída, banco de dados 
  e manipulação de arquivos.

## Contribuições

O TaskPy é um aplicativo simples, com potencial para se tornar ainda mais 
poderoso com diversas oportunidades de aprimoramento.

**Algumas ideias para contribuir:**

* **Priorização de tarefas:** Implementar um sistema de prioridades para 
  destacar tarefas importantes, como "alta prioridade".
* **Customização do terminal:** Implementar a possibilidade de customização 
  para oferecer uma experiência 

**Se você tem interesse em contribuir, sinta-se à vontade para:**

* **Abrir issues:** Relate bugs, sugira novas funcionalidades ou melhorias.
* **Enviar pull requests:** Compartilhe seu código e ajude a melhorar o TaskPy.
* **Sugerir ideias:** Compartilhe suas ideias e ajude a moldar o futuro do 
  TaskPy.

## Conecte-se

Entre em contato para dúvidas, sugestões ou se deseja colaborar com o 
desenvolvimento do aplicativo!
