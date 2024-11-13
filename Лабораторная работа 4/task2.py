# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Десериализация файла из 'input.csv'"""
    with open(INPUT_FILENAME, 'r') as csvfile:
        dictionary = [row for row in csv.DictReader(csvfile)]
    """Cериализация файла в 'output.json'"""
    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        json.dump(dictionary, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
