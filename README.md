# NagaPdf

Este projeto tem como objetivo criar uma aplicação simples que manipule arquivos PDF e os unifique em um único arquivo. Para tornar sua usabilidade mais acessível, foi implementada uma interface gráfica usando PySimpleGUI. O aprendizado adquirido na criação deste código envolveu a manipulação de arquivos em Python, a criação de interfaces gráficas simples e a implementação de threads.

## Possíveis problemas
Pode ocorrer alguns erros na aplicação devido à compatibilidade de bibliotecas e sistemas. Caso ocorra, tente me contatar para solucionar o problema.

## Instalação
A instalação pode ser feita de duas maneiras: baixando o arquivo executável ou gerando o próprio executável através do código fonte. Para fazer a instalação através do código fonte, siga as instruções:

1. Primeiro, você deve ter o PyInstaller. Para isso, use o seguinte comando para baixar:
~~~
pip install pyinstaller
~~~

2. Clone o repositório:
~~~
git clone https://github.com/p-ortilho/NagaPdf.git
~~~

3. Dentro da pasta NagaPdf, abra o terminal e execute o seguinte comando:
~~~
pyinstaller --onefile -w main.py
~~~

Com isso, você terá uma pasta chamada dist. Dentro dela, você encontrará um arquivo executável.