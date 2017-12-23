from UI import Ui_Progresses
from PyQt5 import QtWidgets,  QtTreeView
import sys

app = QtWidgets.QApplication(sys.argv)
progressForm = QtWidgets.QWidget()
ui = Ui_Progresses.Ui_progressForm()
ui.setupUi(progressForm)
progressForm.show()
sys.exit(app.exec_())
