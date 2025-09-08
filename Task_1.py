import argparse
import os
import shutil
from pathlib import Path

def copy_and_sort_files(source_path, dest_path):
    """
    Рекурсивно копіює файли з вихідної директорії до директорії призначення
    та сортує їх за розширенням.
    """
    # Обробка винятків доступу
    try:
        # Перевірка на існування вихідної директорії
        if not source_path.is_dir():
            print(f"Помилка: Вихідна директорія '{source_path}' не існує.")
            return

        # Рекурсивний обхід директорії
        for element in source_path.iterdir():
            if element.is_dir():
                # Рекурсивний виклик для піддиректорій
                copy_and_sort_files(element, dest_path)
            elif element.is_file():
                # Визначення розширення файлу
                extension = element.suffix.lstrip('.')
                if not extension:
                    extension = 'no_extension'

                # Створення нової піддиректорії
                new_dir = dest_path / extension
                new_dir.mkdir(parents=True, exist_ok=True)

                # Копіювання файлу
                shutil.copy(element, new_dir)
                print(f"Файл '{element.name}' скопійовано до '{new_dir}'")

    except PermissionError:
        print(f"Помилка доступу: Відсутній дозвіл для читання/запису в директорію.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    """
    Головна функція для парсингу аргументів командного рядка
    та запуску процесу копіювання.
    """
    # 1. Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Копіює та сортує файли за розширенням.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії.")
    parser.add_argument("-d", "--dest", type=str, default="dist",
                        help="Шлях до директорії призначення. За замовчуванням: 'dist'.")

    args = parser.parse_args()

    source_path = Path(args.source)
    dest_path = Path(args.dest)

    print(f"Вихідна директорія: {source_path}")
    print(f"Директорія призначення: {dest_path}")

    # 2. Запуск процесу копіювання
    copy_and_sort_files(source_path, dest_path)
    print("\nПроцес завершено.")

if __name__ == "__main__":
    main()