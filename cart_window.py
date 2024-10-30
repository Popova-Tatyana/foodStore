from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox

class CartWindow(QDialog):
    def __init__(self, cart, balance, parent):
        super().__init__(parent)
        self.cart = cart
        self.balance = balance
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Корзина")
        layout = QVBoxLayout()
        self.total_price = sum(info['quantity'] * info['price'] for info in self.cart.values())

        for product, info in self.cart.items():
            quantity = info['quantity']
            price = info['price']
            total_cost = quantity * price
            layout.addWidget(QLabel(f"{product} x{quantity} - {total_cost} ₽"))

        layout.addWidget(QLabel(f"Итого: {self.total_price} ₽"))

        btn_checkout = QPushButton("Оплатить")
        btn_checkout.clicked.connect(self.checkout)
        layout.addWidget(btn_checkout)

        self.setLayout(layout)

    def checkout(self):
        if self.total_price > self.balance:
            QMessageBox.warning(self, "Ошибка", "Недостаточно средств на балансе!")
        else:
            self.parent.balance -= self.total_price
            self.parent.generate_receipt(self.total_price)
            self.parent.cart.clear()
            QMessageBox.information(self, "Успех", "Покупка успешно завершена!")
            self.accept()
