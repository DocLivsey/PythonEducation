# Класс «КотоПес» (CatDog)
#
# Экземпляр класса инициализируется двумя целыми числами: первое число относится к кошке, второе - к собаке.
#
# Класс реализует следующие методы:
# climb_tree() - может лазить по деревьям - возвращает True, если часть кошки больше или равна части собаки.
#
# bark() - лает - если часть собаки больше или равна части кошки,
# возвращает строку "Woof!", иначе возвращает строку "Meow!".
#
# eat(food, value) - есть - может есть только рыбу (fish) или мясо (meat).
# Если съедает рыбу, то из части собаки вычитается количество съеденного, кошке добавляется,
# иначе наоборот: у кошки вычитается, а собаке добавляется.
# Нельзя превысить значение 100 или уменьшиться ниже 0.
#
# get_parts() - возвращает список значений [часть кошки, часть собаки].
#
# Создать класс-наследник от класса «КотоПес», например, «Космический КотоПес».
#
# Обязательно использование конструктора, декораторов и метода __str__.

def validate_input(func):
    def wrapper(*args, **kwargs):
        if type(args[1]) is int or type(args[1]) is float:
            if args[1] < 0 or args[1] > 100:
                raise ValueError("Нельзя превысить значение 100 или уменьшиться ниже 0")
        if type(args[2]) is int or type(args[2]) is float:
            if args[2] < 0 or args[2] > 100:
                raise ValueError("Нельзя превысить значение 100 или уменьшиться ниже 0")
        return func(*args, **kwargs)

    return wrapper


class CatDog(object):
    _cats_part: float
    _dogs_part: float

    @validate_input
    def __init__(self, cats_part, dogs_part):
        self._cats_part = float(cats_part)
        self._dogs_part = float(dogs_part)

    def __str__(self):
        return (f"cat - {self._cats_part / (self._dogs_part + self._cats_part) * 100}%, "
                f"dog - {self._dogs_part / (self._dogs_part + self._cats_part) * 100}%")

    def climb_tree(self):
        return self._cats_part >= self._dogs_part

    def bark(self):
        if self._dogs_part >= self._cats_part:
            print("Woof!")
        else:
            print("Meow")

    def get_parts(self):
        return [self._cats_part, self._dogs_part]

    @validate_input
    def eat(self, food, value):
        if food == "meat":
            self._dogs_part = self._dogs_part + value if value + self._dogs_part < 100 else 100
            self._cats_part = self._cats_part - value if self._cats_part - value > 0 else 0
        elif food == "fish":
            self._cats_part = self._cats_part + value if value + self._cats_part < 100 else 100
            self._dogs_part = self._dogs_part - value if self._dogs_part - value > 0 else 0


class CosmoCatDog(CatDog):
    def __init__(self, cats_part, dogs_part, galaxy):
        CatDog.__init__(self, cats_part, dogs_part)
        self._galaxy = galaxy

    def __str__(self):
        return (f"cat - {self._cats_part / (self._dogs_part + self._cats_part) * 100}%, "
                f"dog - {self._dogs_part / (self._dogs_part + self._cats_part) * 100}%, "
                f"galaxy - {self._galaxy}")

    def get_galaxy(self):
        return self._galaxy


c = CatDog(12, 13)
print(c, c.get_parts())
c.eat("meat", 100)
print(c, c.get_parts())

cosmo_c = CosmoCatDog(12, 13, "milky way")
print(cosmo_c, c.get_parts())
