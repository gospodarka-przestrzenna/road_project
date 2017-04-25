# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2015 Maciej Kamiński (kaminski.maciej@gmail.com) Politechnika Wrocławska
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
###############################################################################
__author__ = 'Maciej Kamiński Politechnika Wrocławska'


from PyQt4.QtGui import QIcon,QAction,QMessageBox,QApplication
from PyQt4.QtCore import Qt,QBasicTimer
from os import path

#from dialog import Dialog
#from dialog import Dialog
from dialog2 import Dialog2
#from maindialog import MongoConnectorDialog
#from qgis.core import QgsMapLayerRegistry

class Action2(QAction):
    """
    Action for opening dock widget for database connections
    """
    def __init__(self,plugin):
        self.icon_path=path.join(plugin.plugin_path,'images','icon2.png')
        self.qicon=QIcon(self.icon_path)
        super(Action2,self).__init__(self.qicon,"A&dvancet action with window and two buttons",plugin.iface.mainWindow())
        self.triggered.connect(self.run)
        self.plugin=plugin
        self.iface=plugin.iface

        #self.dlg=Dialog2()
        #self.dlg.calculate_sum.clicked.connect(self.ok)
        #self.dlg.cancel.clicked.connect(self.cancel)

    def run(self):
        """
        Just show/dock Widget/Plugin
        """
        self.dlg=Dialog2()
        self.dlg.calculate_sum.clicked.connect(self.ok)
        self.dlg.calculate_sum.clicked.connect(self.ok2)
        self.dlg.cancel.clicked.connect(self.cancel)

        self.dlg.show()

    def ok(self):
        try:
            l1=int(self.dlg.number_1.text())
            l2=int(self.dlg.number_2.text())
            QMessageBox.information(self.plugin.iface.mainWindow(),
                    "Sum",
                    "Sum is: "+str(l1+l2),
                    QMessageBox.Ok
                    )
        except:
            QMessageBox.information(self.plugin.iface.mainWindow(),
                    "Sum",
                    "Number is not convertable",
                    QMessageBox.Ok
                    )
        #self.dlg.number_1.setText("")
        #self.dlg.number_2.setText("")
        self.dlg.close()

    def ok2(self):
        print("hello from ok")

    def cancel(self):
        self.dlg.close()
