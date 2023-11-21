# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 720)
        MainWindow.setMinimumSize(QSize(1200, 720))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.bgApp)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(60, 0))
        self.leftMenuFrame.setMaximumSize(QSize(60, 16777215))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuFrame)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 40))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 40))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(60, 10, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QLabel(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(15, 6, 30, 30))
        self.topLogo.setMinimumSize(QSize(30, 30))
        self.topLogo.setMaximumSize(QSize(30, 30))
        self.topLogo.setPixmap(QPixmap(u":/images/res/images/logo.ico"))
        self.topLogo.setScaledContents(True)
        self.topLogo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenu = QFrame(self.leftMenuFrame)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenu)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenu)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.toggleBox)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMinimumSize(QSize(0, 45))
        self.menu_button.setFont(font)
        self.menu_button.setLayoutDirection(Qt.LeftToRight)
        self.menu_button.setCheckable(True)

        self.verticalLayout_4.addWidget(self.menu_button)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.leftMenuTopFrame = QFrame(self.leftMenu)
        self.leftMenuTopFrame.setObjectName(u"leftMenuTopFrame")
        self.leftMenuTopFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuTopFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuTopFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.leftMenuTopFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_home = QPushButton(self.leftMenuTopFrame)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        sizePolicy.setHeightForWidth(self.btn_menu_home.sizePolicy().hasHeightForWidth())
        self.btn_menu_home.setSizePolicy(sizePolicy)
        self.btn_menu_home.setMinimumSize(QSize(0, 45))

        self.verticalLayout_8.addWidget(self.btn_menu_home)

        self.btn_menu_info = QPushButton(self.leftMenuTopFrame)
        self.btn_menu_info.setObjectName(u"btn_menu_info")
        sizePolicy.setHeightForWidth(self.btn_menu_info.sizePolicy().hasHeightForWidth())
        self.btn_menu_info.setSizePolicy(sizePolicy)
        self.btn_menu_info.setMinimumSize(QSize(0, 45))

        self.verticalLayout_8.addWidget(self.btn_menu_info)


        self.verticalMenuLayout.addWidget(self.leftMenuTopFrame, 0, Qt.AlignTop)

        self.leftMenuBottomFrame = QFrame(self.leftMenu)
        self.leftMenuBottomFrame.setObjectName(u"leftMenuBottomFrame")
        self.leftMenuBottomFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuBottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.leftMenuBottomFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_settings = QPushButton(self.leftMenuBottomFrame)
        self.btn_menu_settings.setObjectName(u"btn_menu_settings")
        sizePolicy.setHeightForWidth(self.btn_menu_settings.sizePolicy().hasHeightForWidth())
        self.btn_menu_settings.setSizePolicy(sizePolicy)
        self.btn_menu_settings.setMinimumSize(QSize(0, 45))
        self.btn_menu_settings.setFont(font)
        self.btn_menu_settings.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.btn_menu_settings)


        self.verticalMenuLayout.addWidget(self.leftMenuBottomFrame, 0, Qt.AlignBottom)

        self.leftMenuBottomFrame.raise_()
        self.toggleBox.raise_()
        self.leftMenuTopFrame.raise_()

        self.verticalLayout_3.addWidget(self.leftMenu)


        self.appLayout.addWidget(self.leftMenuFrame)

        self.contentFrame = QFrame(self.bgApp)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.NoFrame)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentFrameTop = QFrame(self.contentFrame)
        self.contentFrameTop.setObjectName(u"contentFrameTop")
        self.contentFrameTop.setMinimumSize(QSize(0, 40))
        self.contentFrameTop.setMaximumSize(QSize(16777215, 40))
        self.contentFrameTop.setFrameShape(QFrame.NoFrame)
        self.contentFrameTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentFrameTop)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.contentTopTitleFrame = QFrame(self.contentFrameTop)
        self.contentTopTitleFrame.setObjectName(u"contentTopTitleFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentTopTitleFrame.sizePolicy().hasHeightForWidth())
        self.contentTopTitleFrame.setSizePolicy(sizePolicy1)
        self.contentTopTitleFrame.setFrameShape(QFrame.NoFrame)
        self.contentTopTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.contentTopTitleFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.contentTopTitle = QLabel(self.contentTopTitleFrame)
        self.contentTopTitle.setObjectName(u"contentTopTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentTopTitle.sizePolicy().hasHeightForWidth())
        self.contentTopTitle.setSizePolicy(sizePolicy2)
        self.contentTopTitle.setMaximumSize(QSize(16777215, 45))
        self.contentTopTitle.setFont(font)
        self.contentTopTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.contentTopTitle)

        self.btn_connect = QPushButton(self.contentTopTitleFrame)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(70, 30))
        self.btn_connect.setMaximumSize(QSize(70, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/res/icons/icon_widgets.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect.setIcon(icon)
        self.btn_connect.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_connect)


        self.horizontalLayout.addWidget(self.contentTopTitleFrame)

        self.contentTopButtonsFrame = QFrame(self.contentFrameTop)
        self.contentTopButtonsFrame.setObjectName(u"contentTopButtonsFrame")
        self.contentTopButtonsFrame.setMinimumSize(QSize(0, 28))
        self.contentTopButtonsFrame.setFrameShape(QFrame.NoFrame)
        self.contentTopButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopButtonsFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.contentTopButtonsFrame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(28, 28))
        self.btn_minimize.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/icons/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.contentTopButtonsFrame)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        self.btn_maximize_restore.setMinimumSize(QSize(28, 28))
        self.btn_maximize_restore.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.btn_maximize_restore.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/icons/icon_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)
        self.btn_maximize_restore.setIconSize(QSize(10, 10))
        self.btn_maximize_restore.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.contentTopButtonsFrame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setMouseTracking(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/res/icons/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.contentTopButtonsFrame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentFrameTop)

        self.contentFrameBottom = QFrame(self.contentFrame)
        self.contentFrameBottom.setObjectName(u"contentFrameBottom")
        self.contentFrameBottom.setFrameShape(QFrame.NoFrame)
        self.contentFrameBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentFrameBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentFrameBottom)
        self.content.setObjectName(u"content")
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.content_area_frame = QFrame(self.content)
        self.content_area_frame.setObjectName(u"content_area_frame")
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setSpacing(0)
        self.content_area_layout.setObjectName(u"content_area_layout")
        self.content_area_layout.setContentsMargins(10, 10, 10, 10)

        self.horizontalLayout_4.addWidget(self.content_area_frame)

        self.rightBoxFrame = QFrame(self.content)
        self.rightBoxFrame.setObjectName(u"rightBoxFrame")
        self.rightBoxFrame.setMinimumSize(QSize(0, 0))
        self.rightBoxFrame.setMaximumSize(QSize(0, 16777215))
        self.rightBoxFrame.setFrameShape(QFrame.NoFrame)
        self.rightBoxFrame.setFrameShadow(QFrame.Raised)
        self.rightMenuLayout = QVBoxLayout(self.rightBoxFrame)
        self.rightMenuLayout.setSpacing(0)
        self.rightMenuLayout.setObjectName(u"rightMenuLayout")
        self.rightMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.rightBox = QFrame(self.rightBoxFrame)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setFrameShape(QFrame.NoFrame)
        self.rightBox.setFrameShadow(QFrame.Raised)
        self.contentRightMenuLayout = QVBoxLayout(self.rightBox)
        self.contentRightMenuLayout.setSpacing(0)
        self.contentRightMenuLayout.setObjectName(u"contentRightMenuLayout")
        self.contentRightMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.rightBox)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.contentRightMenuLayout.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.rightMenuLayout.addWidget(self.rightBox)


        self.horizontalLayout_4.addWidget(self.rightBoxFrame)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentFrameBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.credits_label = QLabel(self.bottomBar)
        self.credits_label.setObjectName(u"credits_label")
        self.credits_label.setMaximumSize(QSize(16777215, 16))
        self.credits_label.setFont(font)
        self.credits_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.credits_label)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentFrameBottom)


        self.appLayout.addWidget(self.contentFrame)

        self.contentFrame.raise_()
        self.leftMenuFrame.raise_()

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.topLogo.setText("")
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"Hide Menu", None))
        self.btn_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.btn_menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.contentTopTitle.setText(QCoreApplication.translate("MainWindow", u"Modern Gui Python APP", None))
        self.btn_connect.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.credits_label.setText(QCoreApplication.translate("MainWindow", u"By: Alireza Abbasian", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

