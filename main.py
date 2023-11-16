import sys
from PySide6.QtWidgets import QApplication
from qt_core import *
from core.functions import GlobalFunctions

# IMPORT LAYOUT
from windows.main_window.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(GlobalFunctions.set_image("logo.png")))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())