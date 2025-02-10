from typing import Dict

import bpy


def get_texture(mat: bpy.types.Material) -> bpy.types.Texture:
    """
    获取材质的第一个有效纹理。

    参数:
        mat (bpy.types.Material): 输入的材质对象。

    返回:
        bpy.types.Texture: 材质的第一个有效纹理，如果材质无效则返回 None。
    """
    return next((slot.texture for idx, slot in enumerate(mat.texture_slots) if
                 slot is not None and mat.use_textures[idx]), None)


def get_textures(mat: bpy.types.Material) -> Dict[int, bpy.types.Texture]:
    """
    获取材质的所有有效纹理。

    参数:
        mat (bpy.types.Material): 输入的材质对象。

    返回:
        Dict[int, bpy.types.Texture]: 一个字典，键是纹理索引，值是纹理对象。
    """
    return {idx: slot.texture for idx, slot in enumerate(mat.texture_slots) if
            slot is not None and mat.use_textures[idx]}