from __future__ import annotations
from typing import Any

# 辞書が要素のリストに対して処理をする


class DictUtil:
    # 特定のキーの値が最も大きい要素(辞書)を返します
    def highest(dlist: list[dict], key: str, default: Any = None) -> dict:
        return max(
            dlist,
            key=lambda d: d.get(key, default),
        )
