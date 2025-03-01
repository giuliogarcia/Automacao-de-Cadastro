# Escrever o passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Realizar o login no sistema (colocar um usuario ou senha qualquer)
# Passo 3: Importar a base de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

import pyautogui
import time
pyautogui.PAUSE = 0.5

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas exemplo pyautogui.hotkey("ctrl", "c")
# pyautogui.PAUSE -> server para dar um tempo a cada comando
# Dica comando ctrl + L seleciona a barra do navegador para inserir o site


# Passo 1: Abrir o navegador chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer o login
# Selecionar o campo de e-mail
pyautogui.click(x=465, y=410)
# Preencher com o e-mail
pyautogui.write("seuemail@gmail.com")
# Passar para o campo de senha
pyautogui.press("tab")
# Preencher a senha
pyautogui.write("Kash#lsjadqjçd!@&*nqwjcsb")
# Clicar no botão para login
pyautogui.click(x=661, y=569)
time.sleep(2)

# Passo 3: Importar a base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    # Clicar no campo do código
    pyautogui.click(x=416, y=292)
    # Pegar a informação na tabela
    codigo = tabela.loc[linha, "codigo"]
    # Transformar em uma string e preencher a informação no campo código do produto
    pyautogui.write(str(codigo))
    # Passar para o próximo campo e continuar os preenchimentos
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    # Clicar em enviar para cadastrar o produto
    pyautogui.press("enter")
    # Dar um scroll tudo pra cima para cadastrar o novo produto
    pyautogui.scroll(5000)