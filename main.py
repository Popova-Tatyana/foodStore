import sys
from PyQt6.QtWidgets import QApplication
from shop_window import ShopWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shop = ShopWindow()
    shop.show()
    sys.exit(app.exec())
