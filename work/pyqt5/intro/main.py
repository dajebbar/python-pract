# 1- Import packages
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


# Create clicked Function connected to my_btn
def clicked():
    print('Just clicked!')

def main():
    # Create root application
    app = QApplication(sys.argv)
    # Create a root window
    window = QMainWindow()
    # Set coodinates of window [x, y, width, height] 1366 × 768 1920 × 1080 
    window.setGeometry(0, 0, 1366, 768)
    # Set title
    window.setWindowTitle('App')
    #  Create a text Label
    text = QLabel(window)
    text.setText('Hello from PyQt!!!')
    # Create a Button
    my_btn = QPushButton(window)
    my_btn.setText('Click!')
    my_btn.move(1366/2, 768/2)
    my_btn.clicked.connect(clicked)
    # Loop for window
    window.show()
    # Exit
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
        