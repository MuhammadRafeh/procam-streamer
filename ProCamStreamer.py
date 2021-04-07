import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 461))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/MainWindow/latest.png"))
        self.label.setObjectName("label")
        self.stream = QtWidgets.QPushButton(self.centralwidget)
        self.stream.setGeometry(QtCore.QRect(40, 370, 201, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.stream.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.stream.setFont(font)
        self.stream.setStyleSheet("")
        self.stream.setObjectName("stream")
        self.streamurl = QtWidgets.QLineEdit(self.centralwidget)
        self.streamurl.setGeometry(QtCore.QRect(40, 190, 491, 41))
        self.streamurl.setObjectName("streamurl")
        self.appname = QtWidgets.QLineEdit(self.centralwidget)
        self.appname.setGeometry(QtCore.QRect(40, 280, 121, 41))
        self.appname.setText("")
        self.appname.setObjectName("appname")
        self.streamname = QtWidgets.QLineEdit(self.centralwidget)
        self.streamname.setGeometry(QtCore.QRect(260, 280, 121, 41))
        self.streamname.setObjectName("streamname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.stream.setStyleSheet('QPushButton {background-color: #808080; color: white;}')
        self.streamname.setStyleSheet("QLineEdit {background-color: grey; color: white; border: 1px solid white;}")
        self.appname.setStyleSheet("QLineEdit {background-color: grey; color: white; border: 1px solid white;}")
        self.streamurl.setStyleSheet("QLineEdit {background-color: grey; color: white; border: 1px solid white;}")
        #self.streamurl.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        #self.streamurl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
        #self.streamurl.setFocus(QtCore.Qt.StrongFocus)
        #self.stream.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        MainWindow.setFixedSize(719,480) #Now, we can't resize window
        self.stream.clicked.connect(self.streambutton) #Event Connected to the Stream Button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stream.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#75507b;\">asd</span><span style=\" font-weight:600; color:#75507b;\">s</span></p></body></html>"))
        self.stream.setText(_translate("MainWindow", "Stream"))

    def streambutton(self):
        url = self.streamurl.text()
        app = self.appname.text()
        streamtext = self.streamname.text()
        argument = f"""ffmpeg -f v4l2 -framerate 30 -video_size 640x480 -input_format yuyv422
         -i /dev/video0 -f alsa -i hw:1 -vcodec h264_omx -pix_fmt yuv420p -b:v 1.5M -b:a 128k
          -ar 44100 -acodec aac -f rtsp -rtsp_transport tcp -muxdelay .1 {url}{app}{streamtext}
           -f matroska -codec copy pipe:1|ffplay -fflags nobuffer -hide_banner -window_title PlayerCamPro -x 490 -y 330 -an -i pipe:0"""
        subprocess.call(argument,shell=True)
        
import pic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    MainWindow.setWindowTitle("ProCamStreamer")
    MainWindow.show()
    
    sys.exit(app.exec_())

