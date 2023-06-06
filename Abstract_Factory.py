from abc import ABC, abstractmethod

# Абстрактні класи продуктів
class AbstractProductA(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретні класи продуктів
class ConcreteProductA1(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA1 operation"

class ConcreteProductA2(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA2 operation"

class ConcreteProductB1(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB1 operation"

class ConcreteProductB2(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB2 operation"

# Абстрактна фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Конкретні фабрики
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Клієнтський код
def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(product_a.operation())
    print(product_b.operation())

# Використання
if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    client_code(factory1)
    
    factory2 = ConcreteFactory2()
    client_code(factory2)

