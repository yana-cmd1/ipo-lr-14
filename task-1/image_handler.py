from PIL import Image  # Импортируем класс Image из библиотеки Pillow

class ImageHandler:  # Класс для базовой работы с изображениями
    def __init__(self, path: str):  # Конструктор принимает путь к изображению
        self.path = path  # Сохраняем путь
        self.image = None  # Пока изображение не загружено

    def load_image(self):  # Метод загрузки изображения
        self.image = Image.open(self.path)  # Открываем файл по указанному пути
        print(f"Изображение загружено: {self.path}")  # Сообщаем пользователю
        return self.image  # Возвращаем объект изображения

    def save_as_jpg(self, output_path: str):  # Метод сохранения изображения в формате JPG
        if self.image:  # Проверяем, загружено ли изображение
            self.image.convert("RGB").save(output_path, "JPEG")  # Конвертируем в RGB и сохраняем как JPG
            print(f"Изображение сохранено как JPG: {output_path}")  # Сообщаем пользователю
        else:  # Если изображение не загружено
            print("Сначала загрузите изображение!")  # Предупреждаем пользователя

    def rotate_45(self):  # Метод поворота изображения на 45 градусов
        if self.image:  # Проверяем наличие изображения
            rotated = self.image.rotate(45, expand=True)  # Поворачиваем изображение на 45° с расширением холста
            print("Изображение повернуто на 45°")  # Сообщаем пользователю
            return rotated  # Возвращаем результат
        else:  # Если изображение не загружено
            print("Сначала загрузите изображение!")  # Предупреждаем пользователя
            return None  # Возвращаем None