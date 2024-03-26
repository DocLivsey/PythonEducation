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

class CatDog(object):
    def __int__(self, cats_part, dogs_part):
        self._cats_part = cats_part
        self._dogs_part = dogs_part

    def __str__(self):
        return (f"cat`s - {self._cats_part / (self._dogs_part + self._cats_part)}%, "
                f"dog`s - {self._dogs_part / (self._dogs_part + self._cats_part)}")

    def climb_tree(self):
        return self._cats_part >= self._dogs_part

    def bark(self):
        if self._dogs_part >= self._cats_part:
            print("Woof!")
        else:
            print("Meow")

    def get_parts(self):
        return [self._cats_part, self._dogs_part]


class CosmoCatDog(CatDog):
    def __init__(self, galaxy):
        CatDog.__init__(self)
        self._galaxy = galaxy
