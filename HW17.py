s = input("Введите последовательность целых чисел через пробел:")
a = [int(x) for x in s.split()]
def is_int():
    try:
        int(u)
        return True
    except ValueError:
        return False
u = input("Введите целое число больше минимального и не больше максимального в последовательности:")
if is_int() is True:
    user = int(u)
    if user <= min(a):
        print("Ошибка: Число должно быть больше минимального")
    elif user > max(a):
        print("Ошибка: Число не должно быть больше максимального")
    else:
        a.append(user)
        print("Список до сортировки:", a)

        def my_func():
            for i in range(len(a)):
                idx = i
                for j in range(i, len(a)):
                    if a[j] < a[idx]:
                        idx = j
                if i != idx:
                    a[i], a[idx] = a[idx], a[i]
            return a
        print("Список после сортировки:", my_func())

        def binary_search(a, user, left, right):

            if left > right:
                return False
            middle = (right + left) // 2
            if a[middle] == user:
                return middle
            elif user < a[middle]:
                return binary_search(a, user, left, middle - 1)
            else:
                return binary_search(a, user, middle + 1, right)
        print("Индекс числа, меньше введенного:", (binary_search(a, user, 0, len(a) - 1) - 1))
else:
    print("Ошибка: Введено не целое число")
