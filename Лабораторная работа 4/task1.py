import json


# TODO решите задачу
def task(filename) -> float:
    with open(filename) as file:
        data = json.load(file)

    return sum([round(numberscouple['score'] * numberscouple['weight'], 3)
                for numberscouple in data])


book = 'input.json'
print(task(book))
