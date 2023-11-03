# Bibliotecas

- PySimpleGUI: Criação de interfaces graficas.
- os: Gerenciamento em manipulação de comandos do sistema.
- PyPDF2: Manipulação de arquivos pdf.

# Funções

### layout
Está função é resposanvel pela criação do layout da tela do aplicativo. Para fazer a atribuição de qual tema utilizar no programa usamos o seguinte metodo.
~~~
sg.theme('Green')
~~~
Dentro da bibliteca PySimpleGUI utilizamos uma matriz para definir o layout dos widghts da tela.
~~~
layout = [
        [sg.Text('Selecione a pasta que contêm os arquivos:', text_color='white')],
        [sg.Input(), sg.FolderBrowse()],
        [sg.Button('Mesclar Arquivos', key='folder'), sg.Text('', key='mensagem', text_color='white')]
        ]
~~~

sg.Text() - utilizado para mostrar texto na tela, recebe uma string que é o texto a ser mostrado e a cor do texto.
sg.Input() - metodo de entrada de dados.
sg.FolderBrowse() - utilizado para abrir o explorer de arquivos para seleção da pasta.
sg.Button() - cria um botão na tela, recebe como parametros uma string de mensagem, uma chave para identificação.
