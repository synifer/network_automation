# -*- coding: utf-8 -*-
"""

Функція send_show_command виконує підключення по SSH за допомогою netmiko
до пристроїв із інвентарного файлу YAML

Функція приймає два параметри:

* device - словник з парметрами підключення до пристрою
* command - команда, яку потрібно виконати

Функция строку з виводом команди.

Скрипт відправляє команду command на всі пристрої із файлу devices.yaml

Функція обробляє виключення, що генеруються при:

* помилці автентифікації на пристрої
* недоступності IP-адреси пристрою

Функція виводить повідомлення виключення на стандартний потік виводу.

"""

import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import SSHException

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except (SSHException, Exception) as error:
        print(f"Error connecting to {device['host']}: {error}")

if __name__ == "__main__":
    command = "sh ip int br"
    
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    
    for dev in devices:
        print(f"Device: {dev['host']}")
        output = send_show_command(dev, command)
        print(output)
        print("=" * 40)
