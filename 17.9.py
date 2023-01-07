num_array = [int(x) for x in input("Введите любую последовательность чисел чрез пробел: ").split()]

def merge_sort(num_array):  
    if len(num_array) < 2: 
        return num_array[:] 
    else:
        middle = len(num_array) // 2 
        left = merge_sort(num_array[:middle])  
        right = merge_sort(num_array[middle:])  
        return merge(left, right)  # слияние 

def merge(left, right):
    all_num = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            all_num.append(left[i])
            i += 1
        else:
            all_num.append(right[j])
            j += 1
    while i < len(left):
        all_num.append(left[i])
        i += 1
    while j < len(right):
        all_num.append(right[j])
        j += 1
    return all_num
print(merge_sort(array))

#  БЛОК ЗАПРОСА И ПРОВЕРКИ ЛЮБОГО ЧИСЛА, ЗАДАННОГО ПОЛЬЗОВАТЕЛЕМ
while True:
    try:
        number = int(input("Введите любое число в диапазоне от 1 до 999: "))
        if number < 0 or number > 999:
            raise Exception
        break
    except ValueError:
        print("Вы ввели неверный формат данных. Пожалуйста, введите число")
    except Exception:
        print("Вы ввели число, не воздящее в требуемый диапазон!")

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, element, 0, len(array)))
