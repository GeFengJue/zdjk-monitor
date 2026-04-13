# 重点监控数据采集

自动采集A股重点监控数据，包括：
- ZDJK_Today: 重点监控今日
- ZDJK_His: 重点监控历史
- WXHJ_His: 风险揭示函历史

## 数据来源

同花顺问财接口

## 自动更新

通过GitHub Actions每小时自动更新数据

## 本地运行

```bash
pip install -r requirements.txt
python zdjk_fetcher.py
```

## 数据文件

采集的数据保存在 `data/zdjk_data.json`