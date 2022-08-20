#from tkinter import *
#from tkinter import Tk, Text
#from tkinter.ttk import Frame, Button, Label, Style
#from win32api import GetSystemMetrics
#from PIL import ImageTk, Image

from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_Dialog


if __name__ == "__main__":  
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

