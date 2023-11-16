# IMPORT QT CORE
from qt_core import *

# IMPORT LAYOUT
from res.layout.main_ui import Ui_MainWindow

# IMPORT SETTINGS AND THEME
from res.settings.json_settings import Settings
from res.themes.json_themes import Themes

from . ui_main_window import SetupUIWindow
from . func_main_window import SetupFunctionWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setupObjects()
        SetupUIWindow.setup_ui(self)
        SetupUIWindow.setup_pages_ui(self)
        self.functions = SetupFunctionWindow(self)
    
    def mousePressEvent(self, event):
        self.functions.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.functions.mouseMoveEvent(event)

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        self.functions.resizeGrips()

    def setupObjects(self):
        settings = Settings()
        self.settings = settings.items
        themes = Themes()
        self.themes = themes.items

