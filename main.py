import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.titles = None

    def update_result(self):
        try:
            result = self.cur.execute("SELECT * FROM coffee").fetchall()
            self.table.setRowCount(len(result))
            self.table.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in self.cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        except Exception:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
