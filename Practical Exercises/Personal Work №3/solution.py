# В школу бальных танцев записались n учеников — мальчиков и девочек.
# Руководитель школы построил их в один ряд,
# и хочет отобрать из них для первого занятия группу стоящих подряд учеников,
# в которой количество мальчиков и девочек одинаково.
# Сколько вариантов выбора есть у профессора?

# В первой строке файла задано число n
# Во второй строке задается описание построенного ряда из мальчиков и девочек —
# строка из nn символов a и b (символ a соответствует девочке, а символ b — мальчику).
# Найти количество вариантов выбора требуемой группы

# Например:
# 8
# abbababa
# 13

with open("input.txt") as input_file:
    text = input_file.read().split('\n')
    count = int(text[0])
    pupils = text[1]
    pairs = {}
    for i in range(2, len(pupils) + 1, 2):
        for j in range(len(pupils) - i + 1):
            if pupils[j:i+j].count('a') == pupils[j:i+j].count('b'):
                if pupils[j:i+j] not in pairs.keys():
                    pairs[pupils[j:i+j]] = 1
                else:
                    pairs[pupils[j:i + j]] += 1
    print(sum(pairs.values()))
input_file.close()