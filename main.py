import PySimpleGUI as sg
import PyPDF2, threading

def layout():
    #Teste para ver os temas de interface disponiveis
    #sg.theme_previwer()

    #Selecionando o tema verde
    sg.theme('Green')

    #Criando nosso layout
    layout = [
        [sg.Text('Selecione o primeiro arquivo:', text_color='white')],
        [sg.Input(), sg.FilesBrowse(key='file1')],
        [sg.Text('Selecione o segundo arquivo:', text_color='white')],
        [sg.Input(), sg.FileBrowse(key='file2')],
        [sg.FolderBrowse(button_text='Selecione a pasta para salvar', key='folder'), sg.Button(button_text='Mesclar', key='merge'), sg.Button(button_text='Sair', key='exit')],
        [sg.Text('', key='mensagem', text_color='white')]
    ]

    return layout

#Função responsavel por mesclar os arquivos
def merge(file1, file2, folder):
    merge = PyPDF2.PdfMerger()
    merge.append(file1)
    merge.append(file2)
    merge.write(f'{folder}\\merge.pdf')

#Função principal
def main(layout):
    #Cria a janela
    window = sg.Window(title='NagaPdf', layout=layout, size=(450, 200))

    while True:
        #Lendo os eventos da tela
        events, values = window.read(timeout=10)
        try:
            if events == sg.WINDOW_CLOSED:
                break
            if events == 'merge':
                threading.Thread(target=merge, args=(values['file1'], values['file2'], values['folder'])).start()
                window['mensagem'].update('Arquivos mesclados, com sucesso!')
                window.refresh()
            if events == 'exit':
                window.close()      
        except:
            window['mensagem'].update('Algo deu errado!Tente novamente.')
            window.refresh()
            raise
main(layout())