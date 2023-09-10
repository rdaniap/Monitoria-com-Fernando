from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, som):
        self.som = som

    @abstractmethod
    def fala(self):
        pass

    def fuga(self, como):
        print(f"Ele fugiu {como}.")