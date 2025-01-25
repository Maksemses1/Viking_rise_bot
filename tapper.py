import subprocess

import config


def tap(x, y):
    #print("tap in " + str(x) + " " + str(y))
    subprocess.run(
        [config.get_adb_adress() + "adb", "-s", config.get_device_id(), "exec-out", "input", "tap", str(x), str(y)],
        check=True
    )
