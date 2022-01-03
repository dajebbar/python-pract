import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton


class Ui_MainWindow(QMainWindow):
    ''''''
    def __init__(self, x, y, width, height, title):
        super().__init__()
        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)
        self.setupUI()
    

    def setupUI(self):
        self.text = QLabel(self)
        self.text.setText('Hello from PyQt5!')

        self.btn = QPushButton(self)
        self.btn.setText('Click')
        self.btn.move(120, 120)
        self.btn.clicked.connect(self.click_on)
    
    def click_on(self):
        self.text.setText('Txt changed!')


def main():
    app = QApplication(sys.argv)
    window = Ui_MainWindow(200, 200, 300, 300, 'My App')
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

