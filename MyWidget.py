#from PyQt6.QtGui import
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit
#from PyQt6.QtCore import



class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # create the grid layout
        layout = QGridLayout(self)

        # create the labels and line edits
        label1 = QLabel("Label 1")
        lineedit1 = QLineEdit()
        label2 = QLabel("Label 2")
        lineedit2 = QLineEdit()
        label3 = QLabel("Label 3")
        lineedit3 = QLineEdit()
        label4 = QLabel("Label 4")
        lineedit4 = QLineEdit()

        # add the labels and line edits to the layout
        layout.addWidget(label1, 0, 0)
        layout.addWidget(lineedit1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(lineedit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(lineedit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(lineedit4, 3, 1)