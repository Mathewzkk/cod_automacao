#obs:  baixar pyautogui: pip install pyautogui
import pyautogui 

import time

pyautogui.PAUSE = 0.7
#o comando 'pause' serve para determinar o tempo entre a execussão de cada linha do codigo
# 1 abrir sistema da empresa

#abrir o chrome
pyautogui.press('win')
#o comando 'press' serve para pressionar determinada tecla do pc
pyautogui.write('chrome')
#o comando 'write' serve para o pc digitar textos
pyautogui.press('enter')
time.sleep(2)
#o comando 'sleep' serve para determinar um tempo de espera no codigo até q ele volte a rodar

# .2 acessar o sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#pausa para carregar o site
time.sleep(5)


# 2 fazer login
pyautogui.click(x=559, y=380)
#o comando 'click' serve para o pc clicar com o mouse na coordenada da dela definida
pyautogui.write('ymathx.x@gmail.com')

pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('enter')

# 3 abrir/importar base de dados de produtos p cadastrar
#obs: baixar biblioteca para ler base de dados: pip install pandas numpy openpyxl
import pandas as pd
#obs: é possivel dar um apelido para uma biblioteca utilizando o comando 'as', ex: pandas 'as' pd

#armazenar a tabela em uma variavel
tabela = pd.read_csv('produtos.csv')

# 4 cadastrar um produto

#///preencher os campos///
#usar o comando "for" para iniciar uma estrutura de repetição
#index significa linha em uma tabela, e columns significa colunas
for linha in tabela.index:
    
    #clicar no primeiro campo
    pyautogui.click(x=556, y=256)

    #codigo
    codigo_prod = tabela.loc[linha, 'codigo'] 
    pyautogui.write(codigo_prod)
    #proximo campo
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    #proximo campo
    pyautogui.press('tab')
    
    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    #proximo campo
    pyautogui.press('tab')
    
    #categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    #proximo campo
    pyautogui.press('tab')
    
    #preço
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    #proximo campo
    pyautogui.press('tab')
    
    #custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    #proximo campo
    pyautogui.press('tab')
    
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    #proximo campo
    pyautogui.press('tab')
    
    #enviar
    pyautogui.press('enter')

# 5 repetir isso tudo ate acabar a lista
    pyautogui.scroll(2000)