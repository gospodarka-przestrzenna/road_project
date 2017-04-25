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

from os import path
from PyQt4.QtGui import QIcon,QMessageBox
from example_plugin_action1 import Action1
from example_plugin_action2 import Action2
from example_plugin_action3 import Action3

class ExamplePluginPlugin(object):
    def __init__(self,iface):
        self.iface=iface
        self.plugin_path=path.dirname(path.abspath(__file__))
        self.plugin_menu_entry="&ExamplePlugin"
        self.menu_actions=[]
        # test requirements

        #adding actions
        self.menu_actions.append(Action1(self))
        self.menu_actions.append(Action2(self))
        self.menu_actions.append(Action3(self))




    def initGui(self):
        """
        Gui initialization and actions adding
        """
        for action in self.menu_actions:
            self.iface.addPluginToMenu(self.plugin_menu_entry,action)

    def unload(self):
        """
        Gui purge
        """
        for action in self.menu_actions:
            self.iface.removePluginMenu(self.plugin_menu_entry,action)
