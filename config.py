import json

# Загрузка конфигурации из config.json
with open("config.json", "r") as file:
    config_data = json.load(file)

# Функции для получения значений конфигурации
def get_marches():
    return config_data["max_marches"]

def get_lvl_farm():
    return config_data["lvl_farm"]

def get_lvl_sawmill():
    return config_data["lvl_sawmill"]

def get_lvl_query():
    return config_data["lvl_query"]

def get_lvl_gold():
    return config_data["lvl_gold"]

def get_lvl_niflung():
    return config_data["lvl_niflung"]

def get_adb_adress():
    return config_data["adb_adress"]

def get_device_id():
    return config_data["device_id"]
def isGatherFarm():
    return config_data["gather_farm"]
def isGatherSawmill():
    return config_data["gather_sawmill"]
def isGatherQuery():
    return config_data["gather_query"]
def isGatherGold():
    return config_data["gather_gold"]
def isHelpButton():
    return config_data["help_button"]
def isTrainGruz():
    return config_data["train_gruz"]
def emulator():
    return config_data["emulator"]