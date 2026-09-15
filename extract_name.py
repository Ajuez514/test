#!/usr/bin/env python3
"""从 stdin 读 JSON，输出 name 字段。"""
import json
import sys


def main():
    data = json.load(sys.stdin)
    print(data["name"])


if __name__ == "__main__":
    main()
