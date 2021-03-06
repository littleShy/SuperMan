# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Personal\Python\taoqianyi\autoDoTheTask\UI\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 220)
        MainWindow.setMinimumSize(QtCore.QSize(290, 220))
        MainWindow.setMaximumSize(QtCore.QSize(290, 220))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Iron_Man1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.netClassify = QtWidgets.QComboBox(self.groupBox)
        self.netClassify.setMaxCount(50)
        self.netClassify.setObjectName("netClassify")
        self.netClassify.addItem("")
        self.netClassify.addItem("")
        self.netClassify.addItem("")
        self.netClassify.addItem("")
        self.horizontalLayout_3.addWidget(self.netClassify)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.usePlayInterval = QtWidgets.QLabel(self.groupBox)
        self.usePlayInterval.setAlignment(QtCore.Qt.AlignCenter)
        self.usePlayInterval.setObjectName("usePlayInterval")
        self.horizontalLayout_2.addWidget(self.usePlayInterval)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doTaskType = QtWidgets.QComboBox(self.groupBox)
        self.doTaskType.setMaxCount(3)
        self.doTaskType.setObjectName("doTaskType")
        self.doTaskType.addItem("")
        self.doTaskType.addItem("")
        self.doTaskType.addItem("")
        self.horizontalLayout.addWidget(self.doTaskType)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked['bool'].connect(self.groupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SuperMan"))
        self.groupBox.setTitle(_translate("MainWindow", "配置选项"))
        self.label_3.setText(_translate("MainWindow", "网络类型:"))
        self.netClassify.setItemText(0, _translate("MainWindow", "联通"))
        self.netClassify.setItemText(1, _translate("MainWindow", "电信A"))
        self.netClassify.setItemText(2, _translate("MainWindow", "电信B"))
        self.netClassify.setItemText(3, _translate("MainWindow", "电信C"))
        self.usePlayInterval.setToolTip(_translate("MainWindow", "试玩时是否等待5-6分钟"))
        self.usePlayInterval.setText(_translate("MainWindow", "试玩等待:"))
        self.checkBox.setText(_translate("MainWindow", "等待5分钟(推荐)"))
        self.label.setText(_translate("MainWindow", "任务类型:"))
        self.doTaskType.setItemText(0, _translate("MainWindow", "试玩并分享"))
        self.doTaskType.setItemText(1, _translate("MainWindow", "试玩任务"))
        self.doTaskType.setItemText(2, _translate("MainWindow", "分享任务"))
        self.pushButton.setText(_translate("MainWindow", "开始做任务"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

