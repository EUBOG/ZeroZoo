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


def load_zoo(zoo_file):                   # загрузка данных из файла
    with open(zoo_file, 'r') as f:
        data = json.load(f)

    animals = [Animal(**animal) for animal in data['animals']]
    employees = [Employee(**employee) for employee in data['employees']]

    return animals, employees

zoo = Zoo("Настоящий зоопарк") # создаем зоопарк

# Создаем животных и добавляем их в список
Crow = Bird("Bird", "Ворона Фёкла", "Кар", "Зёрнышки")        # это ворона Фёкла
Cow = Mammal("Mammal", "Корова Зорька", "Му", "Силос")      # это корова Зорька
Cayman = Reptile("Reptile", "Кайман Василий", "Хрр","Рыба") # это кайман Василий
Peacock = Bird("Bird", "Павлин Павел", "Аааа", "Зёрнышки")
Ostrich = Bird("Bird", "Страус Стёпа", "Эгегей", "Вершки и Корешки")
Lion = Mammal("Mammal", "Лев Лёва", "Рррр","Зебра")
Tiger = Mammal("Mammal", "Тигр Киса", "Мяу", "Антилопа")
Boa = Reptile("Reptile", "Удав Каа", "Шшш", "Бандерлоги")
Lizard = Reptile("Reptile","Ящер Яша", "Ик", "Насекомые")
birds = [Crow, Peacock, Ostrich]
mammals = [Cow, Lion, Tiger]
reptiles = [Cayman, Boa, Lizard]
animals = [Crow, Cow, Cayman, Peacock, Ostrich, Lion, Tiger, Boa, Lizard]


# добавляем список животных в зоопарк
for animal in animals:
    zoo.add_animal()

# Создаем новых сотрудников и добавляем их в список
Veter1 = Veterinarian("Veterinarian", "Ветеринар Джек", 45) # это ветеринар Джек
Veter2 = Veterinarian("Veterinarian", "Ветеринар Саша", 32)
Veter3 = Veterinarian("Veterinarian", "Ветеринар Саня", 33)
Veter4 = Veterinarian("Veterinarian", "Ветеринар Санёк", 34)
Keeper1 = ZooKeeper("ZooKeeper", "Смотритель Джон", 55)  # это смотритель Джон
Keeper2 = ZooKeeper("ZooKeeper", "Смотритель Коля", 35)
Keeper3 = ZooKeeper("ZooKeeper", "Смотритель Колян", 36)
Keeper4 = ZooKeeper("ZooKeeper", "Смотритель Николай", 37)
employees = [Veter1, Veter2, Veter3, Veter4, Keeper1, Keeper2, Keeper3, Keeper4]

for employee in employees:
    zoo.add_employee()

# Показываем животных и сотрудников
zoo.show_animals()
zoo.show_employees()

animal_sounds(animals)                     # запуск функции описания звуков
animal_eats(animals)                       # запуск функции описания еды
work(employees)                            # запуск функции описания работы сотрудников

save_zoo('zoo_data.json', animals, employees)