#importando bibliotecas
import PySimpleGUI as sg
import os, PyPDF2, threading

#função que cria o layout
def layout():
    #Teste para ver os temas de interface disponiveis
    #sg.theme_previewer()

    #Configura o tema como verde
    sg.theme('Green')

    #Criação do layout
    '''A definição de layout na biblioteca PySimpleGUI é definido atraves de uma matriz'''
    layout = [
        [sg.Text('Selecione a pasta que contêm os arquivos:', text_color='white')],
        [sg.Input(), sg.FolderBrowse()],
        [sg.Button('Mesclar Arquivos', key='folder'), sg.Text('', key='mensagem', text_color='white')]
        ]
    return layout

#Função que mescla os arquivos pdf
def merge(path):
    #Tratamento do diretorio
    if os.name == 'nt':
        path = path.replace('\\', '\\\\')
    #Objeto de mesclagem
    merge = PyPDF2.PdfMerger()
    #Lista de arquivos
    list_file = os.listdir(path)
    #Percorre a lista de arquivos e adiciona ao objeto de mesclagem
    for file in list_file:
        if '.pdf' in file:
            merge.append(f'{path}\\{file}')
    #Escreve o arquivo mesclado
    merge.write(f'{path}\\merger.pdf')

#função principal
def main(layout):
    #Criando a janela
    window = sg.Window(title='NagaPdf', layout=layout, size=(450, 200))

    #Condições de ações
    #Enquando a janela estiver aberta
    while True:
        #Lendo o que esta acontecendo na janela
        eventos, valores = window.read(timeout=10)
        try:
            #Fecha a janela se o evento for igual a WINDOW_CLOSED
            if eventos == sg.WINDOW_CLOSED:
                break
            #Se o evento for igual a folder, chamamos a função margePdf
            if eventos == 'folder':
                #Para poder funcionar scripts em paralelo usamos Thread para criar tasks de processamento
                threading.Thread(target=merge, args=(valores['Browse']))
                #Atualiza a tela para aparecer mensagem de sucesso
                window['mensagem'].update('Arquivos mesclados, com sucesso!')
                window.refresh()
                if valores[0] == '':
                    window['mensagem'].update('Selecione a pasta!')
                    window.refresh()
            print(valores)
        #Tratamento de erro
        except:
            window['mensagem'].update('Algo deu errado, tente novamente.')
            window.refresh()
            raise
main(layout())