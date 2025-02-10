import webbrowser
from typing import Set

import bpy
from bpy.props import *


class OpenBrowser(bpy.types.Operator):
    bl_idname = 'smc.browser'
    bl_label = bpy.app.translations.pgettext('Open Browser')
    bl_description = bpy.app.translations.pgettext('Click to open in browser')

    link = StringProperty(default='')

    def execute(self, context: bpy.types.Context) -> Set[str]:
        webbrowser.open(self.link)
        self.report({'INFO'}, bpy.app.translations.pgettext('Browser opened'))
        return {'FINISHED'}
