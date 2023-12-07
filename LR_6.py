from datetime import datetime

class Smartphone:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.release_year

class Store:
    def __init__(self):
        self.smartphones = []

    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)

    def remove_smartphone(self, name):
        for smartphone in self.smartphones:
            if smartphone.name == name:
                self.smartphones.remove(smartphone)
                print(f"{name} видалено з магазину.")
                return
        print(f"{name} не знайдено у магазині.")

    def list_smartphones(self, max_year):
        for smartphone in self.smartphones:
            age = smartphone.calculate_age()
            if age <= max_year:
                print(f"{smartphone.name} ({smartphone.release_year}), вік: {age} років")

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            for smartphone in self.smartphones:
                file.write(f"{smartphone.name},{smartphone.release_year}\n")

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.smartphones = [Smartphone(*line.strip().split(',')) for line in lines]
        except FileNotFoundError:
            print("Файл не знайдено.")
        except Exception as e:
            print(f"Помилка завантаження даних з файлу: {e}")

    def clear_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write('')
            print(f"Файл {file_path} очищено.")
        except Exception as e:
            print(f"Помилка очищення файлу: {e}")

def main():
    store = Store()
    
    file_path = input("Введіть шлях до файлу для збереження/завантаження даних: ")
    
    try:
        store.load_from_file(file_path)
    except Exception as e:
        print(f"Помилка завантаження даних: {e}")

    while True:
        print("1. Додати смартфон")
        print("2. Видалити смартфон")
        print("3. Список смартфонів за роком випуску")
        print("4. Зберегти дані до файлу")
        print("5. Очистити файл")
        print("6. Вийти")
        
        choice = input("Введіть ваш вибір: ")
        
        if choice == "1":
            name = input("Введіть назву смартфону: ")
            release_year = input("Введіть рік випуску: ")
            try:
                release_year = int(release_year)
                smartphone = Smartphone(name, release_year)
                store.add_smartphone(smartphone)
                print(f"{name} додано до магазину.")
            except ValueError:
                print("Невірний рік випуску. Будь ласка, введіть правильний рік.")
        elif choice == "2":
            name = input("Введіть назву смартфону для видалення: ")
            store.remove_smartphone(name)
        elif choice == "3":
            max_year = input("Введіть максимальний рік випуску: ")
            try:
                max_year = int(max_year)
                store.list_smartphones(max_year)
            except ValueError:
                print("Невірний рік випуску. Будь ласка, введіть правильний рік.")
        elif choice == "4":
            store.save_to_file(file_path)
            print("Дані збережено до файлу.")
        elif choice == "5":
            store.clear_file(file_path)
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть правильну опцію.")

if __name__ == "__main__":
    main()
