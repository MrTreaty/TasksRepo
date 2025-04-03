import json

def import_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

#Маппим структуры , заполняем совпадающие по id поля значениями value.
def fill_values(tests, values_data):
    if isinstance(tests, list):
        for test in tests:
            fill_values(test, values_data)
    elif isinstance(tests, dict):
        if "id" in tests and "value" in tests:
            tests["value"] = values_data.get(tests["id"], "")
        if "values" in tests:
            fill_values(tests["values"], values_data)

#Основная программа, ждём ввод от пользователя и выполняем функции.
def main():
    values_path = input("Введите путь до values.json: ")
    tests_path = input("Введите путь до tests.json: ")
    reports_path = input("Введите путь для сохранения reports.json: ")
    
    tests_data = import_json(tests_path)
    values_data = import_json(values_path)
    
    new_values = {entry["id"]: entry["value"] for entry in values_data["values"]}
    
    fill_values(tests_data["tests"], new_values)
    
    save_json(tests_data, reports_path)
    print(f"Файл {reports_path} успешно создан!")

if __name__ == "__main__":
    main()
