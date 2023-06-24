# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_result.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_ResultFrame(object):
    def setupUi(self, ResultFrame):
        if not ResultFrame.objectName():
            ResultFrame.setObjectName(u"ResultFrame")
        ResultFrame.resize(681, 632)
        self.layoutWidget_4 = QWidget(ResultFrame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 20, 651, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lineEdit_5 = QLineEdit(self.layoutWidget_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_6.addWidget(self.lineEdit_5)

        self.pushButton_7 = QPushButton(self.layoutWidget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(20, 0))
        self.pushButton_7.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.layoutWidget_5 = QWidget(ResultFrame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 60, 651, 26))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.lineEdit_6 = QLineEdit(self.layoutWidget_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        self.pushButton_10 = QPushButton(self.layoutWidget_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(20, 0))
        self.pushButton_10.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_10)

        self.groupBox = QGroupBox(ResultFrame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 200, 651, 411))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 621, 321))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_l = QLabel(self.layoutWidget)
        self.label_l.setObjectName(u"label_l")
        self.label_l.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_l)

        self.label_r = QLabel(self.layoutWidget)
        self.label_r.setObjectName(u"label_r")
        self.label_r.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_r)

        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(80, 360, 561, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.groupBox_2 = QGroupBox(ResultFrame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 100, 641, 81))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 621, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ResultFrame)

        QMetaObject.connectSlotsByName(ResultFrame)
    # setupUi

    def retranslateUi(self, ResultFrame):
        ResultFrame.setWindowTitle(QCoreApplication.translate("ResultFrame", u"\u9ad8\u5149\u8c31\u56fe\u50cf\u5206\u7c7b\u7ed3\u679c\u9884\u89c8", None))
        self.label_8.setText(QCoreApplication.translate("ResultFrame", u"\u5206\u7c7b\u7ed3\u679c\u4fdd\u5b58\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_5.setText(QCoreApplication.translate("ResultFrame", u"D:\\Results\\IP\\EmbGCN_Exteneded_RAP_Classified.mat", None))
        self.pushButton_7.setText(QCoreApplication.translate("ResultFrame", u"...", None))
        self.label_11.setText(QCoreApplication.translate("ResultFrame", u"\u6807\u7b7e\u6587\u4ef6\uff08\u53ef\u9009\uff09\uff1a", None))
        self.lineEdit_6.setText(QCoreApplication.translate("ResultFrame", u"D:\\Datasets\\IP\\Indian_pines_gt.mat", None))
        self.pushButton_10.setText(QCoreApplication.translate("ResultFrame", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("ResultFrame", u"\u5206\u7c7b\u7ed3\u679c\u9884\u89c8", None))
        self.label_l.setText("")
        self.label_r.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("ResultFrame", u"\u6253\u5370\u5206\u7c7b\u7ed3\u679c", None))
        self.pushButton_3.setText(QCoreApplication.translate("ResultFrame", u"\u6253\u5370\u5bf9\u6bd4\u7ed3\u679c", None))
        self.pushButton.setText(QCoreApplication.translate("ResultFrame", u"\u4fdd\u5b58\u5206\u7c7b\u7ed3\u679c\u5230\u56fe\u7247", None))
        self.pushButton_2.setText(QCoreApplication.translate("ResultFrame", u"\u4fdd\u5b58\u5bf9\u6bd4\u7ed3\u679c\u5230\u56fe\u7247", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ResultFrame", u"\u5206\u7c7b\u7ed3\u679c", None))
        self.label.setText(QCoreApplication.translate("ResultFrame", u"\u6574\u4f53\u7cbe\u5ea6\uff08OA\uff09\uff1a", None))
        self.lineEdit.setText(QCoreApplication.translate("ResultFrame", u"78.79%", None))
        self.label_2.setText(QCoreApplication.translate("ResultFrame", u"\u5e73\u5747\u7cbe\u5ea6\uff08AA\uff09\uff1a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ResultFrame", u"86.62%", None))
        self.label_3.setText(QCoreApplication.translate("ResultFrame", u"Kappa \u7cfb\u6570\uff1a", None))
        self.lineEdit_3.setText(QCoreApplication.translate("ResultFrame", u"76.09%", None))
    # retranslateUi

