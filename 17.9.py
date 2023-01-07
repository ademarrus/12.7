num_array = [int(x) for x in input("Введите любую последовательность чисел через пробел: ").split()]

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
print(merge_sort(num_array))

#  БЛОК ЗАПРОСА И ПРОВЕРКИ ЛЮБОГО ЧИСЛА, ЗАДАННОГО ПОЛЬЗОВАТЕЛЕМ
while True:
    try:
        number = int(input("Введите любое число: "))
        break
    except ValueError:
        print("Вы ввели неверный формат данных. Пожалуйста, введите число")


# БЛОК АЛГОРИТМА БИНАРНОГО ПОИСКА

def binary_search(num_array, number, left, right):
    if left > right:  
        return False  
    middle = (right + left) // 2  
    if num_array[middle] == number:  
        return middle  
    elif number < num_array[middle]:  
        return binary_search(num_array, number, left, middle - 1)
    else:  
        return binary_search(num_array, number, middle + 1, right)

print(binary_search(num_array, number, 0, len(num_array)))
