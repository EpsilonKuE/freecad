#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import os
import FreeCAD
import FreeCADGui as Gui
from .features import ViewProviderGear, involute_gear, involute_gear_rack
from .features import cycloide_gear, bevel_gear, crown_gear


class BaseCommand(object):
    NAME = ""
    GEAR_FUNCTION = None
    ICONDIR = os.path.join(os.path.dirname(__file__), "icons")

    def __init__(self):
        pass

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True

    def Activated(self):
        Gui.doCommandGui("import freecad.gears.commands")
        Gui.doCommandGui("freecad.gears.commands.{}.create()".format(self.__class__.__name__))
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")

    @classmethod
    def create(cls):
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", cls.NAME)
        cls.GEAR_FUNCTION(obj)
        ViewProviderGear(obj.ViewObject)
        return obj

    def GetResources(self):
        return {'Pixmap': self.Pixmap, 
                'MenuText': self.MenuText, 
                'ToolTip': self.ToolTip}


class CreateInvoluteGear(BaseCommand):
    NAME = "InvoluteGear"
    GEAR_FUNCTION = involute_gear
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'involutegear.svg')
    MenuText = 'involute gear'
    ToolTip = 'involute gear'

class CreateInvoluteRack(BaseCommand):
    NAME = "InvoluteRack"
    GEAR_FUNCTION = involute_gear_rack
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'involuterack.svg')
    MenuText = 'involute rack'
    ToolTip = 'involute rack'

class CreateCrownGear(BaseCommand):
    NAME = "CrownGear"
    GEAR_FUNCTION = crown_gear
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'crowngear.svg')
    MenuText = 'crown gear'
    ToolTip = 'crown gear'

class CreateCycloideGear(BaseCommand):
    NAME = "CycloidGear"
    GEAR_FUNCTION = cycloide_gear
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'cycloidegear.svg')
    MenuText = 'cycloide gear'
    ToolTip = 'cycloide gear'

class CreateBevelGear(BaseCommand):
    NAME = "BevelGear"
    GEAR_FUNCTION = bevel_gear
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'bevelgear.svg')
    MenuText = 'bevel gear'
    ToolTip = 'bevel gear'
