import json


def load_json():
    """Функция получает расположение Json-файла и преобразует его в словарь"""
    with open("operations.json", "r", encoding="UTF=8") as read_file:
        operations = json.load(read_file)
        return operations


all_operations = load_json()


def five_operations():
    operations_with_date = []
    correct_operations = []
    date_list = []
    for i in all_operations:
        if "date" in i:
            operations_with_date.append(i)
    # print(operations_with_date)
    for j in operations_with_date:
        if j['state'] == 'EXECUTED':
            correct_operations.append(j)
    # print(correct_operations)
    for k in correct_operations:
        date_list.append(k["date"])
    date_list.sort(reverse=True)
    return date_list[:5]
