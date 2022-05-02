import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class digitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        layout = QVBoxLayout()
        fnt = QFont('open sans', 120, QFont.Bold)
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)
        self.setLayout(layout)
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

    def displaytime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        print(displayText)
        self.lbl.setText(displayText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = digitalClock()
    window.show()
    sys.exit(app.exec_())