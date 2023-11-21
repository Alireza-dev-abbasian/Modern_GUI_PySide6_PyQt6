# import Qt core
from qt_core import *
from res.layout.main_pages_ui import Ui_MainPages
from widgets import *
from res.themes.app_themes import setupStyleOne

class SetupUIWindow:

    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.settings = main_window.settings
        self.themes = main_window.themes
        self.setup_ui()
        self.setup_pages_ui()

    def setup_ui(self):
        # SET STYLE
        self.ui.styleSheet.setStyleSheet(setupStyleOne(self.themes))

        # SET INITIAL PARAMETERS
        self.main_window.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        self.main_window.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # APP TITLE
        self.ui.contentTopTitle.setText(self.settings["app_name"])
        self.ui.version.setText(self.settings["version"])
        self.ui.credits_label.setText(self.settings["copyright"])

        # REMOVE TITLE BAR
        if self.settings["custom_title_bar"]:
            self.main_window.setWindowFlag(Qt.FramelessWindowHint)
            self.main_window.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        if self.settings["custom_title_bar"]:
            self.main_window.hide_grips = True # Show/Hide resize grips
            self.main_window.left_grip = PyGrips(self.main_window, "left", self.main_window.hide_grips)
            self.main_window.right_grip = PyGrips(self.main_window, "right", self.main_window.hide_grips)
            self.main_window.top_grip = PyGrips(self.main_window, "top", self.main_window.hide_grips)
            self.main_window.bottom_grip = PyGrips(self.main_window, "bottom", self.main_window.hide_grips)
            self.main_window.top_left_grip = PyGrips(self.main_window, "top_left", self.main_window.hide_grips)
            self.main_window.top_right_grip = PyGrips(self.main_window, "top_right", self.main_window.hide_grips)
            self.main_window.bottom_left_grip = PyGrips(self.main_window, "bottom_left", self.main_window.hide_grips)
            self.main_window.bottom_right_grip = PyGrips(self.main_window, "bottom_right", self.main_window.hide_grips)

    def setup_pages_ui(self):
        self.ui.load_pages = Ui_MainPages()
        self.ui.load_pages.setupUi(self.ui.content_area_frame)
        self.ui.content_area_layout.addWidget(self.ui.load_pages.pages)

        self.ui.load_pages.pages.setCurrentWidget(self.ui.load_pages.page_home)
