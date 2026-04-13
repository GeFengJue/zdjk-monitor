#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新README中的数据表格
"""

import os
import re

def update_readme(data_file, readme_file):
    """更新README中的数据表格"""
    import json

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 生成ZDJK_Today表格
    zdjk_today_rows = []
    for item in data.get('ZDJK_Today', {}).get('List', []):
        if len(item) >= 5:
            code, name, start, end, status = item[:5]
            zdjk_today_rows.append(f"| {code} | {name} | {start} | {end} | {status} |")

    zdjk_today_table = "\n".join(zdjk_today_rows) if zdjk_today_rows else "| - | - | - | - | - |"

    # 生成WXHJ_His表格
    wxhj_rows = []
    for item in data.get('WXHJ_His', {}).get('List', [])[:10]:
        if len(item) >= 4:
            code, name, date, pdf_url = item[:4]
            wxhj_rows.append(f"| {code} | {name} | {date} | [查看PDF]({pdf_url}) |")

    wxhj_table = "\n".join(wxhj_rows) if wxhj_rows else "| - | - | - | - |"

    # 读取README
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme = f.read()

    # 替换ZDJK_Today表格
    pattern1 = r'### ZDJK_Today \(重点监控今日\)\s*\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\n(\|.*?\n)*'
    readme = re.sub(pattern1, f'### ZDJK_Today (重点监控今日)\n| 股票代码 | 名称 | 开始日期 | 结束日期 | 状态 |\n|---------|------|---------|---------|------|\n{zdjk_today_table}\n', readme, flags=re.DOTALL)

    # 替换WXHJ_His表格
    pattern2 = r'### WXHJ_His \(风险揭示函\)\s*\|.*?\|.*?\|.*?\|.*?\|\n(\|.*?\n)*'
    readme = re.sub(pattern2, f'### WXHJ_His (风险揭示函)\n| 股票代码 | 名称 | 日期 | PDF链接 |\n|---------|------|------|---------|\n{wxhj_table}\n', readme, flags=re.DOTALL)

    # 更新时间戳
    import datetime
    fetch_time = data.get('fetch_time', '')
    readme = re.sub(r'更新于:.*', f'更新于: {fetch_time}', readme)

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f"✅ README已更新")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, "data", "zdjk_data.json")
    readme_file = os.path.join(script_dir, "README.md")
    update_readme(data_file, readme_file)