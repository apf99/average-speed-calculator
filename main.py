from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel('Distance:')
        self.distance_line_edit = QLineEdit()

        time_label = QLabel('Time (hours):')
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        # add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1, 1, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = self.distance_line_edit.text()
        time = self.time_line_edit.text()
        speed = float(distance) / float(time)
        self.output_label.setText(f'Average Speed: {speed} km/h')


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
