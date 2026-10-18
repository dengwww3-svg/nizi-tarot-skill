# 尼子塔罗（nizi-tarot）

一个面向 Codex 的四季塔罗 Skill。它使用完整的韦特塔罗牌组，在春分、夏至、秋分和冬至进行季度牌阵抽取、正逆位解读、趋势分析与季度复盘。

## 功能

- 从完整韦特塔罗 78 张牌中抽取。
- 将牌组分为大阿卡纳、宝剑、权杖、圣杯和星币五组。
- 每组独立随机抽取一张，并随机确定正位或逆位。
- 按四季牌阵分析季度核心、思维、行动、情感与现实层面。
- 输出牌面联动、可执行建议和季度复盘问题。
- 遵循“同一季度只进行一次正式四季牌阵”的规则。

## 牌阵结构

| 位置 | 牌组／元素 | 主题 |
|---|---|---|
| 中央 | 大阿卡纳 | 本季度核心课题与整体趋势 |
| 右侧 | 宝剑／风 | 计划、决策、学习、沟通与思考 |
| 左侧 | 权杖／火 | 事业、目标、行动力、野心与欲望 |
| 下方 | 圣杯／水 | 感情、人际、情绪与感受 |
| 上方 | 星币／土 | 财务、健康、工作、安全感与现实积累 |

## 仓库结构

```text
nizi-tarot-skill/
├── README.md
├── .gitignore
└── skills/
    └── nizi-tarot/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── four-seasons-rules.md
        │   └── tarot-foundations.md
        └── scripts/
            └── draw_four_seasons.py
```

## 安装

### 让 Codex 从 GitHub 安装

将下面地址中的用户名和仓库名替换为实际值，然后把指令交给 Codex：

```text
请安装并验证这个 Skill：
https://github.com/<你的用户名>/<仓库名>/tree/main/skills/nizi-tarot
```

安装后请开启一个新的 Codex 任务，使 Skill 被重新发现。

### 手动安装

下载仓库后，把 `skills/nizi-tarot` 整个目录复制到个人 Codex 技能目录：

- Windows：`C:\Users\<用户名>\.codex\skills\nizi-tarot`
- macOS／Linux：`~/.codex/skills/nizi-tarot`

## 使用

在新的 Codex 任务中输入：

```text
使用 $nizi-tarot 为我进行本季度的四季塔罗抽牌与解读。
```

也可以自然地提出：

```text
帮我进行本季度的四季塔罗抽牌。
```

Codex 会先确认本季度的问题或背景。用户明确表示“开始抽牌”后，Skill 才会运行随机抽牌脚本并揭示结果。

## 环境要求

- 支持本地 Skills 的 Codex 环境。
- Python 3.8 或更高版本。
- 无第三方 Python 依赖。

## 验证

使用 Codex 内置 `skill-creator` 的验证脚本检查 Skill：

```powershell
python <skill-creator目录>/scripts/quick_validate.py ./skills/nizi-tarot
```

也可以单独测试随机抽牌脚本：

```powershell
python ./skills/nizi-tarot/scripts/draw_four_seasons.py
```

脚本应输出五张牌，牌组依次为大阿卡纳、宝剑、权杖、圣杯和星币，并包含每张牌的正逆位。

## 日历提醒

Skill 包含季度提醒规则，但不会自动取得使用者的日历权限。每位使用者需自行连接 Google Calendar、Outlook Calendar，或在 Codex 中创建自动化提醒。提醒应依据每年实际春分、夏至、秋分、冬至日期，在前一天及当天触发。

## 资料来源

- 基础塔罗知识参考：[Tarotap：ChatGPT 塔罗占卜指令 Prompt，免费在线 ChatGPT 算塔罗牌](https://tarotap.com/zh/blog/chatgpt-tarot-reading-guide)
- 四季牌阵规则依据创建者提供的两张规则资料图整理；原始图片未包含在仓库中。

## 免责声明

本项目用于娱乐、自我探索与创意反思，不提供确定预言，也不能替代医疗、心理、法律、财务或其他专业建议。重要决定请结合现实信息并咨询合格专业人士。

## 许可证

当前尚未指定开源许可证。公开发布前，请根据你允许他人使用、修改和再分发代码的范围添加合适的 `LICENSE` 文件。
