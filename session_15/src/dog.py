# Revision - Creating Classes

# All CLASS names MUST be in Pascal Case
# All Class File Names must be in snake_case
# Classes **usually** have a constructor
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says 'woof!'"


if __name__ == '__not_main__':
    fido = Dog("Fido", "Golden Retriever")
    print(fido.bark())
    assert "Fido says 'woof!'" == fido.bark()
