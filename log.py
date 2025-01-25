import datetime

def log_action(message):
    """
    Логирует сообщение с текущим временем.

    :param message: Сообщение для записи в лог.
    """
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"[{current_time}] {message}")  # Вывод в консоль