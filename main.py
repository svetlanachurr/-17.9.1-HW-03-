def user_input():
    correct = False
    while not correct:
        raw_input = input("Введите последовательность чисел через пробел: ")

        raw_input = raw_input.split()

        try:
            numbers = list(map(int, raw_input))
        except:
            correct = False
            print("Введеная последовательность не является корректной")
            continue

        correct = True

    correct = False
    while not correct:
        raw_input = input("Введите число для проверки: ")
        try:

            number = int(raw_input)
        except:
            correct = False
            print("Введенное число не корректно")
            continue
        correct = True

    return numbers, number


def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def find_place(number, array, left, right):
    """
    Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
    а следующий за ним больше или равен этому числу.
    """
    if number > array[-1]:
        return None
    if number <= array[0]:
        return None

    center = (right - left) // 2
    if array[center] < number <= array[center + 1]:
        return center
    elif number > array[center]:
        return find_place(number, array, center, right)
    else:
        return find_place(number, array, left, center)


numbers, number = user_input()

sorted_numbers = sort(numbers)
print("Список после сортировки:", sorted_numbers)
place = find_place(number, sorted_numbers, 0, len(numbers))
if place is not None:
    print("Номер позиции числа:", place)
else:
    print("Число с заданным критерием отсутствует в списке")