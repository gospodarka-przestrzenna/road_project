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
#from maindialog import MongoConnectorDialog
#from qgis.core import QgsMapLayerRegistry

class Action1(QAction):
    """
    Action for opening dock widget for database connections
    """
    def __init__(self,plugin):
        self.icon_path=path.join(plugin.plugin_path,'images','icon.png')
        self.qicon=QIcon(self.icon_path)
        super(Action1,self).__init__(self.qicon,"&Test action",plugin.iface.mainWindow())
        self.triggered.connect(self.run)

        self.plugin=plugin
        self.iface=plugin.iface

    def run(self):
        """
        Just show/dock Widget/Plugin
        """
        print("DEBUG INFORMATION")

        QMessageBox.information(self.plugin.iface.mainWindow(),
                "Simple Title",
                "Heyy First Plugin",
                QMessageBox.Ok
                )
