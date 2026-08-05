# 🚀 GitHub Pages 部署指南

## 第一步：创建 GitHub 仓库

1. **访问 GitHub**：https://github.com
2. **点击右上角 "+" → "New repository"**
3. **填写信息**：
   - Repository name: `my-reports`（或你喜欢的名字）
   - 描述：AI Agent Generated Reports
   - 公开/私有：建议公开（免费）
   - ❌ 不要勾选 "Initialize this repository with a README"
4. **点击 "Create repository"**

## 第二步：推送代码到 GitHub

复制以下命令，**替换 YOUR_USERNAME 为你的 GitHub 用户名**：

```bash
# 进入目录
cd /home/admin/openclaw/workspace/public

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin git@github.com:YOUR_USERNAME/my-reports.git

# 重命名分支为 main
git branch -M main

# 推送到 GitHub
git push -u origin main
```

**如果遇到 SSH 错误**，使用 HTTPS 方式：
```bash
git remote add origin https://github.com/YOUR_USERNAME/my-reports.git
git push -u origin main
```

## 第三步：启用 GitHub Pages

1. **进入刚创建的仓库页面**
2. **点击 "Settings"（设置）**
3. **左侧菜单找到 "Pages"**
4. **Build and deployment 部分**：
   - Source: Deploy from a branch
   - Branch: 选择 `main`
   - Folder: 选择 `/ (root)`
   - 点击 "Save"

## 第四步：等待部署完成

- GitHub 会自动构建（约 1-2 分钟）
- 刷新 Pages 页面，看到绿色对勾表示部署成功
- 你的网站地址类似：
  ```
  https://YOUR_USERNAME.github.io/my-reports/
  ```

## 第五步：访问报告

**索引页面**（报告列表）：
```
https://YOUR_USERNAME.github.io/my-reports/reports/index.html
```

**单个报告示例**：
```
https://YOUR_USERNAME.github.io/my-reports/reports/基金评估报告 -2026-06-23.html
```

## 📱 在微信中查看

1. 复制索引页面链接
2. 发送到微信（文件传输助手或自己）
3. 直接在微信中点击打开
4. 可以分享给任何人查看

## 🔄 后续更新报告

每次生成新报告后，运行：

```bash
cd /home/admin/openclaw/workspace
node scripts/md2html.js
cd public
git add -A
git commit -m "Update reports"
git push
```

GitHub Pages 会在 1-2 分钟内自动更新！

## ⚙️ 自定义域名（可选）

如果想用自己的域名：

1. 在 Pages 设置中添加自定义域名
2. 在你的 DNS 服务商添加 CNAME 记录
3. 等待 DNS 生效（约 10 分钟）

---

**需要帮助？**

运行以下命令检查状态：
```bash
cd /home/admin/openclaw/workspace/public
git status
git remote -v
```

把输出发给我，我帮你检查！
