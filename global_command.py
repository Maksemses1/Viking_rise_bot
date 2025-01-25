from time import sleep

import main_commands
import config
import time
import templates
from log import log_action

def train_gruz_t1():
    if not main_commands.gruz_t1_train_ico():
        main_commands.gruz_build()
        sleep(0.5)
        main_commands.gruz_build()
        main_commands.wait_for_and_click(templates.train_gruz_button(), main_commands.train_gruz_button)
        main_commands.wait_for_and_click(templates.gruz_t1_button(), main_commands.gruz_t1_button)
        main_commands.wait_for_and_click(templates.train_button(), main_commands.train_button)
        if main_commands.wait_for_use_button_train():
            main_commands.use_button()
            main_commands.wait_for_and_click(templates.train_button(), main_commands.train_button)
        sleep(1)
        if not main_commands.goWorld(Tap="abc") and not main_commands.goHome(Tap="abc"):
            main_commands.back()
        sleep(2)
        main_commands.wait_for_world_button()
    else:
        log_action("Грузчики уже тренируются")
def gather_farm():
    log_action("Отправка отряда на ферму")
    main_commands.wait_for_and_click(templates.world_button(), main_commands.goWorld)
    main_commands.wait_for_and_click(templates.find_button(), main_commands.find_button)
    main_commands.wait_for_and_click(templates.farm_button(), main_commands.farm_button)
    lvl = config.get_lvl_farm()
    main_commands.minus_button(9)
    main_commands.plus_button(lvl)
    main_commands.wait_for_and_click(templates.search_button(), main_commands.search_button)
    main_commands.wait_for_and_click(templates.gather_button(), main_commands.gather_button)
    main_commands.wait_for_and_click(templates.create_button(), main_commands.create_button)
    main_commands.wait_for_and_click(templates.march_button(), main_commands.march_button)
    sleep(0.5)
    main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
    sleep(0.5)
    log_action("Отправка произошла успешно")
def gather_query():
    log_action("Отправка отряда на карьер")
    main_commands.wait_for_and_click(templates.world_button(), main_commands.goWorld)
    main_commands.wait_for_and_click(templates.find_button(), main_commands.find_button)
    main_commands.wait_for_and_click(templates.query_button(), main_commands.query_button)
    lvl = config.get_lvl_query()
    main_commands.minus_button(9)
    main_commands.plus_button(lvl)
    main_commands.wait_for_and_click(templates.search_button(), main_commands.search_button)
    main_commands.wait_for_and_click(templates.gather_button(), main_commands.gather_button)
    main_commands.wait_for_and_click(templates.create_button(), main_commands.create_button)
    main_commands.wait_for_and_click(templates.march_button(), main_commands.march_button)
    sleep(0.5)
    main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
    sleep(0.5)
    log_action("Отправка произошла успешно")
def gather_sawmill():
    log_action("Отправка отряда на лесопилку")
    main_commands.wait_for_and_click(templates.world_button(), main_commands.goWorld)
    main_commands.wait_for_and_click(templates.find_button(), main_commands.find_button)
    main_commands.wait_for_and_click(templates.sawmill_button(), main_commands.sawmill_button)
    lvl = config.get_lvl_sawmill()
    main_commands.minus_button(9)
    main_commands.plus_button(lvl)
    main_commands.wait_for_and_click(templates.search_button(), main_commands.search_button)
    main_commands.wait_for_and_click(templates.gather_button(), main_commands.gather_button)
    main_commands.wait_for_and_click(templates.create_button(), main_commands.create_button)
    main_commands.wait_for_and_click(templates.march_button(), main_commands.march_button)
    main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
    log_action("Отправка произошла успешно")
def gather_gold():
    log_action("Отправка отряда на золото")
    main_commands.wait_for_and_click(templates.world_button(), main_commands.goWorld)
    main_commands.wait_for_and_click(templates.find_button(), main_commands.find_button)
    main_commands.wait_for_and_click(templates.gold_button(), main_commands.gold_button)
    lvl = config.get_lvl_gold()
    main_commands.minus_button(9)
    main_commands.plus_button(lvl)
    main_commands.wait_for_and_click(templates.search_button(), main_commands.search_button)
    main_commands.wait_for_and_click(templates.gather_button(), main_commands.gather_button)
    main_commands.wait_for_and_click(templates.create_button(), main_commands.create_button)
    main_commands.wait_for_and_click(templates.march_button(), main_commands.march_button)
    main_commands.wait_for_and_click(templates.home_button(), main_commands.goHome)
    log_action("Отправка произошла успешно")
