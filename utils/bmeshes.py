from typing import Dict
from typing import Iterable
from typing import List
from typing import cast

import bmesh


def get_loops(bm: bmesh.types.BMesh) -> Dict[bmesh.types.BMFace, List[bmesh.types.BMLoop]]:
    """
    获取每个面的循环（loops）。

    参数:
        bm (bmesh.types.BMesh): 输入的 bmesh 对象。

    返回:
        Dict[bmesh.types.BMFace, List[bmesh.types.BMLoop]]: 一个字典，键是面，值是面的循环列表。
    """
    return {face: list(face.loops) for face in cast(Iterable, bm.faces)}