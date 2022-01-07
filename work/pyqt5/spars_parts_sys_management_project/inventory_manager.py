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
        # NAVIGATE Function have no btn should be called in constructor
        self.NAVIGATE()
    
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)
        self.check_btn.clicked.connect(self.LEVEL)

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
        cursor2 = db.cursor()
        cursor3 = db.cursor()

        parts_nbr = '''SELECT COUNT (DISTINCT PartName) FROM parts_table'''
        ref_nbr = '''SELECT COUNT (DISTINCT Reference) FROM parts_table'''

        result_ref_nbr = cursor2.execute(ref_nbr)
        result_parts_nbr = cursor3.execute(parts_nbr)

        self. lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self. lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))

        # Display 4 results: Min, Max, Nbr of holes and their References name
        cursor4 = db.cursor()
        cursor5 = db.cursor()

        min_hole = '''SELECT MIN(NumberOfHoles), Reference FROM parts_table'''
        max_hole = '''SELECT MAX(NumberOfHoles), Reference FROM parts_table'''

        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)

        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()

        # Display results in QLabels
        self.lbl_min_hole.setText(str(r1[0]))
        self.lbl_max_hole.setText(str(r2[0]))
        self.lbl_min_hole_1.setText(str(r1[1]))
        self.lbl_max_hole_2.setText(str(r2[1]))

    
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
    
    def LEVEL(self):
        '''Top 3 reference with min inventory level'''
        db = sqlite3.connect('parts.db')
        cursor = db.cursor()
        command = '''SELECT Reference, PartName, Count FROM parts_table ORDER BY Count LIMIT 3'''
        result = cursor.execute(command)

        self.table2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def NAVIGATE(self):
        '''Get all columns from DB to crud'''
        db = sqlite3.connect('parts.db')
        cursor = db.cursor()
        command = '''SELECT * FROM parts_table'''
        result = cursor.execute(command)
        val = result.fetchone()

        self.id.setText(str(val[0]))
        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setValue(val[8])


# Application
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
