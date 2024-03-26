# Конвертер расстояний.  Напишите класс DistanceConverter,
# который будет преобразовывать расстояния из одной единицы измерения в другую.
# - Создайте статический метод convert_meters_to_feet,
# который будет принимать количество метров и возвращать соответствующее количество футов.
# - Создайте классовый метод convert_feet_to_meters,
# который будет принимать количество футов и возвращать соответствующее количество метров.
# - Оба метода должны быть вызываемыми непосредственно от класса DistanceConverter,
# без необходимости создания экземпляра класса.

class DistanceConverter(object):
    @staticmethod
    def convert_meters_to_feet(distance):
        return distance * 3.28084

    @staticmethod
    def convert_feet_to_meters(distance):
        return distance / 3.28084


print(DistanceConverter.convert_meters_to_feet(float(input("input meters amount = "))), "feet")
print(DistanceConverter.convert_feet_to_meters(float(input("input feet amount = "))), "meters")
