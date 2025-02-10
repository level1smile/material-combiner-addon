from typing import Optional
from typing import Set

import bpy
from bpy.props import IntProperty

from .. import globs
from ..utils.images import get_image
from ..utils.materials import get_shader_type
from ..utils.materials import shader_image_nodes
from ..utils.textures import get_texture


class PropertyMenu(bpy.types.Operator):
    bl_label = bpy.app.translations.pgettext('Settings for material:')
    bl_idname = 'smc.property_menu'
    bl_description = bpy.app.translations.pgettext('Show settings for this material')
    bl_options = {'UNDO', 'INTERNAL'}

    list_id = IntProperty(default=0)

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> Set:
        scn = context.scene
        dpi = bpy.context.preferences.system.dpi if globs.is_blender_2_80_or_newer else bpy.context.user_preferences.system.dpi
        wm = context.window_manager
        scn.smc_list_id = self.list_id
        return wm.invoke_props_dialog(self, width=dpi * 4)

    def check(self, context: bpy.types.Context) -> bool:
        return True

    def execute(self, context: bpy.types.Context) -> Set[str]:
        return {'FINISHED'}

    def draw(self, context: bpy.types.Context) -> None:
        scn = context.scene
        item = scn.smc_ob_data[scn.smc_list_id]
        if globs.is_blender_2_80_or_newer:
            node_tree = item.mat.node_tree if item.mat else None
            image = None
            shader = get_shader_type(item.mat) if item.mat else None
            node_name = shader_image_nodes.get(shader)
            if node_name:
                image = node_tree.nodes[node_name].image
        else:
            image = get_image(get_texture(item.mat))
        col = self.layout.column()
        col.scale_y = 1.2
        col.prop(item.mat, 'name', text='', icon_value=item.mat.preview.icon_id)
        if image:
            self._show_image(col, image)
            self._show_diffuse_color(col, item, image)
            self._show_size_settings(col, item)
        else:
            col.label(text=bpy.app.translations.pgettext('Image size: {0}x{0}px').format(scn.smc_diffuse_size))
            self._show_diffuse_color(col, item)

    @staticmethod
    def _show_image(col: bpy.types.UILayout, image: bpy.types.Image) -> None:
        if globs.is_blender_3_or_newer and not image.preview:
            image.preview_ensure()
        row = col.row()
        image_name = '{0}...'.format(image.name[:16]) if len(image.name) > 16 else image.name
        row.label(text=image_name, icon_value=image.preview.icon_id)
        row.alignment = 'RIGHT'
        row.label(text=bpy.app.translations.pgettext('Size: {0}x{1}px').format(*image.size))

    @staticmethod
    def _show_diffuse_color(col: bpy.types.UILayout, item: bpy.types.PropertyGroup,
                            image: Optional[bpy.types.Image] = None) -> None:
        if globs.is_blender_2_79_or_older:
            col.prop(item.mat, 'smc_diffuse')
            if not item.mat.smc_diffuse:
                return

            split = col.row().split(factor=0.1) if globs.is_blender_2_80_or_newer else col.row().split(
                percentage=0.1)
            split.separator()
            split.prop(item.mat, 'diffuse_color', text=bpy.app.translations.pgettext('Diffuse Color'))
            return

        shader = get_shader_type(item.mat)

        if shader in ['principled', 'xnalara'] and image:
            return

        if image:
            col.prop(item.mat, 'smc_diffuse')
            if not item.mat.smc_diffuse:
                return

        split = (
            col.row().split(factor=0.1) if globs.is_blender_2_80_or_newer and image else
            col.row().split(percentage=0.1) if image else col
        )
        split.separator()

        if shader in ['mmd', 'mmdCol']:
            split.prop(item.mat.node_tree.nodes['mmd_shader'].inputs['Diffuse Color'], 'default_value', text=bpy.app.translations.pgettext('Diffuse Color'))
        if shader in ['mtoon', 'mtoonCol']:
            split.prop(item.mat.node_tree.nodes['Mtoon1PbrMetallicRoughness.BaseColorFactor'], 'color', text=bpy.app.translations.pgettext('Base Color'))
        elif shader in ['vrm', 'vrmCol']:
            split.prop(item.mat.node_tree.nodes['RGB'].outputs[0], 'default_value', text=bpy.app.translations.pgettext('Base Color'))
        elif shader == 'xnalaraNewCol':
            split.prop(item.mat.node_tree.nodes['Group'].inputs['Diffuse'], 'default_value', text=bpy.app.translations.pgettext('Diffuse Color'))
        elif shader in ['principledCol', 'xnalaraCol']:
            split.prop(item.mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'], 'default_value', text=bpy.app.translations.pgettext('Base Color'))

    @staticmethod
    def _show_size_settings(col: bpy.types.UILayout, item: bpy.types.PropertyGroup):
        col.prop(item.mat, 'smc_size', text=bpy.app.translations.pgettext('Custom image size'))
        if item.mat.smc_size:
            split = col.row().split(factor=0.1) if globs.is_blender_2_80_or_newer else col.row().split(percentage=0.1)
            split.separator()
            col = split.column()
            col.prop(item.mat, 'smc_size_width', text=bpy.app.translations.pgettext('Max width (px)'))
            col.prop(item.mat, 'smc_size_height', text=bpy.app.translations.pgettext('Max height (px)'))
