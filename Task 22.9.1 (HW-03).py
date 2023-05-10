def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def sort_list(numbers_list):
    return sorted(numbers_list)


def main():
    sequence_numbers = input("Введите любые целые числа через пробел: ")
    numbers_list = sequence_numbers.split()

    try:
        numbers_list = [int(x) for x in numbers_list]
    except ValueError:
        print("Необходимо вводить только целые числа через пробел")
        return

    if not numbers_list:
        print("Введите данные")
        return

    random_number = input("Введите одно число: ")

    try:
        random_number = int(random_number)
    except ValueError:
        print("Необходимо ввести одно целое число.")
        return

    sorted_list = sort_list(numbers_list)

    if not sorted_list[0] <= random_number <= sorted_list[-1]:
        print("Введенное число вне диапазона значений списка чисел.")
        return

    position = binary_search(sorted_list, random_number)
    print("Числа в порядке возрастания: ", sorted_list)
    print("Позиция элемента, который меньше введенного числа: ", position)
    print("Следующее число, которое больше или равно введённому числу: ", sorted_list[position])


if __name__ == "__main__":
    main()