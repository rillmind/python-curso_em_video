class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @staticmethod
    def turnOn():
        print('Estou ligado!')

    @staticmethod
    def turnOff():
        print('Desligando...')

    @staticmethod
    def march():
        print('Trocando de marcha.')

    def getBrand(self):
        print(self.brand)


car = Car('Fiat', 'Pulse', 2024)

car.getBrand()
car.turnOn()
car.march()
car.turnOff()
