#!/usr/bin/env python3
"""GitHub 测试项目 - Claude Code 调用测试"""
from datetime import datetime

def main():
    print("=" * 40)
    print("Hello, World from GitHub Test!")
    print("=" * 40)
    now = datetime.now()
    print(f"创建日期：{now.strftime('%Y-%m-%d')}")
    print(f"创建时间：{now.strftime('%H:%M:%S')}")
    print(f"星期：{now.strftime('%A')}")
    print("=" * 40)

if __name__ == "__main__":
    main()
