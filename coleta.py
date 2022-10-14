from ast import While
import pyautogui
import time
import keyboard
import button

def main():


  while True:
    mato1 = pyautogui.locateOnScreen("mato1.PNG", confidence=0.85)
    mato2 = pyautogui.locateOnScreen("mato2.PNG", confidence=0.85)
    mato3 = pyautogui.locateOnScreen("mato3.PNG", confidence=0.85)

    mato = mato1 or mato2 or mato3
    
    print('tentando coletar acima')
    coletar_acima(mato)


def coletar_acima(mato):
    coord_mato = pyautogui.center(mato)
    pyautogui.moveTo(coord_mato.x, (coord_mato.y - 70))
    pyautogui.click()
    time.sleep(2)
    nrota = pyautogui.locateOnScreen("nrota.PNG", confidence=0.70)
    if (nrota): 
      print('nao ha rota')
      print('tentando coletar por baixo')
      coletar_abaixo(mato)
    else:
      print('coletando por cima')
      time.sleep(6)
      pyautogui.moveTo(959, 528)
      pyautogui.moveTo(959, (528 + 90), 0.50)
      keyboard.press(button.key['F2'])
      time.sleep(3)
      return

def coletar_abaixo(mato):
    coord_mato = pyautogui.center(mato)
    pyautogui.moveTo(coord_mato.x, (coord_mato.y + 70))
    pyautogui.click()
    time.sleep(2)
    nrota = pyautogui.locateOnScreen("nrota.PNG", confidence=0.80)
    if (nrota): 
      return
    else:
      print('coletando por baixo')
      time.sleep(6)
      pyautogui.moveTo(959, 528)
      pyautogui.moveTo(959, (528 - 90), 0.50)
      keyboard.press(button.key['F2'])
      time.sleep(3)
      return

main()
