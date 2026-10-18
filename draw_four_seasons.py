#!/usr/bin/env python3
"""Draw one card from each Four Seasons Tarot pool with upright/reversed orientation."""

import json
import secrets


MAJOR = [
    "0 愚者", "I 魔术师", "II 女祭司", "III 皇后", "IV 皇帝", "V 教皇",
    "VI 恋人", "VII 战车", "VIII 力量", "IX 隐士", "X 命运之轮", "XI 正义",
    "XII 吊人", "XIII 死神", "XIV 节制", "XV 恶魔", "XVI 高塔",
    "XVII 星星", "XVIII 月亮", "XIX 太阳", "XX 审判", "XXI 世界",
]
RANKS = ["A", "二", "三", "四", "五", "六", "七", "八", "九", "十", "侍从", "骑士", "王后", "国王"]


def suit(name):
    return [f"{name}{rank}" for rank in RANKS]


POOLS = [
    ("整体运势／季度核心", "大阿卡纳", MAJOR),
    ("风／计划·决策·学习·沟通", "宝剑", suit("宝剑")),
    ("火／事业·目标·行动·欲望", "权杖", suit("权杖")),
    ("水／感情·人际·情绪·感受", "圣杯", suit("圣杯")),
    ("土／财务·健康·工作·安全感", "星币", suit("星币")),
]


def main():
    rng = secrets.SystemRandom()
    cards = []
    for position, pool, deck in POOLS:
        cards.append({
            "position": position,
            "pool": pool,
            "card": rng.choice(deck),
            "orientation": rng.choice(["正位", "逆位"]),
        })
    print(json.dumps({"spread": "四季牌阵", "cards": cards}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
