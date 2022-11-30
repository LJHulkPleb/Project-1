from PyQt5.QtWidgets import *
from RecursionView import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculateButton.clicked.connect(lambda: self.calculate())
        self.clearButton.clicked.connect(lambda: self.clear())

    def power(self, firstNum: int, powNum: int):
        """
        Function that calculates a number and an exponent of that number
        :param firstNum: The number that will be used as the base in an exponential problem
        :param powNum: The number that will be used as the exponent in an exponential problem
        :return: The first number taken to the power of the second given number
        """

        if powNum <=0:
            raise ValueError
        elif powNum == 1:
            return firstNum
        else:
            return firstNum * self.power(firstNum, powNum - 1)

    def cat_ears(self, firstNum: int) -> int:
        """
        Function that calculates the number of cat ears in a given group
        :param firstNum: The number of cats in a group
        :return: The amount of cat ears determined from the given group
        """
        if firstNum < 0:
            raise ValueError
        if firstNum == 0:
            return 0
        else:
            return 2 + self.cat_ears(firstNum - 1)

    def alien_ears(self, firstNum: int)-> int:
        """
        Function to calculate the number of alien ears in a given group of Aliens every odd
        alien has 2 ears and every even alien has 3 ears
        :param firstNum: The amount of aliens given
        :return: The calculated number of aliens
        """

        if firstNum < 0:
            raise ValueError
        if firstNum == 0:
            return 0
        else:
            if firstNum % 2 == 0:
                return 3 + self.alien_ears(firstNum - 1)
            else:
                return 2 + self.alien_ears(firstNum - 1)

    def clear(self):
        """
        Removes all entries and resets button to power button
        :return: nothing
        """
        self.firstEntry.setText("")
        self.powerEntry.setText("")
        self.summaryText.setText("")
        self.powerButton.setChecked(True)

    def calculate(self):
        """
        Calculate button to do math given the text in the two entry boxes
        :return: Returns the result depending on the button clicked and numbers entered
        """
        try:
            firstNum = int(self.firstEntry.text())
            if self.powerButton.isChecked():
                powNum = int(self.powerEntry.text())
                result = self.power(firstNum, powNum)
            elif self.catButton.isChecked():
                result = self.cat_ears(firstNum)
            elif self.alienButton.isChecked():
                result = self.alien_ears(firstNum)
            self.summaryText.setText(f'The calculated number is {result}')
        except ValueError:
            self.summaryText.setText("Please enter a valid number in the entry box")



