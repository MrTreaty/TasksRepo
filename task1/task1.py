def main():
    n = int(input("Enter range of numbers n: "))
    m = int(input("Enter step interval m: ")) 

    arr_list = []  
    the_path = ""

    first_element = 1
    while True:
# Генерим массив, заполняя его через остаток от деления
        arr = []
        for i in range(m):
            num =  (first_element + i - 1) % n + 1
            arr.append(num)
    
        arr_list.append(arr)
        the_path += str(arr[0])
    
        if len(arr_list) > 1 and arr_list[-1][-1] == arr_list[0][0]: 
            break
# Первым элементом становится последний
        first_element = arr[m-1]

# Вывод всех массивов
    # for arr in arr_list:
    #     print("".join(map(str, arr)))

# Вывод пути(состоящего из первых цифр каждого массива)
    print("Path:", the_path)

if __name__ == "__main__":
    main()