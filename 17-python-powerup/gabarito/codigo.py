# Passo a Passo

# Passo 1 - Entrar no Sistema da Empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip intall pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
pyautogui.PAUSE = 1
# apertar a tecla windows
pyautogui.press("win")
# digite o nome do programa (google chrome)
pyautogui.write("edge")
# apertar tecla enter
pyautogui.press("enter")

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# espera carregar 
time.sleep(5)

# Passo 2 - Fazer Login
pyautogui.click(x=448, y=365)
# digitar o e-mail
pyautogui.write("pythtonimpressionador@gmail.com")
# passar para o campo senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("minha senha")
# clicar no logar
pyautogui.press("tab")
# entrer no logar 
pyautogui.press("enter")

# Passo 3 - Imporando a base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("gabarito/produtos.csv")
print(tabela)

# Passo 4 - Cadastro de Produtos
for linha in tabela.index:
    pyautogui.click(x=503, y=255)
    # codigo
    #codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # "1"
    pyautogui.press("tab")
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
       
    # enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

