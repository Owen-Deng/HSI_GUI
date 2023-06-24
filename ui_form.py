# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 662)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(0, 0, 851, 541))
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        self.menu_S = QMenu(self.menubar)
        self.menu_S.setObjectName(u"menu_S")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_L = QMenu(self.menubar)
        self.menu_L.setObjectName(u"menu_L")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_L.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action_Open)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menu.addSeparator()
        self.menu.addAction(self.action_8)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u5149\u8c31\u56fe\u50cf\u5206\u7c7b\u7cfb\u7edf", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5206\u7c7b\u7ed3\u679c", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6&F", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91&E", None))
        self.menu_S.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e&S", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3&T", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b&C", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9&H", None))
        self.menu_L.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe&V", None))
    # retranslateUi

