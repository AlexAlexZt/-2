from copy import deepcopy

# Клас прототипу
class Prototype:
    def clone(self):
        return deepcopy(self)


# Конкретний прототип
class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def display(self):
        print(f"Concrete Prototype: {self.name}")


# Використання
if __name__ == "__main__":
    # Створюємо початковий об'єкт-прототип
    prototype = ConcretePrototype("Prototype 1")
    prototype.display()

    # Клонуємо прототип
    clone = prototype.clone()
    clone.display()

    # Змінюємо назву клонованого об'єкта
    clone.set_name("Prototype 2")
    clone.display()

