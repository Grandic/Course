from functions import five_operations, load_json, good_time, hide_card


def data():
    """Функция которая Реализуйте функцию, которая выводит на экран
    список из 5 последних выполненных клиентом операций"""
    for j in five_operations(load_json()):
        for i in load_json():
            if "date" in i:
                if i["date"] == j:
                    operation = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
                    print(f'{good_time(i["date"])} {i["description"]}')
                    if 'открытие' in i['description'].lower():
                        print(f'{hide_card(i["to"])}')
                    else:
                        print(f'{hide_card(i["from"])} -> {hide_card(i["to"])}')
                    print(operation)
                    print()



