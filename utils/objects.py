import math
from collections import defaultdict
from typing import List, Dict

import bpy
from mathutils import Vector


def get_polys(ob: bpy.types.Object) -> Dict[int, bpy.types.MeshPolygon]:
    """
    获取对象的多边形列表，按材质索引分组。

    参数:
        ob (bpy.types.Object): 输入的对象。

    返回:
        Dict[int, bpy.types.MeshPolygon]: 一个字典，键是材质索引，值是多边形列表。
    """
    polys = defaultdict(list)
    for poly in ob.data.polygons:
        polys[poly.material_index].append(poly)
    return polys


def get_uv(ob: bpy.types.Object, poly: bpy.types.MeshPolygon) -> List[Vector]:
    """
    获取多边形的 UV 坐标。

    参数:
        ob (bpy.types.Object): 输入的对象。
        poly (bpy.types.MeshPolygon): 输入的多边形。

    返回:
        List[Vector]: 多边形的 UV 坐标列表。
    """
    data = ob.data.uv_layers.active.data
    return [data[loop_idx].uv if loop_idx < len(data) else Vector((0, 0, 0)) for loop_idx in poly.loop_indices]


def align_uv(face_uv: List[Vector]) -> List[Vector]:
    """
    对齐 UV 坐标，使其最小值为 (0, 0)。

    参数:
        face_uv (List[Vector]): 输入的 UV 坐标列表。

    返回:
        List[Vector]: 对齐后的 UV 坐标列表。
    """
    min_x = float('inf')
    min_y = float('inf')

    for uv in face_uv:
        if not math.isnan(uv.x):
            min_x = min(min_x, uv.x)
        if not math.isnan(uv.y):
            min_y = min(min_y, uv.y)

    min_x = math.floor(min_x)
    min_y = math.floor(min_y)

    if min_x != 0 or min_y != 0:
        for uv in face_uv:
            uv.x -= min_x
            uv.y -= min_y
    return face_uv