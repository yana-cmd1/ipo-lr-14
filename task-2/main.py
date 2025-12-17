# Дмитрук Яны

import sys  # Импортируем модуль sys, чтобы работать с системными путями
import os   # Импортируем модуль os, чтобы работать с файловой системой

# Добавляем путь к родительской папке, чтобы Python видел пакет classes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.image_handler import ImageHandler  # Импортируем класс ImageHandler из пакета classes
from classes.image_processor import ImageProcessor  # Импортируем класс ImageProcessor из пакета classes

def main():  # Главная функция программы
    # --- Работа с первой картинкой через ImageHandler ---
    path1 = input("Введите путь к первой картинке: ")  # Запрашиваем путь к первой картинке
    handler = ImageHandler(path1)  # Создаём объект класса ImageHandler и передаём путь

    img1 = handler.load_image()  # Загружаем изображение
    rotated = handler.rotate_45()  # Поворачиваем изображение на 45 градусов
    handler.image = rotated  # Обновляем текущее изображение в объекте handler
    handler.save_as_jpg("output_handler.jpg")  # Сохраняем изображение в формате JPG

    print("Первая картинка обработана через ImageHandler и сохранена как output_handler.jpg")  # Сообщаем пользователю

    # --- Работа со второй картинкой через ImageProcessor ---
    path2 = input("Введите путь ко второй картинке: ")  # Запрашиваем путь ко второй картинке
    handler2 = ImageHandler(path2)  # Используем ImageHandler только для загрузки
    img2 = handler2.load_image()  # Загружаем изображение

    processor = ImageProcessor(img2)  # Создаём объект класса ImageProcessor и передаём изображение
    sharpened = processor.apply_sharpen()  # Применяем фильтр повышения резкости
    bordered = processor.add_border(color="white")  # Добавляем белую рамку шириной 15 пикселей

    sharpened.save("output_sharpened.jpg")  # Сохраняем изображение с повышенной резкостью
    bordered.save("output_bordered.jpg")  # Сохраняем изображение с рамкой

    print("Вторая картинка обработана через ImageProcessor и сохранена как output_sharpened.jpg и output_bordered.jpg")  # Сообщаем пользователю

if __name__ == "__main__":  # Проверяем, запущен ли файл напрямую
    main()  # Запускаем главную функцию