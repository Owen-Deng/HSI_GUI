# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classify.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_FrameClassify(object):
    def setupUi(self, FrameClassify):
        if not FrameClassify.objectName():
            FrameClassify.setObjectName(u"FrameClassify")
        FrameClassify.resize(696, 559)
        self.layoutWidget_3 = QWidget(FrameClassify)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 50, 651, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_4 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.pushButton_6 = QPushButton(self.layoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(20, 0))
        self.pushButton_6.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.layoutWidget = QWidget(FrameClassify)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 651, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(20, 0))
        self.pushButton_4.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.groupBox = QGroupBox(FrameClassify)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 180, 651, 261))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 110, 611, 121))
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(90, 30, 121, 22))
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 30, 72, 22))
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 70, 72, 22))
        self.spinBox_6 = QSpinBox(self.groupBox_2)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(90, 70, 121, 22))
        self.spinBox_6.setMaximum(99999)
        self.spinBox_6.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spinBox_6.setValue(960)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 70, 101, 22))
        self.comboBox_4 = QComboBox(self.groupBox_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(310, 70, 51, 22))
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 70, 141, 22))
        self.spinBox_7 = QSpinBox(self.groupBox_2)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(510, 70, 81, 22))
        self.spinBox_7.setMaximum(99999)
        self.spinBox_7.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spinBox_7.setValue(10)
        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(410, 20, 101, 31))
        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(520, 20, 101, 31))
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(550, 67, 61, 22))
        self.spinBox_3.setValue(3)
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(100, 67, 42, 22))
        self.spinBox.setValue(25)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 30, 231, 22))
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(250, 67, 42, 22))
        self.spinBox_2.setValue(7)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 67, 72, 22))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 67, 119, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 71, 41))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 67, 221, 22))
        self.layoutWidget_4 = QWidget(FrameClassify)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 90, 651, 26))
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
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(20, 0))
        self.pushButton_7.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.progressBar = QProgressBar(FrameClassify)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 510, 581, 23))
        self.progressBar.setValue(76)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.progressBar.setFormat(u"%p%")
        self.label_15 = QLabel(FrameClassify)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 510, 72, 22))
        self.pushButton_2 = QPushButton(FrameClassify)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 450, 101, 41))
        self.pushButton_3 = QPushButton(FrameClassify)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(260, 450, 101, 41))
        self.pushButton = QPushButton(FrameClassify)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(20, 450, 101, 41))
        self.layoutWidget_5 = QWidget(FrameClassify)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 130, 651, 26))
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

#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.lineEdit_4)
        self.label.setBuddy(self.lineEdit)
        self.label_10.setBuddy(self.comboBox_2)
        self.label_12.setBuddy(self.spinBox_6)
        self.label_13.setBuddy(self.comboBox_4)
        self.label_14.setBuddy(self.spinBox_7)
        self.label_3.setBuddy(self.spinBox)
        self.label_6.setBuddy(self.spinBox_2)
        self.label_2.setBuddy(self.comboBox)
        self.label_9.setBuddy(self.spinBox_3)
        self.label_8.setBuddy(self.lineEdit_4)
        self.label_11.setBuddy(self.lineEdit_4)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(FrameClassify)

        QMetaObject.connectSlotsByName(FrameClassify)
    # setupUi

    def retranslateUi(self, FrameClassify):
        FrameClassify.setWindowTitle(QCoreApplication.translate("FrameClassify", u"\u9ad8\u5149\u8c31\u56fe\u50cf\u5206\u7c7b", None))
        self.label_7.setText(QCoreApplication.translate("FrameClassify", u"\u8bad\u7ec3\u6743\u91cd\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_4.setText(QCoreApplication.translate("FrameClassify", u"D:\\Weights\\IP\\EmbGCN_Exteneded_RAP.pt", None))
        self.pushButton_6.setText(QCoreApplication.translate("FrameClassify", u"...", None))
        self.label.setText(QCoreApplication.translate("FrameClassify", u"\u56fe\u50cf\u4f4d\u7f6e\uff1a", None))
        self.lineEdit.setText(QCoreApplication.translate("FrameClassify", u"D:\\Datasets\\IP\\Indian_pines_corrected.mat", None))
        self.pushButton_4.setText(QCoreApplication.translate("FrameClassify", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("FrameClassify", u"\u5206\u7c7b\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FrameClassify", u"\u6a21\u578b\u8bbe\u7f6e", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("FrameClassify", u"EmbGCN", None))

        self.label_10.setText(QCoreApplication.translate("FrameClassify", u"\u5206\u7c7b\u6a21\u578b\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("FrameClassify", u"\u5d4c\u5165\u5927\u5c0f\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("FrameClassify", u"\u5d4c\u5165\u5408\u5e76\u65b9\u5f0f\uff1a", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("FrameClassify", u"Max", None))

        self.label_14.setText(QCoreApplication.translate("FrameClassify", u"\u6784\u5efa\u56fe\u65f6\u7684\u8fd1\u90bb\u6570\u91cf\uff1a", None))
        self.pushButton_8.setText(QCoreApplication.translate("FrameClassify", u"\u5bfc\u5165\u8bbe\u7f6e", None))
        self.pushButton_9.setText(QCoreApplication.translate("FrameClassify", u"\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("FrameClassify", u"GPU0: NVIDIA GeForce RTX 3080 Ti", None))

        self.label_3.setText(QCoreApplication.translate("FrameClassify", u"\u56fe\u50cf\u5757\u5927\u5c0f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("FrameClassify", u"\u4e3b\u6210\u5206\uff08PC\uff09\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("FrameClassify", u"\u5206\u7c7b\u8bbe\u5907\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("FrameClassify", u"\u6269\u5c55\u5f62\u6001\u5b66\u5206\u6790\uff08EMP\uff09\u4e2d\u5f00\u95ed\u8fd0\u7b97\u6b21\u6570\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("FrameClassify", u"\u5206\u7c7b\u7ed3\u679c\u4fdd\u5b58\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_5.setText(QCoreApplication.translate("FrameClassify", u"D:\\Results\\IP\\EmbGCN_Exteneded_RAP_Classified.mat", None))
        self.pushButton_7.setText(QCoreApplication.translate("FrameClassify", u"...", None))
        self.label_15.setText(QCoreApplication.translate("FrameClassify", u"\u5206\u7c7b\u8fdb\u5ea6\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("FrameClassify", u"\u6682\u505c\u5206\u7c7b", None))
        self.pushButton_3.setText(QCoreApplication.translate("FrameClassify", u"\u4e2d\u6b62\u5206\u7c7b", None))
        self.pushButton.setText(QCoreApplication.translate("FrameClassify", u"\u5f00\u59cb\u5206\u7c7b", None))
        self.label_11.setText(QCoreApplication.translate("FrameClassify", u"\u6807\u7b7e\u6587\u4ef6\uff08\u53ef\u9009\uff09\uff1a", None))
        self.lineEdit_6.setText(QCoreApplication.translate("FrameClassify", u"D:\\Datasets\\IP\\Indian_pines_gt.mat", None))
        self.pushButton_10.setText(QCoreApplication.translate("FrameClassify", u"...", None))
    # retranslateUi

