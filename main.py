import functools

from word_color.get_word_color import get_word_color

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('Word color App')
window.setGeometry(835, 415, 250, 250)

color = QLabel(parent=window)
color.setGeometry(0, 0, 250, 250)

word = input("Enter word: ")
bg = get_word_color(word)

color.setStyleSheet(f'background: rgb({bg[0]}, {bg[1]}, {bg[2]});'
                    f'display: flex;'
                    f'position: absolute;'
                    f'width: 100%;'
                    f'height: 100%;'
                    f'font-size: 56px;'
                    f'justify-content: center;'
                    f'align-items: center;')
color.setText(word)
# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
