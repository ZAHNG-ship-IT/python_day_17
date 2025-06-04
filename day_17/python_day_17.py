class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0##里程数
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,num):
        """打印一条指出汽车行驶里程的消息"""

        if num < self.odometer_reading:
            print("You can't roll back an odometer!")
            self.odometer_reading = self.odometer_reading
        else:
            self.odometer_reading = num







my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1)###更新的功能1
my_new_car.read_odometer()

##类的继承
class ElectricCar(Car):
####完啦，我把我要写的代码给删除了
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 调用父类构造函数
        self.battery_size = 40
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
