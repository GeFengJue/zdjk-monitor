#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重点监控API数据获取脚本
获取: ZDJK_Today, ZDJK_His, WXHJ_His
"""

import requests
import json
import os
from datetime import datetime

# 项目根目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")

def get_device_id():
    """获取设备ID"""
    return "A7POKCVREKRh6OhXQj0w8e"

def get_user_id():
    """获取用户ID"""
    return "55818188"

def fetch_zdjk_today():
    """获取重点监控今日"""
    url = "http://apphq.longhuvip.com/w内在逻辑/DTP_ZDJK_Today"
    params = {
        "device_id": get_device_id(),
        "user_id": get_user_id()
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching ZDJK_Today: {e}")
        return None

def fetch_zdjk_his():
    """获取重点监控历史"""
    url = "http://apphq.longhuvip.com/w内在逻辑/DTP_ZDJK_His"
    params = {
        "device_id": get_device_id(),
        "user_id": get_user_id(),
        "days": 30
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching ZDJK_His: {e}")
        return None

def fetch_wxhjj_his():
    """获取风险揭示函历史"""
    url = "http://apphq.longhuvip.com/w内在逻辑/DTP_WXHJ_His"
    params = {
        "device_id": get_device_id(),
        "user_id": get_user_id(),
        "days": 30
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching WXHJ_His: {e}")
        return None

def main():
    """主函数"""
    print(f"=== 重点监控数据获取 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

    # 确保数据目录存在
    os.makedirs(DATA_DIR, exist_ok=True)

    result = {
        "fetch_time": datetime.now().isoformat(),
        "ZDJK_Today": None,
        "ZDJK_His": None,
        "WXHJ_His": None
    }

    # 获取数据
    print("📡 获取 ZDJK_Today...")
    zdjk_today = fetch_zdjk_today()
    if zdjk_today:
        result["ZDJK_Today"] = zdjk_today
        print(f"   ✅ 获取成功")
    else:
        print(f"   ❌ 获取失败")

    print("\n📡 获取 ZDJK_His...")
    zdjk_his = fetch_zdjk_his()
    if zdjk_his:
        result["ZDJK_His"] = zdjk_his
        print(f"   ✅ 获取成功")
    else:
        print(f"   ❌ 获取失败")

    print("\n📡 获取 WXHJ_His...")
    wxhj_his = fetch_wxhjj_his()
    if wxhj_his:
        result["WXHJ_His"] = wxhj_his
        print(f"   ✅ 获取成功")
    else:
        print(f"   ❌ 获取失败")

    # 保存数据
    output_file = os.path.join(DATA_DIR, "zdjk_data.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n💾 数据已保存到 {output_file}")

    # 打印统计
    if result["ZDJK_Today"] and "List" in result["ZDJK_Today"]:
        print(f"\n📊 ZDJK_Today: {len(result['ZDJK_Today'].get('List', []))} 条记录")
    if result["ZDJK_His"] and "List" in result["ZDJK_His"]:
        print(f"📊 ZDJK_His: {len(result['ZDJK_His'].get('List', []))} 条记录")
    if result["WXHJ_His"] and "List" in result["WXHJ_His"]:
        print(f"📊 WXHJ_His: {len(result['WXHJ_His'].get('List', []))} 条记录")

    print("\n=== 完成 ===")

if __name__ == "__main__":
    main()