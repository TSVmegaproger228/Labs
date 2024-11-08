# TODO Напишите функцию find_common_participants
def find_common_participants(first_list, second_list, separator=','):
    first_group = set(first_list.split(separator))
    second_group = set(second_list.split(separator))
    common_group = list(first_group.intersection(second_group))
    common_group.sort()
    return common_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
