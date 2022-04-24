import PySimpleGUI as sg

tema = "Material1"

fonte = "Helvitica 15 bold italic"

usuario_correto = ""
senha_correta = ""
count = 0


def criar_janela():
    sg.theme(tema)

    layout = [
        [sg.Text("Usuário:")],
        [sg.Input("", key="-USUARIO-")],
        [sg.Text("Senha:")],
        [sg.Input("", key="-SENHA-")],
        [sg.Button("Login", ), sg.Button("Criar Conta")],
        [sg.Text("", key="-MENSAGEM-")]

    ]

    return sg.Window("Login", layout=layout, finalize=True, font=fonte)


def verificar_login():
    global usuario_correto, senha_correta, count

    if values["-USUARIO-"] == "" or values["-SENHA-"] == "":
        janela["-MENSAGEM-"].update("Por favor, preencha os campos disponiveis.")
    elif usuario_correto == values["-USUARIO-"] and senha_correta == values["-SENHA-"]:
        janela["-MENSAGEM-"].update("Login efetuado com sucesso!")
    elif usuario_correto != values["-USUARIO-"] or senha_correta != values["-SENHA-"]:
        janela["-MENSAGEM-"].update("Usuario ou senha incorretos.")


def cadastrar_login():
    global usuario_correto, senha_correta

    if values["-USUARIO-"] == "" or values["-SENHA-"] == "":
        janela["-MENSAGEM-"].update("Preencha os campos disponiveis.")
    elif values["-USUARIO-"] != "" and values["-SENHA-"] != "":
        if values["-USUARIO-"] == usuario_correto:
            janela["-MENSAGEM-"].update("Já existe um usuário com esse nome cadastrado :(\nutilize um nome de usuário diferente.")
        elif values["-USUARIO-"] != usuario_correto:
            usuario_correto = values["-USUARIO-"]
            senha_correta = values["-SENHA-"]
            janela["-MENSAGEM-"].update("Conta criada com sucesso.")


janela = criar_janela()

while True:
    window, event, values = sg.read_all_windows(timeout=1)

    if window == janela and event == sg.WIN_CLOSED:
        break
    if window == janela and event == "Login":
        verificar_login()
    if window == janela and event == "Criar Conta":
        cadastrar_login()
