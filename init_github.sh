#!/bin/bash
# GitHub仓库初始化脚本
# 使用方法: bash init_github_repo.sh <你的GitHub用户名> <仓库名>

set -e

GITHUB_USER="${1:-}"
REPO_NAME="${2:-zdjk-monitor}"

if [ -z "$GITHUB_USER" ]; then
    echo "请提供GitHub用户名"
    echo "使用方式: bash init_github_repo.sh <你的GitHub用户名> [仓库名]"
    exit 1
fi

echo "=== 初始化GitHub仓库: $GITHUB_USER/$REPO_NAME ==="

# 创建GitHub仓库 (通过GitHub CLI)
if command -v gh &> /dev/null; then
    # 使用GitHub CLI
    echo "使用 GitHub CLI 创建仓库..."
    gh repo create "$REPO_NAME" --public --source=. --push --description "重点监控数据自动采集"
elif command -v git &> /dev/null; then
    # 手动创建
    echo "GitHub CLI 未安装，请手动创建仓库:"
    echo "1. 访问 https://github.com/new"
    echo "2. Repository name: $REPO_NAME"
    echo "3. 选择 Public"
    echo "4. 不要初始化README"
    echo "5. 运行以下命令:"
    echo ""
    echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo "   git push origin --set-upstream main"
else
    echo "错误: 未找到 git 命令"
    exit 1
fi

echo ""
echo "=== 创建本地git仓库 ==="
git init
git add -A
git commit -m "Initial commit: 重点监控数据采集"

echo ""
echo "=== 推送代码 ==="
if [ -n "$REPO_NAME" ]; then
    git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"
    git branch -M main
    git push -u origin main
fi

echo ""
echo "=== 完成 ==="
echo "仓库地址: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "Actions监控: https://github.com/$GITHUB_USER/$REPO_NAME/actions"