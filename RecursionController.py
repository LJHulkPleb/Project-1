from PyQt5.QtWidgets import *
from RecursionView import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculateButton.clicked.connect(lambda: self.calculate())
        self.clearButton.clicked.connect(lambda: self.clear())

    def power(self, firstNum, powNum):
        if powNum == 1:
            return firstNum
        else:
            return firstNum * self.power(firstNum, powNum - 1)


    def cat_ears(self,firstNum):
        if firstNum == 0:
            return 0
        else:
            return 2 + self.cat_ears(firstNum - 1)


    def alien_ears(self, firstNum):
        if firstNum == 0:
            return firstNum
        else:
            if firstNum % 2 == 0:
                return 3 + self.alien_ears(firstNum - 1)
            else:
                return 2 + self.alien_ears(firstNum - 1)

    def clear(self):
        self.firstEntry.setText("")
        self.powerEntry.setText("")
        self.summaryText.setText("")

    def calculate(self):
        try:
            firstNum = float(self.firstEntry.text())
            powNum = float(self.powerEntry.text())
            result = 0
            if self.powerButton.isChecked():
                result = self.power(firstNum, powNum)
            elif self.catButton.isChecked():
                result = self.cat_ears(firstNum)
            elif self.alienButton.isChecked():
                result = self.alien_ears(firstNum)
            self.summaryText.setText("The calculated number is " + result)
        except ValueError:
            self.summaryText.setText("Please enter a valid number in the entry box")



