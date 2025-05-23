from PyQt5.QtWidgets import (
    QApplication,QWidget,QRadioButton,
    QLabel,QVBoxLayout,QHBoxLayout,
    QMessageBox
    )
from PyQt5.QtCore import Qt

app = QApplication([])

def show_win():
    victory_window = QMessageBox()
    victory_window.setText('Жаль')
    victory_window.exec()

def show_lose():
    lose_window = QMessageBox()
    lose_window.setText('Жди') 
    lose_window.exec()

window = QWidget()
window.resize(750,550)
window.setWindowTitle('Конкурс от Crazy People')
window.move(0,0)

quection = QLabel('Ты один?')
btn1 = QRadioButton('Да')
btn1.clicked.connect(show_lose)
btn2 = QRadioButton('Нет')
btn2.clicked.connect(show_win)
btn3 = QRadioButton('Не знаю')
btn3.clicked.connect(show_lose)
btn4 = QRadioButton('Может быть')
btn4.clicked.connect(show_lose)

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line1.addWidget(quection,alignment = Qt.AlignCenter)
h_line2.addWidget(btn1,alignment = Qt.AlignCenter)
h_line2.addWidget(btn3,alignment = Qt.AlignCenter)
h_line3.addWidget(btn2,alignment = Qt.AlignCenter)
h_line3.addWidget(btn4,alignment = Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

window.setLayout(v_line)

window.show()
app.exec()