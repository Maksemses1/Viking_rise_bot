from time import sleep

import config
import tapper
import screenshoter
import cv2
import templates
import os
import time

from log import log_action
from templates import search_button

def wait_for_and_click(template, action_func, timeout=10, interval=0.5, curacity=0.8, log=True):
    start_time = time.time()
    while time.time() - start_time < timeout:
        found, max_loc = analise(template, cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY), curacity)
        if found:
            action_func()  # Вызываем переданную функцию действия
            sleep(0.5)
            return True
        time.sleep(interval)  # Ждём перед следующей проверкой
    if log: print(f"Элемент с шаблоном не найден за {timeout} секунд.")
    return False

def wait_for_use_button_train(timeout=10, interval=0.5, curacity=0.8):
    start_time = time.time()
    while time.time() - start_time < timeout:
        found, max_loc = analise(templates.use_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY), curacity)
        if found:
            log_action("Кнопка использовать найдена")
            return True
        time.sleep(interval)  # Ждём перед следующей проверкой
    print("Ресурсов на тренировку достаточно")
    return False
def wait_for_world_button(timeout=10, interval=0.5, curacity=0.8):
    start_time = time.time()
    while time.time() - start_time < timeout:
        found, max_loc = analise(templates.use_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY), curacity)
        if found:
            return True
        time.sleep(interval)  # Ждём перед следующей проверкой
    return False


def analise(picture, screen, curacity=0.8):
    result = cv2.matchTemplate(screen, picture, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Возвращаем результат и координаты, если совпадение найдено
    if max_val > curacity:
        return True, max_loc
    else:
        return False, None
def search_button():
    log_action("поиск кнопки найту плитку")
    found, max_loc = analise(templates.search_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def march_button():
    log_action("поиск кнопки отправки отряда")
    found, max_loc = analise(templates.march_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def create_button():
    log_action("поиск кнопки создать отряд")
    found, max_loc = analise(templates.create_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    found2, max_loc2 = analise(templates.create_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        log_action("кнопка найдена и нажата")
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
    elif found2 and max_loc2 is not None:
        log_action("кнопка найдена и нажата")
        tapper.tap(max_loc2[0], max_loc2[1])
def gather_button():
    log_action("поиск кнопки собрать ресурсы")
    found, max_loc = analise(templates.gather_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def minus_button(range_ = 1):
    log_action("поиск кнопки уменьший уровень")
    found, max_loc = analise(templates.minus_button(),cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY), curacity=0.8)
    if found and max_loc is not None:
        for i in range(range_):
            tapper.tap(max_loc[0]+1, max_loc[1]+1)
            sleep(0.02)
    log_action("кнопка найдена и нажата " + str(range_) + " раз" )
def marsch_button():
    log_action("поиск кнопки отправить отряд ")
    found, max_loc = analise(templates.march_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def plus_button(range_ = 1):
    range_ = range_ - 1
    log_action("поиск кнопки плюс уровня")
    found, max_loc = analise(templates.plus_button(),cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY), curacity=0.8)
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        for i in range(range_):
            tapper.tap(max_loc[0]+1, max_loc[1]+1)
            sleep(0.1)
    log_action("кнопка найдена и нажата " + str(range_) + " раз")

def goWorld(Tap="tap"):
    log_action("поиск кнопки выйти в мир")
    found, max_loc = analise(templates.world_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        if Tap == "tap":
            tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def goHome(Tap="tap"):
    log_action("поиск кнопки вернуться на базу")
    found, max_loc = analise(templates.home_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        if Tap == "tap":
            tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def find_button():
    log_action("поиск кнопки поиск")
    found, max_loc = analise(templates.find_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def farm_button():
    log_action("поиск кнопки выбрать ферму")
    found, max_loc = analise(templates.farm_button(),cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def sawmill_button():
    log_action("поиск кнопки выбрать лесопилку")
    found, max_loc = analise(templates.sawmill_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def query_button():
    log_action("поиск кнопки карьер")
    found, max_loc = analise(templates.query_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def gold_button():
    log_action("поиск кнопки выбрать золото")
    found, max_loc = analise(templates.gold_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
def count_reminds_marches(screen):
    log_action("поиск количества маршей")
    found_one, max_loc = analise(templates.oneMarchesAlready(), screen, 0.9)
    found_two, max_loc = analise(templates.twoMarchesAlready(), screen, 0.9)
    found_theree, max_loc = analise(templates.thereeMarchesAlready(), screen, 0.9)
    found_four, max_loc = analise(templates.fourMarchesAlready(), screen, 0.9)
    if found_one:
        log_action("1 марш занят")
        return config.get_marches() - 1;
    elif found_two:
        log_action("2 марша занято")
        return config.get_marches() - 2;
    elif found_theree:
        log_action("3 марша занято")
        return config.get_marches() - 3;
    elif found_four:
        log_action("4 марша занято")
        return config.get_marches() - 4;
    else:
        log_action("марши все свободные либо не найдены")
        return config.get_marches();
def back():
    os.system("\"" + config.get_adb_adress() + "\" -s" + config.get_device_id() + " shell input keyevent 4")
def niflung_button():
    found, max_loc = analise(templates.niflung_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
def help_button():
    log_action("поиск кнопки помощи")
    found, max_loc = analise(templates.help_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def gruz_build():
    log_action("нажимаю на казармы грузчиков")
    tapper.tap(320, 180)
def train_gruz_button():
    log_action("поиск кнопки тренировки")
    found, max_loc = analise(templates.train_gruz_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def gruz_t1_button():
    log_action("поиск кнопки Т1 грузчиков")
    found, max_loc = analise(templates.gruz_t1_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def train_button():
    log_action("поиск кнопки тренировки")
    found, max_loc = analise(templates.train_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def use_button():
    log_action("поиск кнопки использовать")
    found, max_loc = analise(templates.use_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False
def gruz_t1_train_ico():
    log_action("поиск иконки грузчиков")
    screen = cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY)
    found, max_loc = analise(templates.gruz_t1_train_ico(), screen)
    if found and max_loc is not None:
        log_action("Иконка грузчиков найдена")
        return True
    found, max_loc = analise(templates.gruz_t1_train_ico_2(), screen)
    if found and max_loc is not None:
        log_action("Иконка грузчиков найдена")
        return True
    return False
def ok_button(screen):
    found, max_loc = analise(templates.ok_button(), screen)
    if found and max_loc is not None:
        log_action("нашел баг и исправил")
        tapper.tap(max_loc[0]+3, max_loc[1]+3)
        return True
    return False
def viking_rise_ico():
    found, max_loc = analise(templates.viking_rise_ico(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        log_action("Включаю игру")
        tapper.tap(max_loc[0], max_loc[1])
        return True
    return False
def exit_button():
    log_action("поиск кнопки выхода покупки")
    found, max_loc = analise(templates.help_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(627, 71)
        tapper.tap(627, 71)
        log_action("кнопка найдена и нажата")
        return True
    found, max_loc = analise(templates.exit_button_2(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        tapper.tap(627, 71)
        tapper.tap(627, 71)
        log_action("кнопка найдена и нажата")
        return True
    return False
def no_load_rss_button():
    log_action("поиск кнопки выхода покупки")
    found, max_loc = analise(templates.not_found_rss_button(), cv2.cvtColor(screenshoter.screen(), cv2.COLOR_BGR2GRAY))
    if found and max_loc is not None:
        # Если кнопка найдена, совершаем клик по координатам
        tapper.tap(max_loc[0], max_loc[1])
        log_action("кнопка найдена и нажата")
        return True
    return False