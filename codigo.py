# pyautogui - RPA = Robot Processing Automation
# Passo a Passo do projeto

# Passo 1 - Entrar no sistema da empresa

#pip install pyautogui
import pyautogui
import time
import pyperclip
# clicar -> pyautogui.click
# escrever -> pyauto    
#apertar uma tecla ->pyautogui.press
pyautogui.PAUSE = 0.5

#Aperta a tecla do windows
#pyautogui.press('super')

#Digita o nome do programa (chrome)
#pyautogui.write("chrome")

#Apertar "Enter"
#pyautogui.hotkey("enter")
pyautogui.click(x=582, y=90)

#Digitar o link (chrome)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
#Apertar "Enter"
pyautogui.hotkey("enter")
time.sleep(3)

# Passo 2 - Fazer login no sistema
#clicar no campo email
pyautogui.click(x=913, y=399)

#Digitar o email
pyautogui.write("matheusx.ono@gmail.com")

#Ir para o campo senha
pyautogui.press("tab")

#Digitar a Senha
pyautogui.write("1234")

#Apertar Enter
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3 - Importar a base de dados
#pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=830, y=289)

    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press('tab')

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press('tab')

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')


    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if not pd.isna(obs):
        pyautogui.write(obs)

    #cadatrar clicando em enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
# Passo 5 - Repetir isso até acabar a base de dados'
