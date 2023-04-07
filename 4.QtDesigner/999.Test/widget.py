import resource_rc
import ui_widget as uw 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PySide6 import QtWidgets


class Widget(QWidget, uw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        screen_size = QApplication.primaryScreen().availableGeometry()
        self.quote_label.setGeometry(screen_size)
        
        print(self.quotes_output.geometry().getCoords())
        print(screen_size.getCoords())

        possitionX = (screen_size.getCoords()[2] / self.quotes_output.geometry().getCoords()[2]) * self.quotes_output.geometry().getCoords()[0]
        possitionY = (screen_size.getCoords()[3] / self.quotes_output.geometry().getCoords()[3]) * self.quotes_output.geometry().getCoords()[1]
        print(possitionX, possitionY)
        self.quotes_output.setGeometry(possitionX, possitionY, self.quotes_output.geometry().getCoords()[2], self.quotes_output.geometry().getCoords()[3])

        self.showFullScreen()


app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()

app.exec()