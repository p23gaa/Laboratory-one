numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
newnumbers = numbers[:4]+numbers[5:]
sredznach = sum(newnumbers)/len(numbers)
numbers[4] = sredznach
print("Измененный список:", numbers)

