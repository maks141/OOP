import itertools
import os
import time

from typing import List

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        print('Ошибка: нельзя создать ещё одного робота!')  
        return None

class Robot(metaclass = Singleton):
    serial_number : str = 'АА001221-56'
    name : str = None
    place : str = None
    functions : List[str] = list()

    def __str__(self) -> str:
        funs = 'Отсутствуют' if len(self.functions) == 0 else ', '.join(self.functions)

        return f'Серийный номер: {self.serial_number}.\n' + \
                f'Имя: {self.name}.\n' + \
                f'Место пребывания: {self.place}.\n' + \
                f'Функции: {funs}.'

class RobotV(Robot):
    def __init__(self):
        self.name = 'В'
        self.place = 'Робозавод'

class RobotDecorator(Robot):
    robot : Robot
    
    def __init__(self, robot):
        self.robot = robot

class RobotVita(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self.name = 'Вита'
        self.place = 'Робошкола'
        self.functions.append('постройка домов')
        self.functions.append('постройка сараев')

class RobotVitaliy(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self.name = 'Виталий'
        self.place = 'Предприятие "ООО Кошмарик"'
        self.functions.append('добавление этажей к постройкам')
        self.functions.append('снос верхних этажей у построек')

def print_loading(text : str):
    os.system('cls')
    print(text, end='')
    it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
    for i in range(30):
        time.sleep(.3)
        print(next(it), end='', flush=True)
    os.system('cls')

def print_info(header : str, robot : Robot):
    os.system('cls')
    print(header.capitalize() + '!\n')
    print(str(robot) + '\n')
    input('Нажмите enter для продолжения...')
    os.system('cls')

if __name__ == '__main__':
    print_loading('Создание робота')
    robot = RobotV()
    print_info(header='робот создан', robot=robot)

    print_loading('Первичное обучение')
    robot = RobotVita(robot)
    print_info(header='робот прошел первичное обучение', robot=robot)

    print_loading('Практика на предприятии')
    robot = RobotVitaliy(robot)
    print_info(header='робот окончил практику на предприятии', robot=robot)