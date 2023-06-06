from abc import ABC, abstractmethod

# Абстрактний клас продукту
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Конкретний продукт A
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

# Конкретний продукт B
class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

# Абстрактний клас фабрики
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

# Конкретна фабрика для продукту A
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# Конкретна фабрика для продукту B
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Клієнтський код
def client_code(creator: Creator):
    print(creator.some_operation())

if __name__ == "__main__":
    # Використання фабрики для створення продукту A
    client_code(ConcreteCreatorA())

    # Використання фабрики для створення продукту B
    client_code(ConcreteCreatorB())

