# -*- coding: utf-8 -*-

"""

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к одному устройству
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

Аргументы show и config должны передаваться только как ключевые. При передачи
этих аргументов как позиционных, должно генерироваться исключение TypeError.

В зависимости от того, какой аргумент был передан, функция вызывает разные функции
внутри. При вызове функции send_commands, всегда должен передаваться
только один из аргументов show, config. Если передаются оба аргумента, должно
генерироваться исключение ValueError.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 18.1
* config - функция send_config_commands из задания 18.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

"""

import yaml
from show_commands import send_show_command
from config_commands import send_config_commands

def send_commands(device, *, config=None, show=None):
    if show is not None and config is not None:
        raise ValueError("Only one of the arguments can be passed show/config")
    elif show is not None:
        return send_show_command(device, show)
    elif config is not None:
        return send_config_commands(device, config)
    else:
        raise ValueError("You need to pass the argument show or config")

if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]

    show_result = send_commands(r1, show="sh clock")
    print(show_result)

    config_commands = [
        "username user5 password pass5",
        "username user6 password pass6"
    ]
    config_result = send_commands(r1, config=config_commands)
    print(config_result)

