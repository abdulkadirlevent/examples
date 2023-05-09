from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')

        self.num1_label = QLabel('Number 1:')
        self.num1_edit = QLineEdit()

        self.num2_label = QLabel('Number 2:')
        self.num2_edit = QLineEdit()

        self.result_label = QLabel('Result:')
        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_edit)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_edit)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_edit)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        num1 = int(self.num1_edit.text())
        num2 = int(self.num2_edit.text())
        result = num1 + num2
        self.result_edit.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
