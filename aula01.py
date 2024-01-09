#instalar biblioteca pyautogui
#pip install pyautogui
import pyautogui
import time



pyautogui.PAUSE = 1
#pressionar a tecla Windows
pyautogui.press("Win")
#digitar Opera
pyautogui.write("Opera")
#pressionar a tecla Enter
pyautogui.press("Enter")
#entrar no site de login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
#pressionar Enter no Opera
pyautogui.press("Enter")

time.sleep(2)

#clicar no campo para digitar o e-mail
pyautogui.click(x=825, y=355)
#colocar o e-mail
pyautogui.write("pythonimpressionador@gmail.com")
#pular pro campo de senha com o Tab
pyautogui.press("Tab")
#colocar a senha
pyautogui.write("1234567")
#pressionar Enter
pyautogui.press("Enter")
time.sleep(3)

#instalar 3 bibliotecas python
#pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)
pyautogui.click(x=806, y=238)

#PASSO 4, CADASTRAR UM PRODUTO
for linha in tabela.index: #.index = referente às linhas
    pyautogui.click(x=806, y=238) #clica novamente no primeiro campo
    #codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #pega o dado da coluna 'codigo' da linha referente ao loop da vez(ex: 1,2,3...)
    pyautogui.press("Tab")
    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("Tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("Tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("Tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("Tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("Tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    #enviar produto
    pyautogui.press("Tab")
    pyautogui.press("Enter")


    #voltar a página pro topo
    pyautogui.scroll(1000)







