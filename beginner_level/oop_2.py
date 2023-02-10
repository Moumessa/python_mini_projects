class Car:
    def __init__(self, make, model, year,color) -> None:
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    def stop(self):
        print('---car stopping')

    def move(self):
        print("---car moving")

c=Car("Renault", 'Clio 4', 2022, "red")

print(c.color)