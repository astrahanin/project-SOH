import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

# Объединенные таблицы замены для русского и английского языков
lookup_table = {
    'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы', 'Е': 'Ъ', 'Щ': 'Ё',
    'Ж': 'Ш', 'З': 'Ч', 'И': 'Ц', 'Й': 'Х', 'К': 'Ф', 'Л': 'У', 'М': 'Т',
    'Н': 'С', 'О': 'Р', 'П': 'П', 'Р': 'О', 'С': 'Н', 'Т': 'М', 'У': 'Л',
    'Ф': 'К', 'Х': 'Й', 'Ц': 'И', 'Ч': 'З', 'Ш': 'Ж', 'Щ': 'Ё', 'Ъ': 'Е',
    'Ы': 'Д', 'Ь': 'Г', 'Э': 'В', 'Ю': 'Б', 'Я': 'А',
    'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ',
    'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х', 'к': 'ф', 'л': 'у', 'м': 'т',
    'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л',
    'ф': 'к', 'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'Ъ': 'е',
    'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а',
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A',
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
}

# Обратная таблица замены для дешифровки
reverse_lookup_table = {v: k for k, v in lookup_table.items()}

class AtbashCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Atbash Cipher')  # Установка заголовка окна
        self.setGeometry(100, 100, 400, 300)  # Установка размеров окна

        # Создание элементов интерфейса
        self.label = QLabel('Введите текст для шифрования/расшифрования:')  # Метка для ввода текста
        self.text_edit = QTextEdit()  # Поле для ввода текста
        self.process_button = QPushButton('Преобразовать')  # Кнопка для запуска преобразования
        self.result_label = QLabel('Результат:')  # Метка для отображения результата
        self.result_text_edit = QTextEdit()  # Поле для отображения результата

        # Создание компоновки интерфейса
        vbox = QVBoxLayout()  # Вертикальная компоновка
        vbox.addWidget(self.label)  # Добавление метки для ввода текста в компоновку
        vbox.addWidget(self.text_edit)  # Добавление поля ввода текста в компоновку
        vbox.addWidget(self.process_button)  # Добавление кнопки в компоновку
        vbox.addWidget(self.result_label)  # Добавление метки для результата в компоновку
        vbox.addWidget(self.result_text_edit)  # Добавление поля для результата в компоновку

        self.setLayout(vbox)  # Установка компоновки для виджета

        # Подключение кнопки к обработчику события
        self.process_button.clicked.connect(self.processText)

        self.show()  # Отображение окна приложения

    def processText(self):
        text = self.text_edit.toPlainText()  # Получение введенного текста
        processed_text = self.atbash(text)  # Шифрование/дешифрование текста
        self.result_text_edit.setPlainText(processed_text)  # Отображение результата в поле

    def atbash(self, message):
        cipher = ''  # Переменная для хранения результата
        for char in message:  # Перебор символов в тексте
            if char.isalpha():  # Проверка, является ли символ буквой
                if char in lookup_table:  # Если символ найден в таблице замены
                    cipher += lookup_table[char]  # Добавляем замену в результат
                elif char.lower() in lookup_table:  # Проверяем и для маленьких букв
                    cipher += lookup_table[char.lower()].upper()  # Добавляем замену в верхнем регистре
            else:
                cipher += char  # Если символ не является буквой, добавляем как есть
        return cipher  # Возвращаем зашифрованный/расшифрованный текст

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создание объекта приложения
    ex = AtbashCipherApp()  # Создание экземпляра приложения
    sys.exit(app.exec_())  # Запуск основного цикла приложения
