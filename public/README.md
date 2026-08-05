# 🚀 部署到 GitHub Pages - 快速指南

## ✅ 已完成

- [x] 76 份报告转换为 HTML
- [x] 生成索引页面
- [x] 初始化 Git 仓库
- [x] 创建推送脚本

## 📝 你需要做的 3 件事

### 1️⃣ 在 GitHub 创建仓库

访问：https://github.com/new

- Repository name: `my-reports`
- 描述：AI Agent Generated Reports
- Public（公开）
- ❌ **不要**勾选 "Initialize with README"
- 点击 **Create repository**

### 2️⃣ 推送代码到 GitHub

**方法 A：使用推送脚本（推荐）**

```bash
cd /home/admin/openclaw/workspace/public
bash /home/admin/openclaw/workspace/scripts/push-to-github.sh
```

**方法 B：手动推送**

```bash
cd /home/admin/openclaw/workspace/public
git remote add origin https://github.com/hardycrab/my-reports.git
git branch -M main
git push -u origin main
```

如果提示输入用户名密码：
- Username: `hardycrab`
- Password: 使用 **Personal Access Token**（不是 GitHub 密码）
  - 创建 Token：https://github.com/settings/tokens
  - 勾选 `repo` 权限
  - 复制生成的 token（只显示一次）

### 3️⃣ 启用 GitHub Pages

1. 访问你的仓库：https://github.com/hardycrab/my-reports
2. 点击 **Settings**（设置）
3. 左侧菜单点击 **Pages**
4. Build and deployment：
   - Source: Deploy from a branch
   - Branch: 选择 **main**
   - Folder: 选择 **/ (root)**
5. 点击 **Save**

## 🎉 完成！

等待 1-2 分钟部署，然后访问：

**📱 报告索引页**：
```
https://hardycrab.github.io/my-reports/reports/index.html
```

**示例报告**：
```
https://hardycrab.github.io/my-reports/reports/基金评估报告 -2026-06-23.html
```

## 🔄 后续更新

每次生成新报告后：

```bash
cd /home/admin/openclaw/workspace
node scripts/md2html.js
cd public
git add -A
git commit -m "Update reports"
git push
```

GitHub Pages 会在 1-2 分钟内自动更新！

## ❓ 遇到问题？

**检查仓库是否创建成功**：
```bash
curl https://github.com/hardycrab/my-reports
```

**检查 Git 状态**：
```bash
cd /home/admin/openclaw/workspace/public
git status
git remote -v
git log --oneline -5
```

**网络问题**：
如果 push 失败，可能是网络问题，可以：
1. 使用代理
2. 稍后再试
3. 使用 GitHub Desktop 图形界面

---

**需要帮助？把错误信息发给我！**
