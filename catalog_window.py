from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class CatalogWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Каталог продуктов")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #8a7f8e; font-size: 18px;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        categories = {
            'Овощи и фрукты': {
                'Помидоры, 1кг': 180,
                'Огурцы, 1кг': 100,
                'Картофель, 1кг': 42,
                'Лук, 1кг': 33,
                'Морковь, 1кг': 70,
                'Яблоки, 1кг': 100,
                'Бананы, 1кг': 130,
                'Виноград, 1кг': 160,
                'Апельсины, 1кг': 200,
                'Киви, 1кг': 230
            },
            'Молочные продукты': {
                'Молоко, 900мл': 62,
                'Сметана, 300г': 60,
                'Сыр, 200г': 200,
                'Творог, 180г': 88,
                'Кефир, 900мл': 105,
                'Масло, 180г': 190
            },
            'Хлеб и выпечка': {
                'Батон, 400г': 44,
                'Хлеб, 700г': 54,
                'Круассан, 45г': 100,
                'Ватрушка, 100г': 50,
                'Пицца, 300г': 350
            },
            'Мясо': {
                'Курица, 1кг': 160,
                'Говядина, 1кг': 800
            },
            'Рыба и морепродукты': {
                'Форель, 200г': 300,
                'Креветки, 450г': 450,
                'Мидии, 200г': 350
            },
            'Бакалея': {
                'Чай, 50г': 80,
                'Кофе, 95г': 300,
                'Гречка, 900г': 42,
                'Рис, 900г': 110,
                'Макароны, 450г': 60,
                'Овсянка, 400г': 23
            },
            'Алкоголь': {
                'Коньяк, 250мл': 680
            }
        }

        button_style = "font-size: 18px; color: white;"
        for category in categories.keys():
            category_button = QPushButton(category)
            category_button.setStyleSheet(button_style)
            category_button.clicked.connect(
                lambda checked, cat=category: self.show_category_products(cat, categories[cat]))
            layout.addWidget(category_button)

        self.setLayout(layout)

    def show_category_products(self, category, products):
        products_window = QDialog(self)
        products_window.setWindowTitle(f"Категория: {category}")
        products_window.setFixedSize(600, 400)
        products_window.setStyleSheet("background-color: #8a7f8e; font-size: 18px;")

        layout = QVBoxLayout()

        for product, price in products.items():
            product_layout = QHBoxLayout()

            product_label = QLabel(f"{product} - {price} ₽")

            product_image = QLabel()
            image_name = product.split(',')[0].replace(' ', '_').lower()
            image_path = f'png/{image_name}.png'
            pixmap = QPixmap(image_path)

            if pixmap.isNull():
                print(f"Не удалось загрузить изображение: {image_path}")
            else:
                product_image.setPixmap(pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))

            btn_add_to_cart = QPushButton("Добавить в корзину")
            btn_add_to_cart.setStyleSheet("font-size: 18px; color: white;")
            btn_add_to_cart.clicked.connect(lambda checked, p=product, pr=price: self.parent.add_to_cart(p, pr))

            product_layout.addWidget(product_image)
            product_layout.addWidget(product_label)
            product_layout.addWidget(btn_add_to_cart)
            layout.addLayout(product_layout)

        products_window.setLayout(layout)
        products_window.exec()
