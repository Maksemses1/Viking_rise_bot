from itertools import count
from multiprocessing import Process
from time import sleep, time
import os
import sys

import cv2

import config
import screenshoter
import templates
from log import log_action
import main_commands
import global_command

count = 0
def reboot():
    """
    Перезапуск программы.
    """
    log_action("Перезапуск программы...")
    python = sys.executable  # Путь к интерпретатору Python
    os.execl(python, python, *sys.argv)  # Полный перезапуск программы

def reboot_timer():
    """
    Таймер для перезапуска программы каждые 60 минут.
    """
    while True:
        sleep(30)  # Ждем 1 час
        reboot()     # Запускаем перезапуск программы

def wait_for_march(interval=10):
    while True:
        screen = screenshoter.screen()
        if screen is None:
            log_action("Ошибка захвата экрана")
            continue  # Конечно. А как я по твоему 10 лвл апаю
            # до 600 кристаллов дохожу когда покупаю

        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        marches = main_commands.count_reminds_marches(screen_gray)
        main_commands.ok_button(screen_gray)
        if marches != 0:
            if main_commands.goWorld(Tap="c"):
                log_action("Свободных маршей: " + str(marches))
                return True
            else:
                log_action("непредвиденная ошибка \n Пробую исправить")
                try_fix()
                return False

        log_action("Все отряды заняты, количество сборов: " + str(count))
        idle()
        sleep(interval)


def try_fix():
    """
    Попытка исправить ошибки.
    """
    main_commands.back()
    sleep(10)
    if main_commands.goWorld(Tap="c"):
        main_commands.wait_for_and_click(templates.world_button(), main_commands.goWorld)
        main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
        sleep(3)
        log_action("Попытка фикса прошла успешно 1")
    if main_commands.goHome(Tap="c"):
        main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
        log_action("Попытка фикса прошла успешно 2")

def idle():
    """
    Выполнение фоновых задач.
    """
    if config.isHelpButton():
        if main_commands.help_button():
            log_action("Помощь прожата")
    if config.isTrainGruz():
        global_command.train_gruz_t1()

def main_program():
    """
    Основной цикл программы.
    """
    count = 0
    while True:
        ismarches = wait_for_march()
        if config.isGatherFarm() and ismarches:
            global_command.gather_farm()
            sleep(1)
            count += 1
            ismarches = False
        if not ismarches:
            ismarches = wait_for_march()
        if config.isGatherSawmill() and ismarches:
            global_command.gather_sawmill()
            sleep(1)
            count += 1
            ismarches = False
        if not ismarches:
            ismarches = wait_for_march()
        if config.isGatherQuery() and ismarches:
            global_command.gather_query()
            sleep(1)
            count += 1
            ismarches = False
        if not ismarches:
            ismarches = wait_for_march()
        if config.isGatherGold() and ismarches:
            global_command.gather_gold()
            sleep(1)
            count += 1
            ismarches = False
        if not ismarches:
            ismarches = wait_for_march()

if __name__ == "__main__":
    count = 0
    # Запуск таймера в отдельном процессе
    log_action("Начинаю программу")
    timer_process = Process(target=reboot_timer, daemon=True)
    timer_process.start()

    # Запуск основного кода программы
    main_program()
