#!/usr/bin/env python3
"""
免费节点订阅自动更新脚本

说明：
- 本脚本作为模板，默认只更新 update.log 时间戳
- 你可以在 SOURCES 中添加公开免费订阅源，脚本会尝试拉取并写入 subscriptions/
- 请自行确保数据源合法、稳定，并遵守对方服务条款
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUB_DIR = ROOT / "subscriptions"
LOG_FILE = ROOT / "update.log"

# 在这里添加你信任的公开免费订阅源（示例为空，避免写入失效链接）
# 格式: ("文件名", "订阅URL")
SOURCES: list[tuple[str, str]] = [
    # ("clash.txt", "https://example.com/clash-free"),
    # ("v2ray.txt", "https://example.com/v2ray-free"),
    # ("mixed.txt", "https://example.com/mixed-free"),
]


def update_log() -> None:
    today = dt.datetime.utcnow().strftime("%Y-%m-%d")
    entry = f"\n## {today}\n- 自动更新检查完成\n"
    if LOG_FILE.exists():
        content = LOG_FILE.read_text(encoding="utf-8")
        if today in content:
            return
        LOG_FILE.write_text(content.rstrip() + entry, encoding="utf-8")
    else:
        LOG_FILE.write_text("# 更新日志\n" + entry, encoding="utf-8")


def fetch_and_save(filename: str, url: str) -> bool:
    """尝试拉取订阅内容并保存。成功返回 True。"""
    try:
        import urllib.request

        req = urllib.request.Request(
            url,
            headers={"User-Agent": "free-proxy-nodes-updater/1.0"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        if not data or len(data) < 20:
            print(f"[skip] {filename}: empty or too short")
            return False
        path = SUB_DIR / filename
        path.write_bytes(data)
        print(f"[ok] updated {filename}")
        return True
    except Exception as e:
        print(f"[fail] {filename}: {e}")
        return False


def main() -> None:
    SUB_DIR.mkdir(parents=True, exist_ok=True)

    if not SOURCES:
        print("No sources configured. Only updating log timestamp.")
        print("Edit scripts/update_subscriptions.py and add URLs to SOURCES.")
    else:
        for filename, url in SOURCES:
            fetch_and_save(filename, url)

    update_log()
    print("Done.")


if __name__ == "__main__":
    main()
