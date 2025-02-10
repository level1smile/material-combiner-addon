import bpy
from bpy.app.translations import pgettext_iface as _

from ... import globs
from ...icons import get_icon_id
from ...type_annotations import Scene
from ...ui.main_menu import MaterialMenu


def draw_ui(context: bpy.types.Context, m_col: bpy.types.UILayout) -> None:
    if globs.pil_exist:
        _materials_list(context.scene, m_col)
    elif globs.smc_pi:
        col = m_col.box().column()
        col.label(text=_('Installation complete'), icon_value=get_icon_id('done'))
        col.label(text=_('Please restart Blender'), icon_value=get_icon_id('null'))
    else:
        MaterialMenu.pillow_installator(m_col)


def _materials_list(scn: Scene, m_col: bpy.types.UILayout) -> None:
    patreon = 'https://www.patreon.com/shotariya'
    buymeacoffee = 'https://buymeacoffee.com/shotariya'

    if scn.smc_ob_data:
        m_col.template_list('SMC_UL_Combine_List', 'combine_list', scn, 'smc_ob_data',
                            scn, 'smc_ob_data_id', rows=12, type='DEFAULT')
    col = m_col.column(align=True)
    col.scale_y = 1.2
    col.operator('smc.refresh_ob_data',
                 text=_('Update Material List') if scn.smc_ob_data else _('Generate Material List'),
                 icon_value=get_icon_id('null'))
    col = m_col.column()
    col.scale_y = 1.5
    col.operator('smc.combiner', text=_('Save Atlas to..'), icon_value=get_icon_id('null')).cats = True
    col.separator()
    col = m_col.column()
    col.label(text=_('If this saved you time:'))
    col.operator('smc.browser', text=_('Support Material Combiner'), icon_value=get_icon_id('patreon')).link = patreon
    col.operator('smc.browser', text=_('Buy Me a Coffee'), icon_value=get_icon_id('bmc')).link = buymeacoffee