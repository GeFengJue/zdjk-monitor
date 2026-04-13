# 重点监控数据采集

自动采集A股重点监控数据，每小时更新。

## 数据来源

同花顺问财接口

## 自动更新

通过GitHub Actions每小时自动更新数据

## 当前数据

[![Actions Status](https://github.com/GeFengJue/zdjk-monitor/workflows/Fetch%20ZDJK%20Data/badge.svg)](https://github.com/GeFengJue/zdjk-monitor/actions)

### ZDJK_Today (重点监控今日)
| 股票代码 | 名称 | 开始日期 | 结束日期 | 状态 |
|---------|------|---------|---------|------|
| 000890 | 法尔胜 | 2026-04-08 | 2026-04-21 | 2 |
| 600488 | 津药药业 | 2026-04-08 | 2026-04-21 | 2 |
| 300834 | 星辉环材 | 2026-04-07 | 2026-04-20 | 2 |
| 605255 | 天普股份 | 2026-03-31 | 2026-04-14 | 2 |
| 001896 | 豫能控股 | 2026-03-30 | 2026-04-13 | 2 |

### WXHJ_His (风险揭示函)
| 股票代码 | 名称 | 日期 | PDF链接 |
|---------|------|------|---------|
| 603023 | 威帝股份 | 2026-04-13 | [查看PDF](https://appdata.longhuvip.com/SupPDFs/2026-04/603023_10815082_28_10012.pdf) |
| 600635 | 大众公用 | 2026-03-30 | [查看PDF](https://appdata.longhuvip.com/SupPDFs/2026-03/600635_10813524_28_10743.pdf) |
| 603168 | 莎普爱思 | 2026-03-17 | [查看PDF](https://appdata.longhuvip.com/SupPDFs/2026-03/603168_10812097_28_10743.pdf) |

## 本地运行

```bash
pip install -r requirements.txt
python zdjk_fetcher.py
```

## API访问

Raw JSON: https://raw.githubusercontent.com/GeFengJue/zdjk-monitor/main/data/zdjk_data.json