# -*- coding: utf-8 -*-

"""
Module implementing progressForm.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_Progresses import Ui_progressForm


class progressForm(QWidget, Ui_progressForm):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(progressForm, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(QModelIndex)
    def on_progressTree_expanded(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        raise NotImplementedError
