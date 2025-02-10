#edit by deepseek r1

from typing import Dict
from typing import Union

import bpy

from . import addon_updater_ops
from . import extend_lists
from . import extend_types
from . import globs
from . import operators
from . import ui
from .icons import initialize_smc_icons
from .icons import unload_smc_icons
from .type_annotations import BlClasses

# 添加翻译字典
translations_dict = {
    "zh_CN": {
        # UI 面板
        ("*", "Material Combiner"): "材质合并工具",
        ("*", "Combine materials and pack textures"): "合并材质并打包纹理",
        ("*", "Credits"): "致谢",
        ("*", "Properties"): "属性",
        ("*", "Updates"): "更新",

        # 操作符
        ("Operator", "Combine Materials"): "合并材质",
        ("Operator", "Refresh Object Data"): "刷新对象数据",
        ("Operator", "Switch Combine Mode"): "切换合并模式",
        ("Operator", "Add Image"): "添加图像",
        ("Operator", "Move Image"): "移动图像",
        ("Operator", "Set Image Path"): "设置图像路径",
        ("Operator", "Reset Image"): "重置图像",
        ("Operator", "Remove Image"): "移除图像",
        ("Operator", "Open Browser"): "打开浏览器",
        ("Operator", "Install PIL"): "安装 PIL",

        # 其他
        ("*", "Error"): "错误",
        ("*", "Success"): "成功",
                # CombineList 属性
        ("*", "Current Object"): "当前对象",
        ("*", "Current Object Material"): "当前对象材质",
        ("*", "Material Layers"): "材质层",
        ("*", "Materials with the same number will be merged together.\nUse this to create multiple materials linked to the same atlas file"): 
            "相同编号的材质将被合并。\n使用此功能可以创建链接到同一图集文件的多个材质",
        ("*", "Used"): "已使用",
        ("*", "Type"): "类型",

        # UpdatePreferences 属性
        ("*", "Auto-check for Update"): "自动检查更新",
        ("*", "If enabled, auto-check for updates using an interval"): "如果启用，将按间隔自动检查更新",
        ("*", "Months"): "月",
        ("*", "Number of months between checking for updates"): "检查更新之间的月数",
        ("*", "Days"): "天",
        ("*", "Number of days between checking for updates"): "检查更新之间的天数",
        ("*", "Hours"): "小时",
        ("*", "Number of hours between checking for updates"): "检查更新之间的小时数",
        ("*", "Minutes"): "分钟",
        ("*", "Number of minutes between checking for updates"): "检查更新之间的分钟数",

        # Scene 属性
        ("*", "Atlas size"): "图集尺寸",
        ("*", "Power of 2"): "2 的幂",
        ("*", "Combined image size is power of 2"): "合并图像的尺寸是 2 的幂",
        ("*", "Quadratic"): "正方形",
        ("*", "Combined image has same width and height"): "合并图像的宽度和高度相同",
        ("*", "Automatic"): "自动",
        ("*", "Combined image has minimal size"): "合并图像的尺寸最小",
        ("*", "Custom"): "自定义",
        ("*", "Combined image has proportionally scaled to fit in custom size"): "合并图像按比例缩放以适应自定义尺寸",
        ("*", "Strict Custom"): "严格自定义",
        ("*", "Combined image has exact custom width and height"): "合并图像具有精确的自定义宽度和高度",
        ("*", "Max width (px)"): "最大宽度（像素）",
        ("*", "Select max width for combined image"): "选择合并图像的最大宽度",
        ("*", "Max height (px)"): "最大高度（像素）",
        ("*", "Select max height for combined image"): "选择合并图像的最大高度",
        ("*", "Crop outside images by UV"): "根据 UV 裁剪外部图像",
        ("*", "Crop images by UV if materials UV outside of bounds"): "如果材质的 UV 超出边界，则根据 UV 裁剪图像",
        ("*", "Pixel Art / Small Textures"): "像素艺术 / 小纹理",
        ("*", "Avoids 1-pixel UV scaling for small textures.\nDisable for larger textures to avoid blending with nearby pixels"): 
            "避免对小纹理进行 1 像素 UV 缩放。\n对于较大的纹理，请禁用以避免与附近像素混合",
        ("*", "Size of materials without image"): "无图像材质的大小",
        ("*", "Select the size of materials that only consist of a color"): "选择仅由颜色组成的材质的大小",
        ("*", "Size of gaps between images"): "图像之间的间隙大小",
        ("*", "Select size of gaps between images"): "选择图像之间的间隙大小",
        ("*", "Select the directory in which the generated texture atlas will be saved"): "选择生成的纹理图集的保存目录",

        # Material 属性
        ("*", "Material Root"): "材质根节点",
        ("*", "Multiply image with diffuse color"): "将图像与漫反射颜色相乘",
        ("*", "Multiply the materials image with its diffuse color.\nINFO: If this color is white the final image will be the same"): 
            "将材质的图像与其漫反射颜色相乘。\n提示：如果此颜色为白色，则最终图像将相同",
        ("*", "Custom image size"): "自定义图像大小",
        ("*", "Select the max size for this materials image in the texture atlas"): "选择此材质图像在图集中的最大尺寸",
        # UI 列表
        ("*", "Deselect All"): "取消全选",
        ("*", "Select All"): "全选",
        ("*", "PREFERENCES"): "偏好设置",
        ("*", "SCRIPT"): "脚本",
                # 面板标签
        ("*", "Credits"): "致谢",

        # 文本标签
        ("*", "Created by:"): "作者：",
        ("*", "If you have found a bug:"): "如果您发现了一个错误：",
        ("*", "If this saved you time:"): "如果这节省了您的时间：",

        # 按钮文本
        ("*", "Contact me on Discord (@shotariya)"): "通过 Discord 联系我 (@shotariya)",
        ("*", "Report a Bug on GitHub"): "在 GitHub 上报告错误",
        ("*", "Support Material Combiner"): "支持 Material Combiner",
        ("*", "Buy Me a Coffee"): "请我喝杯咖啡",
                # 面板标签
        ("*", "Main Menu"): "主菜单",

        # 文本标签
        ("*", "Materials to combine:"): "要合并的材质：",
        ("*", "Properties:"): "属性：",
        ("*", "Size of materials without image"): "无图像材质的大小",
        ("*", "Size of gaps between images"): "图像之间的间隙大小",

        # 按钮文本
        ("*", "Update Material List"): "更新材质列表",
        ("*", "Generate Material List"): "生成材质列表",
        ("*", "Save Atlas to.."): "保存图集到..",
        ("*", "Install Pillow"): "安装 Pillow",

        # 提示信息
        ("*", "Python Imaging Library required to continue"): "需要 Python Imaging Library 才能继续",
        ("*", "If the installation process is repeated\n"
              "try to run Blender as Administrator\n"
              "or check your Internet Connection."): 
              "如果安装过程重复，请尝试以管理员身份运行 Blender\n"
              "或检查您的网络连接。",
        ("*", "If the error persists, contact me on Discord for a manual installation:"): 
              "如果问题仍然存在，请联系我以进行手动安装：",
        # 操作符标签和描述
        ("*", "Settings for material:"): "材质设置：",
        ("*", "Show settings for this material"): "显示此材质的设置",

        # 文本标签
        ("*", "Image size: {0}x{0}px"): "图像大小：{0}x{0}像素",
        ("*", "Diffuse Color"): "漫反射颜色",
        ("*", "Base Color"): "基础颜色",

        # 属性名称
        ("*", "smc_size"): "自定义图像大小",
        ("*", "smc_size_width"): "最大宽度（像素）",
        ("*", "smc_size_height"): "最大高度（像素）",

        # 面板标签
        ("*", "Updates"): "更新",
        # browser.py
        ("*", "Open Browser"): "打开浏览器",
        ("*", "Click to open in browser"): "点击以在浏览器中打开",
        ("*", "Browser opened"): "浏览器已打开",

        # combine_list.py
        ("*", "Combine List"): "合并列表",
        ("*", "Updates the material list"): "更新材质列表",
        ("*", "Add Item"): "添加项目",
        ("*", "Selected materials will be combined into one texture atlas"): "选中的材质将被合并到一个纹理图集中",

        # include.py
        ("*", "Installation complete"): "安装完成",
        ("*", "Please restart Blender"): "请重启 Blender",
        ("*", "Update Material List"): "更新材质列表",
        ("*", "Generate Material List"): "生成材质列表",
        ("*", "Save Atlas to.."): "保存图集到..",
        ("*", "If this saved you time:"): "如果这节省了您的时间：",
        ("*", "Support Material Combiner"): "支持 Material Combiner",
        ("*", "Buy Me a Coffee"): "请我喝杯咖啡",
        # multicombine_list.py
        ("*", "Add Item"): "添加项目",
        ("*", "Remove Item"): "移除项目",
        ("*", "Move Item"): "移动项目",
        ("*", "Reset Item"): "重置项目",
        ("*", "Reset Selected Texture"): "重置选中的纹理",
        ("*", "Diffuse Item"): "漫反射项目",
        ("*", "Texture as Color"): "纹理作为颜色",
        ("*", "Path Item"): "路径项目",
        ("*", "Select an Image"): "选择图像",

        # combiner.py
        ("*", "Create Atlas"): "创建图集",
        ("*", "Combine materials"): "合并材质",
        ("*", "Materials were combined"): "材质已合并",
        ("*", "Duplicates were combined"): "重复项已合并",
        ("*", "No unique materials selected"): "未选择唯一材质",
    },
}

__bl_classes = [
    ui.credits_menu.CreditsMenu,
    ui.main_menu.MaterialMenu,
    ui.property_menu.PropertyMenu,
    ui.update_menu.UpdateMenu,

    operators.combiner.Combiner,
    operators.combine_list.RefreshObData,
    operators.combine_list.CombineSwitch,
    operators.multicombine_list.MultiCombineColor,
    operators.multicombine_list.MultiCombineImageAdd,
    operators.multicombine_list.MultiCombineImageMove,
    operators.multicombine_list.MultiCombineImagePath,
    operators.multicombine_list.MultiCombineImageReset,
    operators.multicombine_list.MultiCombineImageRemove,
    operators.browser.OpenBrowser,
    operators.get_pillow.InstallPIL,

    extend_types.CombineList,
    extend_types.UpdatePreferences,

    extend_lists.SMC_UL_Combine_List,
]


def register_all(bl_info: Dict[str, Union[str, tuple]]) -> None:
    # 注册翻译
    bpy.app.translations.register(__name__, translations_dict)

    _register_classes()
    initialize_smc_icons()
    addon_updater_ops.register(bl_info)
    addon_updater_ops.check_for_update_background()
    extend_types.register()


def unregister_all() -> None:
    _unregister_classes()
    unload_smc_icons()
    addon_updater_ops.unregister()
    extend_types.unregister()

    # 注销翻译
    bpy.app.translations.unregister(__name__)

def _register_classes() -> None:
    count = 0
    for cls in __bl_classes:
        make_annotations(cls)
        try:
            bpy.utils.register_class(cls)
            count += 1
        except ValueError as e:
            print('Error:', cls, e)
    print('Registered', count, 'Material Combiner classes.')
    if count < len(__bl_classes):
        print('Skipped', len(__bl_classes) - count, 'Material Combiner classes.')


def _unregister_classes() -> None:
    count = 0
    for cls in reversed(__bl_classes):
        try:
            bpy.utils.unregister_class(cls)
            count += 1
        except (ValueError, RuntimeError) as e:
            print('Error:', cls, e)
    print('Unregistered', count, 'Material Combiner classes.')


def make_annotations(cls: BlClasses) -> BlClasses:
    if globs.is_blender_2_79_or_older:
        return cls

    if bpy.app.version >= (2, 93, 0):
        bl_props = {k: v for k, v in cls.__dict__.items() if isinstance(v, bpy.props._PropertyDeferred)}
    else:
        bl_props = {k: v for k, v in cls.__dict__.items() if isinstance(v, tuple)}

    if bl_props:
        if '__annotations__' not in cls.__dict__:
            setattr(cls, '__annotations__', {})

        annotations = cls.__dict__['__annotations__']

        for k, v in bl_props.items():
            annotations[k] = v
            delattr(cls, k)

    return cls