import numpy as np
import PySide6
import PySide6.QtWidgets as QtWidgets
import spectral
from PIL import Image
from PySide6.QtGui import QActionEvent, QIcon, QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QFileDialog, QFrame, QMainWindow,
                               QMdiSubWindow, QMenu, QMenuBar, QStyleFactory)

import utils as ut
from ui_classify import Ui_FrameClassify
from ui_form import Ui_MainWindow
from ui_preview import Ui_PreviewFrame
from ui_preview_result import Ui_ResultFrame
from ui_train import Ui_TrainFrame


def scale_image( width, height, box_width, box_height):
    # Determine the aspect ratio of the image
    aspect_ratio = width / height

    # Determine the aspect ratio of the box
    box_aspect_ratio = box_width / box_height

    # If the image is wider than the box
    if aspect_ratio > box_aspect_ratio:
        # Scale the image to fit the width of the box
        new_width = box_width
        new_height = new_width / aspect_ratio
    # If the image is taller than the box
    else:
        # Scale the image to fit the height of the box
        new_height = box_height
        new_width = new_height * aspect_ratio

    return int(new_width), int(new_height)

def get_pixmap(img, lw, lh):
    img_w, img_h = img.shape[1], img.shape[0]
    qimgl = QImage(img,img.shape[1],img.shape[0],img.strides[0],QImage.Format.Format_BGR888)
    nw, nl = scale_image(img_w, img_h, lw,lh)
    qpixl = QPixmap.fromImage(qimgl).scaled(nw,nl)

    return qpixl

class ResultFrame(QFrame, Ui_ResultFrame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ini_width = self.width()
        self.ini_height = self.height() + 30
    
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        parent =  self.parent()
        parent.resize(self.ini_width,self.ini_height)
        
        classified = Image.open(r"D:\OneDrive\Projects\HSI_FSL\output\figures\IP\EmbGCN+RAP_82.77.jpg")
        gt = Image.open(r"D:\OneDrive\Projects\HSI_FSL\output\figures\IP\ground_truth.jpg")
        classified = np.array(classified)
        gt = np.array(gt)

        lrw,lrh = self.label_r.width(),  self.label_r.height()
        llw,llh = self.label_l.width(),  self.label_l.height()

        qpixl = get_pixmap(classified, lrw, lrh)
        qpixr = get_pixmap(gt, llw, llh)
        self.label_l.setPixmap(qpixl)
        self.label_r.setPixmap(qpixr)
        return super().showEvent(event)
    

class ClassifyFrame(QFrame, Ui_FrameClassify):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ini_width = self.width()
        self.ini_height = self.height() + 30
    
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        parent =  self.parent()
        parent.resize(self.ini_width,self.ini_height)
        return super().showEvent(event)
        
class TrainFrame(QFrame, Ui_TrainFrame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ini_width = self.width()
        self.ini_height = self.height() + 30
    
    
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        parent =  self.parent()
        parent.resize(self.ini_width,self.ini_height)
        return super().showEvent(event)
    
class PreviewFrame(QFrame, Ui_PreviewFrame):
    def __init__(self,filename):
        super().__init__()
        self.setupUi(self)
        self.ini_width = self.width()
        self.ini_height = self.height() + 30
        self.lineEdit.setText(filename)
    
        self.hsi, self.gt = ut.load_dataset('IP',"D:\\Datasets")
        self.lineEdit_h.setText(str(self.hsi.shape[0]))
        self.lineEdit_w.setText(str(self.hsi.shape[1]))
        self.lineEdit_band.setText(str(self.hsi.shape[2]))

        self.lineEdit_r.textChanged.connect(self.textChanged)
        self.lineEdit_g.textChanged.connect(self.textChanged)
        self.lineEdit_b.textChanged.connect(self.textChanged)
        self.pushButton_train.clicked.connect(self.OnpushButton_train)
        self.pushButton_classify.clicked.connect(self.OnpushButton_classify)
        self.textChanged()

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        parent =  self.parent()
        parent.resize(self.ini_width,self.ini_height)
        return super().showEvent(event)
        
    def OnpushButton_train(self):
        main_window = self.parent().parent().parent().parent()
        qsub = QMdiSubWindow(main_window)
        qsub.setWidget(TrainFrame())
        qsub.setWindowIcon(QIcon('icon.png'))
        main_window.mdiArea.addSubWindow(qsub)
        qsub.show()
    
    def OnpushButton_classify(self):
        main_window = self.parent().parent().parent().parent()
        qsub = QMdiSubWindow(main_window)
        qsub.setWidget(ClassifyFrame())
        qsub.setWindowIcon(QIcon('icon.png'))
        geo = main_window.mdiArea.geometry()
        w,h = geo.width(), geo.height()
        qsub.resize(w-20,h-20)
        main_window.mdiArea.addSubWindow(qsub)
        qsub.show()
    
    def textChanged(self):
        r_text = self.lineEdit_r.text()
        g_text = self.lineEdit_g.text()
        b_text = self.lineEdit_b.text()
        if not r_text or not g_text or not b_text:
            return
        
        r_band = int(self.lineEdit_r.text())
        g_band = int(self.lineEdit_g.text())
        b_band = int(self.lineEdit_b.text())

        lw,lh = self.label_img.width(),  self.label_img.height()
        
        rgb = (spectral.get_rgb(self.hsi,bands=(r_band,g_band,b_band))*255).astype(np.uint8)
        img_w, img_h = rgb.shape[1], rgb.shape[0]
        qimg = QImage(rgb,rgb.shape[1],rgb.shape[0],rgb.strides[0],QImage.Format.Format_BGR888)
        nw, nl = scale_image(img_w, img_h, lw,lh)
        qpix = QPixmap.fromImage(qimg).scaled(nw,nl)
        self.label_img.setPixmap(qpix)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setCentralWidget(self.mdiArea)

        self.action_Open.triggered.connect(self.OpenFile)
        
        self.add_subwindow(PreviewFrame,r'D:\Datasets\IP\Indian_pines_corrected.mat')

        self.add_subwindow(TrainFrame)
        self.add_subwindow(ClassifyFrame)
        self.add_subwindow(ResultFrame)
    
    def OpenFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"选择一个高光谱图像","D:\\Datasets\\IP","高光谱图像(*.mat)", options=options)
        if not fileName:
            return 
        
        self.add_subwindow(PreviewFrame,fileName)
        
    def add_subwindow(self, FrameClass, *args):
        qsub = QMdiSubWindow(self)
        qsub.setWidget(FrameClass(*args))
        qsub.setWindowIcon(QIcon('icon.png'))
        self.mdiArea.addSubWindow(qsub)
        qsub.show()
        
        
if __name__ == '__main__':
    app = QApplication()
    main_wind = MainWindow()
    main_wind.show()
    app.exec()
        