import sys  # Нужно импортировать прежде чем задавать функцию


def moon_weight():  # Задаю функцию
    index = 0.165  # Задаю переменную
    print('What are your start weight?')
    start_weight = int(sys.stdin.readline())
    print('How much is delta weight?')
    delta_weight = int(sys.stdin.readline())
    print('How long thise will be heppen?')
    year_count = int(sys.stdin.readline())
    year_count = year_count + 1
    for year in range(1, year_count):
        weight = start_weight + delta_weight
        finish_weight = weight * index
        start_weight = weight
        print('Через %s год мой вес на луне будет %s кг' % (year, finish_weight))


moon_weight()  # На вход только целые числа
