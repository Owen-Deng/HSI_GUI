# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_PreviewFrame(object):
    def setupUi(self, PreviewFrame):
        if not PreviewFrame.objectName():
            PreviewFrame.setObjectName(u"PreviewFrame")
        PreviewFrame.resize(751, 585)
        self.groupBox = QGroupBox(PreviewFrame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 110, 711, 361))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 49, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 100, 49, 20))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 130, 49, 16))
        self.lineEdit_r = QLineEdit(self.groupBox)
        self.lineEdit_r.setObjectName(u"lineEdit_r")
        self.lineEdit_r.setGeometry(QRect(60, 70, 81, 22))
        self.lineEdit_g = QLineEdit(self.groupBox)
        self.lineEdit_g.setObjectName(u"lineEdit_g")
        self.lineEdit_g.setGeometry(QRect(60, 100, 81, 22))
        self.lineEdit_b = QLineEdit(self.groupBox)
        self.lineEdit_b.setObjectName(u"lineEdit_b")
        self.lineEdit_b.setGeometry(QRect(60, 130, 81, 22))
        self.label_img = QLabel(self.groupBox)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setGeometry(QRect(160, 20, 531, 321))
        self.label_img.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 40, 89, 20))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 160, 121, 20))
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 210, 121, 41))
        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 270, 121, 41))
        self.widget = QWidget(PreviewFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 651, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(20, 0))
        self.pushButton_4.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.widget1 = QWidget(PreviewFrame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 70, 411, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_h = QLineEdit(self.widget1)
        self.lineEdit_h.setObjectName(u"lineEdit_h")

        self.horizontalLayout_2.addWidget(self.lineEdit_h)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_w = QLineEdit(self.widget1)
        self.lineEdit_w.setObjectName(u"lineEdit_w")

        self.horizontalLayout_2.addWidget(self.lineEdit_w)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_band = QLineEdit(self.widget1)
        self.lineEdit_band.setObjectName(u"lineEdit_band")

        self.horizontalLayout_2.addWidget(self.lineEdit_band)

        self.widget2 = QWidget(PreviewFrame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 500, 691, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy1)
        self.widget2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_train = QPushButton(self.widget2)
        self.pushButton_train.setObjectName(u"pushButton_train")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_train.sizePolicy().hasHeightForWidth())
        self.pushButton_train.setSizePolicy(sizePolicy2)
        self.pushButton_train.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_train)

        self.pushButton_classify = QPushButton(self.widget2)
        self.pushButton_classify.setObjectName(u"pushButton_classify")
        sizePolicy2.setHeightForWidth(self.pushButton_classify.sizePolicy().hasHeightForWidth())
        self.pushButton_classify.setSizePolicy(sizePolicy2)
        self.pushButton_classify.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_classify)


        self.retranslateUi(PreviewFrame)

        QMetaObject.connectSlotsByName(PreviewFrame)
    # setupUi

    def retranslateUi(self, PreviewFrame):
        PreviewFrame.setWindowTitle(QCoreApplication.translate("PreviewFrame", u"\u9ad8\u5149\u8c31\u56fe\u50cf\u9884\u89c8", None))
        self.groupBox.setTitle(QCoreApplication.translate("PreviewFrame", u"\u4f2a\u5f69\u8272\u56fe\u50cf\u9884\u89c8", None))
        self.label_5.setText(QCoreApplication.translate("PreviewFrame", u"R", None))
        self.label_6.setText(QCoreApplication.translate("PreviewFrame", u"G", None))
        self.label_7.setText(QCoreApplication.translate("PreviewFrame", u"B", None))
        self.lineEdit_r.setText(QCoreApplication.translate("PreviewFrame", u"0", None))
        self.lineEdit_g.setText(QCoreApplication.translate("PreviewFrame", u"15", None))
        self.lineEdit_b.setText(QCoreApplication.translate("PreviewFrame", u"25", None))
        self.label_img.setText("")
        self.radioButton.setText(QCoreApplication.translate("PreviewFrame", u"\u9009\u62e9\u6ce2\u6bb5\u9884\u89c8", None))
        self.radioButton_2.setText(QCoreApplication.translate("PreviewFrame", u"\u4e09\u4e2a\u4e3b\u6210\u5206\u9884\u89c8", None))
        self.pushButton_5.setText(QCoreApplication.translate("PreviewFrame", u"\u4fdd\u5b58\u5f53\u524d\u9884\u89c8\u56fe\u7247", None))
        self.pushButton_6.setText(QCoreApplication.translate("PreviewFrame", u"\u6253\u5370\u5f53\u524d\u9884\u89c8\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("PreviewFrame", u"\u56fe\u50cf\u4f4d\u7f6e\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("PreviewFrame", u"...", None))
        self.label_2.setText(QCoreApplication.translate("PreviewFrame", u"\u5bbd\u5ea6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("PreviewFrame", u"\u9ad8\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("PreviewFrame", u"\u6ce2\u6bb5\u6570\uff1a", None))
        self.pushButton_train.setText(QCoreApplication.translate("PreviewFrame", u"\u9ad8\u5149\u8c31\u5206\u7c7b\u6a21\u578b\u8bad\u7ec3", None))
        self.pushButton_classify.setText(QCoreApplication.translate("PreviewFrame", u"\u9ad8\u5149\u8c31\u56fe\u50cf\u5206\u7c7b", None))
    # retranslateUi

