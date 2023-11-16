# import Qt core
from qt_core import *
from res.layout.main_pages_ui import Ui_MainPages
from widgets import *
from res.themes.app_themes import setupStyleOne

class SetupUIWindow:

    def setup_ui(self):
        # SET STYLE
        self.ui.styleSheet.setStyleSheet(setupStyleOne(self.themes))

        # SET INITIAL PARAMETERS
        self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        self.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # APP TITLE
        self.ui.contentTopTitle.setText(self.settings["app_name"])
        self.ui.version.setText(self.settings["version"])
        self.ui.credits_label.setText(self.settings["copyright"])

        # REMOVE TITLE BAR
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        if self.settings["custom_title_bar"]:
            self.hide_grips = True # Show/Hide resize grips
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

    def setup_pages_ui(self):
        self.ui.load_pages = Ui_MainPages()
        self.ui.load_pages.setupUi(self.ui.content_area_frame)
        self.ui.content_area_layout.addWidget(self.ui.load_pages.pages)

        self.ui.load_pages.pages.setCurrentWidget(self.ui.load_pages.page_home)
