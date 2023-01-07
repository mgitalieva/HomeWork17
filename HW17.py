s = input("Введите последовательность целых чисел через пробел: ")
a = [int(x) for x in s.split()]
user = int(input("Введите целое число больше минимального и не больше максимального в последовательности: "))

if user <= min(a) or user > max(a):
    print("Число не удовлетворяет условиям")
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
    print("Индекс числа, меньше введенного: ", (binary_search(a, user, 0, len(a) - 1)-1))
