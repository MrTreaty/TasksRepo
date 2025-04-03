import os

def read_numbers_from_file(filename):
    numbers = []
# Проверяем существование файла
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return []
# Проверка на соответствие формату int
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            clean_line = line.strip()
            if clean_line.isdigit():
                number = int(clean_line)
                numbers.append(number)
        return numbers

    except Exception as e:
        print(f"Cant read file: {e}")
        return []

def min_steps_to_equalize(numbers):
    m = sorted(numbers)[len(numbers) // 2]
    return sum(abs(v - m) for v in numbers)

def main():
    path_to_nums = input("Enter path to file with array elements: ").strip()
    numbers = read_numbers_from_file(path_to_nums)
    steps = min_steps_to_equalize(numbers)
    print(steps)

if __name__ == "__main__":
    main()