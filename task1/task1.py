import array

n = int(input("Введите диапазон чисел n: "))
m = int(input("Введите интервал движения по массиву m: ")) 

arr_list = []  
the_way = ""

first_element = 1
while True:
    # Генерим массив, заполняя его через остаток от деления
    arr = []
    for i in range(m):
        num =  (first_element + i - 1) % n + 1
        arr.append(num)
    
    arr_list.append(arr)
    the_way += str(arr[0])
    
    if len(arr_list) > 1 and arr_list[-1][-1] == arr_list[0][0]: 
        break
    #Первым элементом становится последний
    first_element = arr[m-1]

# Вывод всех массивов
for arr in arr_list:
    print("".join(map(str, arr)))

# Вывод пути(состоящего из первых цифр каждого массива)
print("Путь:", the_way)
