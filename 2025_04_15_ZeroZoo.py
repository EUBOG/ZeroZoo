import json

class Animal(): # вводим класс животных
    def __init__(self, classis, name, sound, meal):
        self.classis = classis
        self.name = name
        self.sound = sound
        self.meal = meal

    def make_sound(self): # вводим метод звуков
        pass

    def eat(self): # вводим метод еды
        pass

    def to_dict(self):  # вводим метод to_dict
        return {
            'classis': self.classis,
            'name': self.name,
            'sound': self.sound,
            'meal': self.meal
        }

class Bird(Animal):        # вводим класс птиц

    def make_sound(self):  # описываем звук птицы
        print(f"Звук, который издает", self.name, "-", self.sound)

    def eat(self):  # описываем еду птицы
        print(f"Еда, которую ест", self.name, "-", self.meal)

class Mammal(Animal):      # вводим класс млекопитающих

    def make_sound(self):  # описываем звук млекопитающего
        print(f"Звук, который издает", self.name, "-", self.sound)

    def eat(self):  # описываем еду млекопитающего
        print(f"Еда, которую ест", self.name, "-", self.meal)

class Reptile(Animal):     # вводим класс рептилий

    def make_sound(self):  # описываем звук рептилий
        print(f"Звук, который издает", self.name, "-", self.sound)

    def eat(self):  # описываем еду рептилий
        print(f"Еда, которую ест", self.name, "-", self.meal)

class Employee():
    def __init__(self, proff, name, age):
        self.proff = proff
        self.name = name
        self.age = age

    def work(self):
        pass

    def to_dict(self):  # вводим метод to_dict
        return {
            'proff': self.proff,
            'name': self.name,
            'age': self.age,
        }

class ZooKeeper(Employee):

    def feed_animal(self):
        print(f"Работа, которую выполняет", self.proff, self.name, "- кормит животных")

class Veterinarian(Employee):

    def heal_animal(self):
        print(f"Работа, которую выполняет", self.proff, self.name, "- лечит животных")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = [] # список животных
        self.employees = [] # список сотрудников

    def add_animal(self):
        self.animals.append(animal)

    def add_employee(self):
        self.employees.append(employee)

    def show_animals(self):
        print("Перечень животных зоопарка:")
        for animal in self.animals:
            print(f"{animal.classis} {animal.name} (Class: {animal.__class__.__name__})")

    def show_employees(self):
        print("Перечень сотрудников зоопарка:")
        for employee in self.employees:
            print(f"{employee.proff} {employee.name} (Class: {employee.__class__.__name__})")

def animal_sounds(animals): # функция, вызывающая описание звука для животных из списка animals
        for animal in animals:
            animal.make_sound()

def animal_eats(animals):  # функция, вызывающая описание еды животных из списка animals
    for animal in animals:
        animal.eat()

def work(employees):
    for employee in employees:
        if isinstance(employee, Veterinarian):
            employee.heal_animal()
        elif isinstance(employee, ZooKeeper):
            employee.feed_animal()
        else: print("Такой сотрудни не найден")

def save_zoo(zoo_file, animals, employees): # сохранение данных в файл
    data = {
        'animals': [animal.to_dict() for animal in animals],
        'employees': [employee.to_dict() for employee in employees]
    }
    with open(zoo_file, 'w') as f:
        json.dump(data, f, indent=5)


def load_zoo(zoo_file):  # загрузка данных из файла
    with open(zoo_file, 'r') as f:
        data = json.load(f)

    # Создание объектов животных по данным, полученным из файла
    for animal_data in data['animals']:
        if animal_data['classis'] == 'Bird':  # Пример условия для создания объекта
            animal = Bird(**animal_data)
        elif animal_data['classis'] == 'Mammal':
            animal = Mammal(**animal_data)
        else:
            animal = Reptile(**animal_data)  # Предположим, что все остальные - рептилии
        animals.append(animal)

    # Создание объектов сотрудников по данным, полученным из файла
    for employee_data in data['employees']:
        if employee_data.get('proff') == 'Veterinarian':
            employee = Veterinarian(**employee_data)
        else:
            employee = ZooKeeper(**employee_data)  # Предположим, что остальные - смотрители
        employees.append(employee)

    return animals, employees

zoo = Zoo("Настоящий зоопарк") # создаем зоопарк
animals = []
employees = []

loaded_animals, loaded_employees = load_zoo('zoo_data.json') # загружаем в зоопарк животных и сотрудников из файла

# добавляем список животных в зоопарк
for animal in animals:
    zoo.add_animal()

# добавляем спсок сотрудников в зоопарк
for employee in employees:
    zoo.add_employee()

# Показываем животных и сотрудников
zoo.show_animals()
zoo.show_employees()

animal_sounds(animals)                     # запуск функции описания звуков
animal_eats(animals)                       # запуск функции описания еды
work(employees)                            # запуск функции описания работы сотрудников