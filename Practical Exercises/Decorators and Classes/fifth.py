#  Класс учета продаж. Напишите класс SalesCounter,
#  который будет отслеживать количество продаж и суммарную выручку.
# - Создайте классовый атрибут total_sales, который будет хранить общее количество продаж.
# - Создайте статический метод calculate_total_revenue,
# который будет принимать цену товара и количество проданных единиц и возвращать суммарную выручку.
# - Создайте классовый метод reset_total_sales,
# который будет сбрасывать значение классового атрибута total_sales на ноль.
# - Оба метода должны быть вызываемыми непосредственно от класса SalesCounter,
# без необходимости создания экземпляра класса.

class SalesCounter(object):
    total_sales = 0

    @staticmethod
    def calculate_total_revenue(price, count):
        return price * count

    @classmethod
    def reset_total_sales(cls):
        cls.total_sales = 0


sales = SalesCounter
sales1 = SalesCounter
sales.total_sales = SalesCounter.calculate_total_revenue(13, 12)
print(sales.total_sales, sales1.total_sales)
sales1.total_sales = 1234
print(sales.total_sales, sales1.total_sales)
SalesCounter.reset_total_sales()
print(sales.total_sales, sales1.total_sales)
