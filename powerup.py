#Passo 1 - entrar no sistema da empresa
#Link - https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Passo 2 - fazer login

#Passo 3 - acessar a base de dados

#Passo 4 - cadastrar um produto

#Passo 5 - repetir o passo 4 até registrar todos os produtos
import time
import pyautogui


#pyautogui.click - click
#pytautogui.write - write
#pytautogui.press - pressiona uma tecla
#pytautogui.hotkey - combinação de teclas
#pytautogui.screenshot - tira um print da tela
#pytautogui.scroll - rola a tela

pyautogui.PAUSE = 0.5
#Passo 1 - entrar no sistema da empresa
# Abrir navegador
pyautogui.press("win")

pyautogui.write("google chrome")

pyautogui.press("enter")


# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(3)

#fazer loginhttps://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.click(x=394, y=373)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("samytu@gmail.com")

#passar para o proximo campo 
pyautogui.press("tab")
pyautogui.write("senha")
time.sleep(3)

# clicar no botão entrar
pyautogui.click(x=669, y=550)   

#passo 3 importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)   

#passo 4 cadastrar um produto

#para cada linha da minha tabela:
for linha in tabela.index:
        #codigo
        pyautogui.click(x=411, y=260)
        codigo = str (tabela.loc[linha, "codigo"])
        pyautogui.write(codigo)


        #marca
        marca = str (tabela.loc[linha, "marca"])
        pyautogui.press("tab")
        pyautogui.write(marca)
        #tipo
        tipo = str (tabela.loc[linha, "tipo"])
        pyautogui.press("tab")
        pyautogui.write(tipo)

        #categoria
        categoria = str (tabela.loc[linha, "categoria"])
        pyautogui.press("tab")
        pyautogui.write(categoria)

                        
        #preco_unitario
        preco = str (tabela.loc[linha, "preco_unitario"])
        pyautogui.press("tab")
        pyautogui.write(preco)

        #custo
        custo = str (tabela.loc[linha, "custo"]) 
        pyautogui.press("tab")
        pyautogui.write(custo)

                        
        #obs
        obs = str (tabela.loc[linha, "obs"]) 
        pyautogui.press("tab")
        if obs != "nan":
            pyautogui.write(obs)

        #enter
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.press("enter")

        pyautogui.scroll(5000)

        #passo 5 repetir o passo 4 até registrar todos os produtos