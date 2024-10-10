# Домашнее задание по теме "Генераторы"
# Задача: Напишите функцию-генератор all_variants(text),
# которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

def all_variants(text):
    for a in text:
        yield a

    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            yield text[i:j + 1]


a = all_variants("abc")
for i in a:
    print(i)
