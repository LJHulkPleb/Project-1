from PyQt5.QtWidgets import *
from RecursionView import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())

    def power(self,x, y):
        if y == 1:
            return x
        else:
            return x * power(x, y - 1)


    def cat_ears(self,n):
        if n == 0:
            return 0
        else:
            return 2 + cat_ears(n - 1)


    def alien_ears(self,n):
        if n == 0:
            return n
        else:
            if n % 2 == 0:
                return 3 + alien_ears(n - 1)
            else:
                return 2 + alien_ears(n - 1)

