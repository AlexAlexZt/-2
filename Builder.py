# Клас продукту
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None

    def __str__(self):
        return f"Part A: {self.part_a}\nPart B: {self.part_b}\nPart C: {self.part_c}"


# Абстрактний будівник
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


# Конкретний будівник
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_b = "Part B"

    def build_part_c(self):
        self.product.part_c = "Part C"

    def get_product(self):
        return self.product


# Керівник
class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


# Використання
if __name__ == "__main__":
    director = Director()

    builder = ConcreteBuilder()
    director.set_builder(builder)

    director.construct_product()
    product = builder.get_product()
    print(product)

