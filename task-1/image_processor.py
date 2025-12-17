from PIL import ImageFilter, ImageOps  # Импортируем фильтры и операции из Pillow

class ImageProcessor:  # Класс для обработки изображений
    def __init__(self, image):  # Конструктор принимает объект изображения
        self.image = image  # Сохраняем изображение в атрибуте класса

    def apply_sharpen(self):  # Метод применения фильтра повышения резкости
        sharpened = self.image.filter(ImageFilter.SHARPEN)  # Применяем фильтр SHARPEN
        print("Фильтр SHARPEN применён")  # Сообщаем пользователю
        return sharpened  # Возвращаем результат

    def add_border(self, border_size=15, color="white"):  # Метод добавления рамки (по умолчанию белая)
        bordered = ImageOps.expand(self.image, border=border_size, fill=color)  # Добавляем рамку указанного размера и цвета
        print(f"Добавлена {color} рамка шириной {border_size}px")  # Сообщаем пользователю
        return bordered  # Возвращаем результат