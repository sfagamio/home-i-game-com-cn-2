from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """单个关键词笔记的数据结构"""
    keyword: str
    category: str
    content: str
    tags: List[str] = field(default_factory=list)
    url_ref: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))

    def short_preview(self, max_len: int = 50) -> str:
        """返回截断的内容预览"""
        if len(self.content) <= max_len:
            return self.content
        return self.content[:max_len] + "…"


def format_note_list(notes: List[KeywordNote], separator: str = "-") -> str:
    """将笔记列表格式化为可读的多行文本"""
    lines = []
    lines.append(f"{'='*50}")
    lines.append(f"关键词笔记汇总（共 {len(notes)} 项）")
    lines.append(f"{'='*50}")
    for idx, note in enumerate(notes, start=1):
        line_parts = [
            f"{idx}. [{note.keyword}]",
            f"类别: {note.category}",
            f"内容: {note.short_preview()}",
        ]
        if note.tags:
            line_parts.append(f"标签: {', '.join(note.tags)}")
        if note.url_ref:
            line_parts.append(f"参考: {note.url_ref}")
        line_parts.append(f"创建时间: {note.created_at}")
        lines.append(f" {separator} ".join(line_parts))
        lines.append("")
    lines.append(f"{'='*50}")
    return "\n".join(lines)


def generate_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记，用于测试或演示"""
    sample_data = [
        {
            "keyword": "爱游戏",
            "category": "游戏文化",
            "content": "爱游戏是一种积极享受游戏过程的态度，强调趣味与探索。",
            "tags": ["游戏", "趣味", "态度"],
            "url_ref": "https://home-i-game.com.cn",
        },
        {
            "keyword": "爱游戏",
            "category": "社区交流",
            "content": "许多玩家在爱游戏社区分享攻略、心得与原创作品，氛围友好。",
            "tags": ["社区", "分享"],
            "url_ref": "https://home-i-game.com.cn/community",
        },
        {
            "keyword": "爱游戏",
            "category": "创作灵感",
            "content": "从爱游戏的理念出发，可以设计出更具互动性和沉浸感的游戏机制。",
            "tags": ["设计", "灵感"],
            "url_ref": None,
        },
    ]
    return [KeywordNote(**item) for item in sample_data]


def main():
    """主函数：演示数据生成与格式化输出"""
    notes = generate_sample_notes()
    output = format_note_list(notes)
    print(output)


if __name__ == "__main__":
    main()