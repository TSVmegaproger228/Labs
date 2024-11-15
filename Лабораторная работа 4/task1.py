import json


# TODO решите задачу
def task(filename) -> float:
    with open(filename) as file:
        data = json.load(file)
        total = 0
        for numberscouple in data:
            product = numberscouple['score'] * numberscouple['weight']
            total += product
    roundtotal = round(total, 3)
    return roundtotal


book = 'input.json'
print(task(book))
