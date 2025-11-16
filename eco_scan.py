import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PNG Button Example")
window.resize(1024, 600)

bg_path = os.path.join(os.path.dirname(__file__), "ui_elements/123 1.png")
# изображения
icon_start_path = os.path.join(os.path.dirname(__file__), "ui_elements/rectangle_start.png")
text_start_path = os.path.join(os.path.dirname(__file__), "ui_elements/start.png")
icon_path= os.path.join(os.path.dirname(__file__), "ui_elements/icon.png")
how_it_work_item_path= os.path.join(os.path.dirname(__file__), "ui_elements/how_it_work_item.png")
how_it_work_path=os.path.join(os.path.dirname(__file__), "ui_elements/how_it_work.png")

# исправлено: QLabel (с правильным регистром) и QPixmap импортирован выше
label = QLabel(window)
pix = QPixmap(icon_path)
if not pix.isNull():
    w1,h1=119,117
    pix_scaled = pix.scaled(w1, h1, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(pix_scaled)
    label.setFixedSize(pix_scaled.size())
    label.move(453, 0)  # позиция, поменяйте по необходимости
else:
    label.setText("Icon not found")
    label.setFixedSize(119, 117)
    label.move(453, 0)

how_it_work_item=QLabel(window)
how_pix=QPixmap(how_it_work_item_path)
if not how_pix.isNull():
    w2, h2 = 329, 63
    how_scaled = how_pix.scaled(w2, h2, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    how_it_work_item.setPixmap(how_scaled)
    how_it_work_item.setFixedSize(how_scaled.size())
    how_it_work_item.move(348, 104)
else:
    how_it_work_item.setText("How it work item not found")
    how_it_work_item.setFixedSize(329, 63)
    how_it_work_item.move(348, 104)

how_it_work=QLabel(window)
how_it_pix=QPixmap(how_it_work_path)
if not how_it_pix.isNull():
    w3, h3 = 792, 304
    how_it_scaled = how_it_pix.scaled(w3, h3, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    how_it_work.setPixmap(how_it_scaled)
    how_it_work.setFixedSize(how_it_scaled.size())
    how_it_work.move(116, 183)
else:
    how_it_work.setText("How it work not found")
    how_it_work.setFixedSize(792, 304)
    how_it_work.move(116, 183)


# фон (цвет или картинка)
bg_path = os.path.join(os.path.dirname(__file__), "ui_elements/bg.png")
if os.path.exists(bg_path):
    window.setStyleSheet(f"background-image: url({bg_path});")
# else:
#     window.setStyleSheet("background-color: #8be09b;")

button = QPushButton("", window)
button.setIcon(QIcon(icon_start_path))
button.setIconSize(QSize(329, 63))
button.setFixedSize(329, 63)
button.move(349, 496)



window.show()
app.exec()
