from random import randint
from time import sleep

import pyautogui as pg

# def abrir_navegador(browser):
#     pg.hotkey('win', 'r')
#     pg.write(browser)
#     pg.press('Enter')
# #x,y = pg.size()
# # pg..moveTo(x/2,y/2)
# # pg.click(30,1070)
# opcao = pg.prompt('[1]Edge \n[2]Chrome', 'Navegador')
# if opcao == '1':
#     navegador = 'msedge'
# elif opcao =='2':
#     abrir_navegador('chrome')
# else:
#     pg.alert('Programa não encontrado')

sleep(randint(1, 15))
pg.mouseInfo()
