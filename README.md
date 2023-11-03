# NagaPdf

Esse projeto tem como intuito o desenvolvimento de uma aplicação que trabalhe na manipulação de arquivos pdf, além do aprendizado no com o desenvolvimento de interface grafica. Em um primeiro momento a unica funcionalidade é de mesclar arquivos pdf em um unico arquivo, futuramente novas funcionalidades seram emprementadas.

## Possiveis problemas
Durante os teste de desenvolvimento foram encontrados alguns problemas na hora de mesclar os arquivos. Quando o pdf apresenta uma grande quantidade de paginas é possivel que o programa entre em um erro ou pare de funcionar, nesses casos a melhor opção é fechar o programa e tentar novamente.

## Instalação
Voce pode criar um executavel utilizando a biblioteca pyinstaller para isso basta seguir os passo:

~~~
pip install pyinstaller
~~~

Clone o repositorio do NagaPdf ou baixe somente o arquivo main.py. Apos isso abra o terminal onde está salvo o arquivo main.py, feito isso execute o seguinte comando:

~~~
pyinstaller --onefile -w main.py
~~~