from enum import Enum
from colorama import Fore
import pyautogui
import keyboard
import time
import threading

def mouse_click():
    """Simulates a mouse click."""
    pyautogui.click()

class ReportTypes(Enum):
    OffensiveComm = (0.5, 0.4)
    AnnoyingBehavior = (0.5, 0.45)
    Wallhack = (0.5, 0.5)
    AimHack = (0.5, 0.55)
    OtherCheats = (0.5, 0.6)

    def __init__(self, x, y):
        self.x = x
        self.y = y

def instant_mouse_clicks(click_count):
    """Simulates multiple instant mouse clicks using threading."""
    threads = [threading.Thread(target=mouse_click) for _ in range(click_count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def click_on_screen(x_multiplier, y_multiplier):
    """Moves the mouse to a position on the screen based on given multipliers and clicks."""
    screen_width, screen_height = pyautogui.size()
    target_x = screen_width * x_multiplier
    target_y = screen_height * y_multiplier
    pyautogui.moveTo(target_x, target_y)
    pyautogui.click()

def automatic_reports(report_count, report_type=ReportTypes.AnnoyingBehavior, sleep_duration=0.3):
    """Performs automatic reporting by clicking specific screen coordinates."""
    for _ in range(report_count):
        click_on_screen(report_type.x, report_type.y)
        time.sleep(sleep_duration)
        click_on_screen(0.60, 0.67)
        time.sleep(sleep_duration)

def request_user_input():
    """Requests and validates user input for the report type and count."""
    print(Fore.BLUE + "Select the type of report:" + Fore.RESET)
    for r in ReportTypes:
        print(r.name)

    report_type_input = input(Fore.BLUE + "Enter the name of the report type: " + Fore.RESET).strip()

    try:
        report_type = ReportTypes[report_type_input]
    except KeyError:
        print(Fore.RED + "Invalid report type. Using AnnoyingBehavior by default." + Fore.RESET)
        report_type = ReportTypes.AnnoyingBehavior

    try:
        report_count = int(input("Enter the number of reports: "))
    except ValueError:
        print(Fore.RED + "Invalid number of reports. Using 1 by default." + Fore.RESET)
        report_count = 1

    return report_count, report_type

if __name__ == "__main__":
    count, report_type = request_user_input()
    print(f"{Fore.GREEN}Configured to make {count} reports of {report_type.name}.{Fore.RESET}")
    print(Fore.YELLOW + "Place the mouse over the report button and press 'k' to start or 'L' to stop the script." + Fore.RESET)

    while True:
        if keyboard.is_pressed('k'):
            instant_mouse_clicks(count)
            time.sleep(0.5)
            automatic_reports(count, report_type)
            time.sleep(0.5)
        elif keyboard.is_pressed('l'):
            print(Fore.RED + "Exiting program..." + Fore.RESET)
            break
        time.sleep(0.01)
