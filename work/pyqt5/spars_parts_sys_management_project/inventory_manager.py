# Import packages
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys

from os import path

from PyQt5.uic import loadUiType

import sqlite3

FORM_CLASS, _ = loadUiType(path.join(path.dirname('__file__'), 'main.ui'))


# Main class
class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
    
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)

    # core code
    def GET_DATA(self):
        '''Connect with database and fill GUI table with data'''
        db = sqlite3.connect('parts.db')
        cursor = db.cursor()
        command = '''SELECT * FROM parts_table'''
        result = cursor.execute(command)

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        # Display references and type number in statistics tab
    
    def SEARCH(self):
        '''Take the count level and return all references equal or less than it'''
        db = sqlite3.connect('parts.db')
        cursor = db.cursor()
        nbr = self.count_filter_txt.text()
        command = '''SELECT * FROM parts_table where count <= ?'''
        result = cursor.execute(command, [nbr])

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))


# Application
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
