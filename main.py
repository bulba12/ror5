class Car:
    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, increase):
        self.speed += increase
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        print(f"{self.make} {self.model} розганяється до {self.speed} км/год")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.make} {self.model} сповільнюється до {self.speed} км/год")

class Driver:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def drive(self, car):
        print(f"{self.name} починає керувати {car.make} {car.model}")
        car.accelerate(self.experience * 10)

class Track:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def start_race(self, driver, car):
        print(f"Гонка починається на автодромі {self.name} ({self.length} км)")
        driver.drive(car)
        car.accelerate(20)
        car.brake(10)
        print(f"Гонка завершена на {car.speed} км/год")


car1 = Car("Toyota", "Supra", 250)
driver1 = Driver("Іван", 5)
track1 = Track("Silverstone", 5.8)

track1.start_race(driver1, car1)
