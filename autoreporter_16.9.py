from enum import Enum
from colorama import Fore

import pyautogui
import keyboard
import time
import threading


def click_raton():
    pyautogui.click()


class TiposDeReporte(Enum):
    ComOfensiva = (0.5, 0.4)
    ConductaMolesta = (0.5, 0.45)
    Wallhack = (0.5, 0.5)
    AimHack = (0.5, 0.55)
    OtrosChetos = (0.5, 0.6)

    def __init__(self, x, y):
        self.x = x
        self.y = y


def clicks_de_raton_instantaneos(click_count):
    threads = []
    for _ in range(click_count):
        thread = threading.Thread(target=click_raton)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def clickar_en_pantalla(multiplicador_x, multiplicador_y):
    screen_width, screen_height = pyautogui.size()

    center_x = screen_width * multiplicador_x
    center_y = screen_height * multiplicador_y

    pyautogui.moveTo(center_x, center_y)

    pyautogui.click()


def reportes_automaticos(report_count, tipo_reporte=TiposDeReporte.ConductaMolesta):
    for _ in range(report_count):
        clickar_en_pantalla(tipo_reporte.x, tipo_reporte.y)
        time.sleep(0.3)
        clickar_en_pantalla(0.60, 0.67)
        time.sleep(0.3)


def pedir_entrada_usuario():
    print(Fore.BLUE + "Seleccione el tipo de reporte:" + Fore.RESET)
    for r in TiposDeReporte:
        print(r.name)

    tipo_reporte_input = input(Fore.BLUE + "Ingrese el nombre del tipo de reporte: " + Fore.RESET).strip()

    try:
        t_reporte = TiposDeReporte[tipo_reporte_input]
    except KeyError:
        print(Fore.RED + "Tipo de reporte no válido. Usando ConductaMolesta por defecto." + Fore.RESET)
        t_reporte = TiposDeReporte.ConductaMolesta

    try:
        r_count = int(input("Ingrese la cantidad de reportes: "))
    except ValueError:
        print(Fore.RED + "Cantidad de reportes no válida. Usando 1 por defecto." + Fore.RESET)
        r_count = 1

    return r_count, t_reporte


count, tipo = pedir_entrada_usuario()
print(f"{Fore.GREEN}Configurado para hacer {count} reportes de {tipo.name}.{Fore.RESET}")
print(Fore.YELLOW + "Pon el ratón sobre el botón de reporte y pulsa 'k'." + Fore.RESET)

while True:
    if keyboard.is_pressed('k'):
        clicks_de_raton_instantaneos(count)
        time.sleep(0.5)
        reportes_automaticos(count, tipo)
        time.sleep(0.5)
    time.sleep(0.01)
