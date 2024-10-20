numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sumofnumbs = sum(numbers[:4] + numbers[5:])
length = len(numbers)
midd = sumofnumbs / length
numbers[4] = midd

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
