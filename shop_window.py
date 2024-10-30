from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDialog, QLabel
from catalog_window import CatalogWindow
from cart_window import CartWindow
from history_window import HistoryWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from datetime import datetime

class ShopWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продуктовый магазин")
        self.balance = 5000
        self.cart = {}
        self.purchase_history = []
        self.receipt_number = 1
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #8a7f8e; font-size: 18px;")
        button_style = "font-size: 18px; color: white;"

        layout = QVBoxLayout()

        btn_catalog = QPushButton('Каталог')
        btn_balance = QPushButton('Баланс')
        btn_cart = QPushButton('Корзина')
        btn_history = QPushButton('История покупок')

        btn_catalog.setStyleSheet(button_style)
        btn_balance.setStyleSheet(button_style)
        btn_cart.setStyleSheet(button_style)
        btn_history.setStyleSheet(button_style)

        btn_catalog.clicked.connect(self.show_catalog)
        btn_balance.clicked.connect(self.show_balance)
        btn_cart.clicked.connect(self.show_cart)
        btn_history.clicked.connect(self.show_purchase_history)

        layout.addWidget(btn_catalog)
        layout.addWidget(btn_balance)
        layout.addWidget(btn_cart)
        layout.addWidget(btn_history)

        self.setLayout(layout)

    def show_balance(self):
        balance_window = QDialog(self)
        balance_window.setWindowTitle("Баланс")

        layout = QVBoxLayout()
        label_balance = QLabel(f"Баланс вашей карты: {self.balance} ₽")
        layout.addWidget(label_balance)

        pixmap = QPixmap('png/credit_card.png')
        pixmap = pixmap.scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio)
        label_image = QLabel()
        label_image.setPixmap(pixmap)
        layout.addWidget(label_image)

        balance_window.setLayout(layout)
        balance_window.exec()

    def show_catalog(self):
        catalog_window = CatalogWindow(self)
        catalog_window.exec()

    def show_cart(self):
        cart_window = CartWindow(self.cart, self.balance, self)
        cart_window.exec()

    def show_purchase_history(self):
        history_window = HistoryWindow(self.purchase_history, self)
        history_window.exec()

    def add_to_cart(self, product, price):
        if product in self.cart:
            self.cart[product]['quantity'] += 1
        else:
            self.cart[product] = {'quantity': 1, 'price': price}

    def generate_receipt(self, total_price):
        receipt_number = self.receipt_number
        self.receipt_number += 1
        receipt_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.purchase_history.append(
            f"Дата: \"{receipt_date}\" Сумма: \"{total_price} ₽\" Номер чека: \"{receipt_number}\"")

        self.show_receipt(receipt_number, total_price, receipt_date)

    def show_receipt(self, receipt_number, total_price, receipt_date):
        receipt_window = QDialog(self)
        receipt_window.setWindowTitle("Чек")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("ООО \"Продуктовый магазин\""))
        layout.addWidget(QLabel("г. Москва, Волгоградский проспект, 43с1А"))
        layout.addWidget(QLabel(f"КАССОВЫЙ ЧЕК №{receipt_number}"))

        for product, info in self.cart.items():
            quantity = info['quantity']
            price = info['price']
            total_cost = quantity * price
            layout.addWidget(QLabel(f"{product} x{quantity} - {total_cost} ₽"))

        layout.addWidget(QLabel(f"ИТОГ ---------- {total_price} ₽"))
        layout.addWidget(QLabel(f"БЕЗНАЛИЧНЫМИ ---------- {total_price} ₽"))
        layout.addWidget(QLabel("СПАСИБО ЗА ПОКУПКУ!"))
        layout.addWidget(QLabel(receipt_date))

        receipt_window.setLayout(layout)
        receipt_window.exec()

