# NagaPdf

Este projeto tem como objetivo o desenvolvimento de uma aplicação que trabalhe na manipulação de arquivos PDF, além do aprendizado com o desenvolvimento de interface gráfica. Em um primeiro momento, a única funcionalidade é de mesclar arquivos PDF em um único arquivo, futuramente novas funcionalidades serão implementadas.

## Possíveis problemas
Durante os testes de desenvolvimento, foram encontrados alguns problemas na hora de mesclar os arquivos. Quando o PDF apresenta uma grande quantidade de páginas, é possível que o programa entre em um erro ou pare de funcionar. Nestes casos, a melhor opção é fechar o programa e tentar novamente.

## Instalação
Você pode criar um executável utilizando a biblioteca PyInstaller. Para isso, basta seguir os passos:

~~~
pip install pyinstaller
~~~

Clone o repositório do NagaPdf ou baixe somente o arquivo main.py. Após isso, abra o terminal onde está salvo o arquivo main.py e execute o seguinte comando:

~~~
pyinstaller --onefile -w main.py
~~~