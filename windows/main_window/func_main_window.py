from qt_core import *
from core.functions import GlobalFunctions

class SetupFunctionWindow:
        
        def __init__(self, main_window):
            self.main_window = main_window
            self.ui = main_window.ui
            self.settings = main_window.settings
            self.themes = main_window.themes
            self.setupSignals()
        
        # self is MainWindow
        
        def mousePressEvent(self, event):
            if event.buttons() == Qt.LeftButton:
                self.main_window.drag_start_position = event.globalPos() - self.main_window.frameGeometry().topLeft()
                event.accept()

        def mouseMoveEvent(self, event):
            if event.buttons() == Qt.LeftButton:
                self.main_window.move(event.globalPos() - self.main_window.drag_start_position)
                event.accept()
        
        def setupSignals(self):
            self.ui.btn_close.clicked.connect(lambda: self.main_window.close())
            self.ui.btn_minimize.clicked.connect(lambda: self.main_window.showMinimized())
            self.ui.btn_maximize_restore.toggled.connect(lambda checked: self.maximizeRestore(checked))
            self.ui.menu_button.clicked.connect(lambda: self.open_close_frame(
                self.ui.leftMenuFrame, self.settings["lef_menu_size"]['minimum'], self.settings["lef_menu_size"]['maximum'])
            )
            self.ui.btn_menu_home.clicked.connect(lambda: self.btn_clicked(self.ui.btn_menu_home))
            self.ui.btn_menu_settings.clicked.connect(lambda: self.btn_clicked(self.ui.btn_menu_settings))
            self.ui.btn_menu_info.clicked.connect(lambda: self.btn_clicked(self.ui.btn_menu_info))
        
        def btn_clicked(self, btn):
            # GET BUTTON CLICKED
            btn_name = btn.objectName()

            if btn_name == "btn_menu_home":
                self.set_page(self.ui.load_pages.page_home)
                self.select_menu(btn.objectName())
            
            if btn_name == "btn_menu_info":
                self.set_page(self.ui.load_pages.page_info)
                self.select_menu(btn.objectName())
            
            if btn_name == "btn_menu_settings":
                self.set_page(self.ui.load_pages.page_settings)
                self.select_menu(btn.objectName())

            # PRINT BTN NAME
            print(f'Button "{btn_name}" pressed!')


        def set_page(self, page):
            self.ui.load_pages.pages.setCurrentWidget(page)

        def maximizeRestore(self, is_maximized):
            if (is_maximized):
                self.main_window.showMaximized()
                self.ui.btn_maximize_restore.setToolTip("Restore")
                self.ui.btn_maximize_restore.setIcon(QIcon(GlobalFunctions.set_svg_icon("icon_restore.svg")))
                self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            else:
                self.main_window.showNormal()
                self.ui.btn_maximize_restore.setToolTip("Maximize")
                self.ui.btn_maximize_restore.setIcon(QIcon(GlobalFunctions.set_svg_icon("icon_maximize.svg")))
                self.ui.appMargins.setContentsMargins(10, 10, 10, 10)

        def resizeGrips(self):
            self.main_window.left_grip.setGeometry(0, 10, 10, self.main_window.height())
            self.main_window.right_grip.setGeometry(self.main_window.width() - 10, 10, 10, self.main_window.height())
            self.main_window.top_grip.setGeometry(0, 0, self.main_window.width(), 10)
            self.main_window.bottom_grip.setGeometry(0, self.main_window.height() - 10, self.main_window.width(), 10)

        def open_close_frame(self, menu: QFrame, min_widht, max_width):
            width = menu.width()
            
            # SET MAX WIDTH
            if width == 60:
                width_extended = max_width
            else:
                width_extended = min_widht
            
            # ANIMATION
            menu.animation = QPropertyAnimation(menu, b"minimumWidth")
            menu.animation.setDuration(700)
            menu.animation.setStartValue(width)
            menu.animation.setEndValue(width_extended)
            menu.animation.setEasingCurve(QEasingCurve.InOutCubic)
            menu.animation.start()

        # SELECT ONLY ONE BTN MENU
        def select_menu(self, widget: str):
            for btn in self.ui.leftMenu.findChildren(QPushButton):
                if btn.objectName() == widget:
                    
                    MENU_SELECTED_STYLESHEET = f"""
                    #{btn.objectName()} {{
                        background-color:{self.themes["app_color"]["bg_one"]};
                    }}
                    """

                    btn.setStyleSheet(MENU_SELECTED_STYLESHEET)
                else:
                    btn.setStyleSheet("")
                    
            



