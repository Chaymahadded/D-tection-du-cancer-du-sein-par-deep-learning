import pickle
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QFileDialog, QLabel, QWidget
from PyQt5.uic import loadUi
import resources_rc


class Login(QWidget):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.label.setStyleSheet(u"\n"
                                 "border-image: url(image3.png);\n"
                                 "border-top-left-radius: 50px;")
        self.pushButton.clicked.connect(self.gototest)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_7.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.lineEdit.text()
        password=self.lineEdit_2.text()
        print("Successfully logged in with email: ", email, "and password:", password)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gototest(self):
        test = Test()
        widget.addWidget(test)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QWidget):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.label.setStyleSheet(u"\n"
                                 "border-image: url(image3.png);\n"
                                 "border-top-left-radius: 50px;")
        self.pushButton.clicked.connect(self.gototest)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.lineEdit_6.text()==self.lineEdit_7.text():
            password=self.lineEdit_6.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
    def gototest(self):
        test = Test()
        widget.addWidget(test)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Test(QWidget):
    def __init__(self):
        super(Test,self).__init__()
        loadUi("main.ui",self)
        self.label.setStyleSheet(u"\n"
                                 "border-image: url(image3.png);\n"
                                 "border-top-left-radius: 50px;")
        self.pushButton.clicked.connect(self.chooseFileFunction)
        self.pushButton_6.clicked.connect(self.testImage)


    def chooseFileFunction(self):
        self.home_dir = str(Path.home())
        self.imagePath = QFileDialog.getOpenFileName(self, 'Open', self.home_dir)[0]
        self.lineEdit.setText(self.imagePath)
        label = QLabel()
        pixmap = QPixmap(self.imagePath)
        label.setPixmap(pixmap)
        print(self.imagePath)


    def testImage(self):
        #image=self.imagePath
        message = ""
        model = 'model/model.h5'
        model_path = 'model/modelSVM.h5'

        import numpy as np
        import cv2
        from keract import get_activations
        import tensorflow as tf
        import tensorflow_hub as hub
        from keras.layers import Flatten
        loaded_model = pickle.load(open(model_path, 'rb'))
        loded_model_cnn = tf.keras.models.load_model(model)
        # image = cv2.imread("../SOB_B_A-14-22549AB-400-001.png")
        #print(self.imagePath)
        image = cv2.imread(self.imagePath)
        #image = cv2.imread(image)
        image = cv2.resize(image, (256, 128))
        image = np.expand_dims(image, 0)
        image = get_activations(loded_model_cnn, image, layer_names='flatten')
        image = image['flatten']
        image = np.array(image.reshape(1, 1792))
        image = np.asmatrix(image)
        print(image)
        pred = loaded_model.predict(image)
        print(pred)

        if pred == 1:
            message = " La tumeur est Maligne "
        else:
            message = "La tumeur est benigne "
        self.label_5.setText(message)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(600)
widget.setFixedHeight(600)
widget.show()
app.exec()