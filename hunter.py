hunters_power = {
    "Джин": 85,
    "Дон": 90,
    "Сим": 88,
    "Андрей": 70,
    "Богги": 95,
    "Кастиель": 95,
    "Ребекка": 80,
    "Люцифер": 100,
    "Микаэль": 98,
    "Габриэль": 92
}

a = input()

if a in hunters_power:
    print(f"Уровень силы {a}:", hunters_power[a])
else:
    print("Такой охотник не найден в архиве.")

hunters_power = {
    "Джин": 85,
    "Дон": 90,
    "Сим": 88,
    "Андрей": 70,
    "Богги": 95,
    "Кастиель": 95,
    "Ребекка": 80,
    "Люцифер": 100,
    "Микаэль": 98,
    "Габриэль": 92
}


def count_hunters():
    print("Всего охотников в базе:", len(hunters_power))
a = input()

if a in hunters_power:
    print(f"Уровень силы {a}:", hunters_power[a])
else:
    print("Такой охотник не найден в архиве.")
count_hunters()

