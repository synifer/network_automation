# -*- coding: utf-8 -*-
"""

Функція send_config_commands підключається до пристроїв із інвентарного файлу
і виконує перелік команд в конфігураційному режимі на основі переданих 
аргументів.

Параметри функції:

* device - словник з параметрами підключення до пристрою
* config_commands - список команд, що потрібно виконати

Функція повертає строки з результатами виконання команди.

Параметр log виконує контроль за виводом інформації на 
стандартний потік виводу про те, до якого пристрою виконується підключення.

Якщо, при виконанні команди на обладнанні виникає помилка, на екрані з'являється
запитання, чи потрібно виконувати налаштування далі.

Варіанти відповіді [y]/n:

* y - продовжити виконання наступних команд. Значення за замовчуванням
* n - не продовжувати виконання команд. Скрипт завершає роботу.

"""

import yaml
import re
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException

commands_with_errors = ["logging 0255.255.1", "logging", "i"]
correct_commands = ["interface loopback 0", "description python configuration"]
commands = commands_with_errors + correct_commands

def send_config_commands(device, config_commands, log=True):
    try:
        good_commands = {}
        bad_commands = {}
        #error_msg = 'The command "{}" failed with an error "{}" on the device {}'
        regex = "% (?P<errmsg>.+)"

        if log:
            print(f"Connecting to {device['host']}...")
        
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in config_commands:
                result = ssh.send_config_set(command, exit_config_mode=False)
                error_in_result = re.search(regex, result)
                if error_in_result:
                    err_msg = 'The command "{}" failed with an error "{}" on the device {}'
                    print(err_msg.format(command, error_in_result.group("errmsg"), ssh.host))
                    bad_commands[command] = result
                    decision = input("Continue executing the commands? [y]/n: ").strip().lower()
                    if decision not in ("y", "yes"):
                        break
                else:
                    good_commands[command] = result
            ssh.exit_config_mode()
        
        return good_commands, bad_commands

    except (NetMikoTimeoutException, NetMikoAuthenticationException) as error:
        return f"Error connecting to {device['host']}: {error}"

if __name__ == "__main__":

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        #print(f"Device: {dev['host']}")
        good, bad = send_config_commands(dev, commands)
        print(f"Correct commands on {dev['host']}:\n{good}")
        print(f"Incorrect commands on {dev['host']}:\n{good}")
        print("=" * 40)

