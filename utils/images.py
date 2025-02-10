import os
from typing import Union

import bpy


def get_image(tex: bpy.types.Texture) -> bpy.types.Image:
    """
    获取纹理对应的图像。

    参数:
        tex (bpy.types.Texture): 输入的纹理对象。

    返回:
        bpy.types.Image: 纹理对应的图像对象，如果纹理无效则返回 None。
    """
    return tex.image if tex and hasattr(tex, 'image') and tex.image else None


def get_packed_file(image: Union[bpy.types.Image, None]) -> Union[bpy.types.PackedFile, None]:
    """
    获取图像的打包文件。

    参数:
        image (Union[bpy.types.Image, None]): 输入的图像对象。

    返回:
        Union[bpy.types.PackedFile, None]: 图像的打包文件，如果图像无效或未打包则返回 None。
    """
    if image and not image.packed_file and _get_image_path(image):
        image.pack()
    return image.packed_file if image and image.packed_file else None


def _get_image_path(img: Union[bpy.types.Image, None]) -> Union[str, None]:
    """
    获取图像的绝对路径。

    参数:
        img (Union[bpy.types.Image, None]): 输入的图像对象。

    返回:
        Union[str, None]: 图像的绝对路径，如果路径无效则返回 None。
    """
    if not img:
        return None

    # 获取图像的相对路径并转换为绝对路径
    relative_path = img.filepath
    if not relative_path:
        return None

    # 使用 bpy.path.abspath 处理 Blender 路径
    abs_path = bpy.path.abspath(relative_path)
    if not abs_path:
        return None

    # 使用 os.path.abspath 确保路径格式正确
    abs_path = os.path.abspath(abs_path)

    # 检查路径是否为文件，并排除特定格式
    if os.path.isfile(abs_path) and not abs_path.lower().endswith(('.spa', '.sph')):
        return abs_path

    return None