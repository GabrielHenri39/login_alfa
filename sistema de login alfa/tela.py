import PySimpleGUI as sg
sg.theme('DarkBlue16')


def login():
    janena = [[sg.Text(' Login:'), sg.Input(key='usuario', size=(20, 1))],
              [sg.Text('Senha'), sg.Input(key='senhar',password_char="*", size=(20, 1))],
              [sg.Button("Entra"), sg.Button('Cria')]
              ]
    return sg.Window('Login', layout=janena, finalize=True, size=(200, 100), element_justification='center')


def cadastro():
    janena = [[sg.Text(' Login:'), sg.Input(key='usuario', size=(20, 1))],
            #   [sg.Text('E-mail'), sg.Input(Key='email', size=(20, 1))]
              [sg.Text('Senha'), sg.Input(key='senhar',password_char="*", size=(20, 1))],
              [sg.Text('confimar\nSenha'), sg.Input(key='c_senhar', password_char="*", size=(20, 1))],
              [sg.Button("Cadastra"), sg.Button('Voltar'), ]
              ]
    return sg.Window('cria login', layout=janena, finalize=True, size=(200, 150), element_justification='center')


