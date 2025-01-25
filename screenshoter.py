import subprocess
import cv2

import config


def screen():
    try:
        with open("screenshot.png", "wb") as f:
            subprocess.run(
                [config.get_adb_adress() + "adb", "-s", config.get_device_id(), "exec-out", "screencap", "-p"],
                stdout=f,
                check=True
            )
        return cv2.imread("screenshot.png")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")
        return None
