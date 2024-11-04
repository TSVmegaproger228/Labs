# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    first_group = set(first_group.split(separator))
    second_group = set(second_group.split(separator))
    general_group = list(first_group.intersection(second_group))
    general_group.sort()
    return general_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
