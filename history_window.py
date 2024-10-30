from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class HistoryWindow(QDialog):
    def __init__(self, purchase_history, parent):
        super().__init__(parent)
        self.purchase_history = purchase_history
        self.initUI()

    def initUI(self):
        self.setWindowTitle("История покупок")
        layout = QVBoxLayout()

        if not self.purchase_history:
            layout.addWidget(QLabel("История покупок пуста."))
        else:
            for entry in self.purchase_history:
                layout.addWidget(QLabel(entry))

        self.setLayout(layout)
