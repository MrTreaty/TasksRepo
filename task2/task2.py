import math

# Что мы вводим? Проверка данных на float-type.
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Пилим строку на пары чисел, если все элементы строки - числа
def parse_line(line):
    parts = line.split()
    return list(map(float, parts)) if all(is_float(p) for p in parts) else None

# Читаем координаты точек из файла и возвращаем кортеж координат (X,Y). Проверка на количество точек.
def read_points(filename):
    with open(filename, "r") as file:
        return [tuple(data) for line in file if (data := parse_line(line)) and len(data) == 2]
    if not (1 <= len(points) <= 100):
        raise ValueError(f"Ошибка: количество точек должно быть от 1 до 100, а в файле {len(points)} точек.")
    
    return points

# Читаем данные по окружности
def read_circle_data(filename):
    with open(filename, "r") as file:
        data = [parse_line(line) for line in file if parse_line(line)]
    #Вернул как смог, мейби можно чище сделать
    return data[0], data[1][0] 

def main():
# Запрашиваем у пользователя пути к файлам
    path_to_coord = input("Введите путь к файлу с координатами точек: ")
    path_to_circle = input("Введите путь к файлу с данными окружности: ")

# Нашел, что можно обработать "мягко" ошибки. Вай нот.
    try:
        points = read_points(path_to_coord)
        center, r = read_circle_data(path_to_circle)

        print("Точки:", points)
        print("Центр окружности:", center, "Радиус:", r)

# Проверяем каждую точку и выводим.
        c, d = center
        for a, b in points:
            distance = math.sqrt((c - a) ** 2 + (d - b) ** 2)
            print(0 if distance == r else 2 if distance > r else 1)

    except ValueError as errVal:
        print(errVal)
    except FileNotFoundError:
        print("Ошибка: Файл не найден. Проверьте путь и попробуйте снова.")
    except Exception as errExept:
        print(f"Произошла ошибка: {errExept}")

if __name__ == "__main__":
    main()