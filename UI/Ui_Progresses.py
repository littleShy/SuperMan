# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Personal\Python\taoqianyi\autoDoTheTask\UI\Progresses.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_progressForm(object):
    def setupUi(self, progressForm):
        progressForm.setObjectName("progressForm")
        progressForm.setWindowModality(QtCore.Qt.WindowModal)
        progressForm.resize(328, 226)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Iron_Man1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        progressForm.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(progressForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressStatusLabel = QtWidgets.QLabel(progressForm)
        self.progressStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressStatusLabel.setObjectName("progressStatusLabel")
        self.verticalLayout_2.addWidget(self.progressStatusLabel)
        self.progressTree = QtWidgets.QTreeWidget(progressForm)
        self.progressTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.progressTree.setObjectName("progressTree")
        self.verticalLayout_2.addWidget(self.progressTree)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(progressForm)
        QtCore.QMetaObject.connectSlotsByName(progressForm)

    def retranslateUi(self, progressForm):
        _translate = QtCore.QCoreApplication.translate
        progressForm.setWindowTitle(_translate("progressForm", "任务进度"))
        self.progressStatusLabel.setText(_translate("progressForm", "正在做任务"))
        self.progressTree.headerItem().setText(0, _translate("progressForm", "账号"))
        self.progressTree.headerItem().setText(1, _translate("progressForm", "进度"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progressForm = QtWidgets.QWidget()
    ui = Ui_progressForm()
    ui.setupUi(progressForm)
    progressForm.show()
    sys.exit(app.exec_())

