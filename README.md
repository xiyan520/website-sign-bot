# 自动网站签到脚本

这是一个基于 GitHub Actions 的自动签到脚本，用于自动登录网站并完成每日签到任务，签到结果会通过 IYUU 推送到您的设备上。

---

## ✨ 功能特点

- ✅ 自动登录网站并完成签到操作  
- ✅ 定时执行（默认每天早上 8 点）  
- ✅ 签到结果通过 IYUU 通知推送  
- ✅ 获取详细的签到奖励信息  
- ✅ 失败时自动截图和错误报告  
- ✅ 完全基于 GitHub Actions，无需服务器  

---

## 🚀 快速开始

### 1. Fork 本仓库

点击本仓库右上角的 **Fork** 按钮，将仓库复制到您的 GitHub 账号下。

### 2. 设置 Secrets

在您 Fork 的仓库中，进行以下操作：

1. 点击 **Settings > Secrets and variables > Actions**
2. 点击 **New repository secret**
3. 添加以下两个 secret：

- `COOKIE`：您的网站 Cookie（从浏览器开发者工具中获取）
- `IYUU_TOKEN`：您的 IYUU 推送令牌

### 3. 启用 GitHub Actions

1. 在您的仓库中，点击 **Actions** 标签  
2. 如看到提示，点击 **I understand my workflows, go ahead and enable them**  
3. 在左侧找到 **Auto Sign In** 工作流，点击进入  
4. 点击 **Run workflow** 按钮进行手动测试  

设置完成后，脚本会根据设定的时间自动运行，您也可以随时手动触发。

---

## 📁 文件说明

| 文件名                          | 说明                            |
|-------------------------------|---------------------------------|
| `sign.py`                     | 主要的签到脚本                  |
| `.github/workflows/main.yml`  | GitHub Actions 工作流配置       |
| `requirements.txt`            | Python 依赖列表                  |

---

## ⚙️ 自定义配置

### 修改运行时间

编辑 `.github/workflows/main.yml` 文件中的 cron 表达式：

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # 默认为 UTC 时间 0 点，即北京时间早上 8 点
```

Cron 表达式格式为：`分 时 日 月 星期`

例如：

- `0 22 * * *`：每天 UTC 22 点（北京时间早上 6 点）
- `0 0 * * 1-5`：每周一至周五 UTC 0 点

---

## 🔄 更新 Cookie

1. 在浏览器中登录目标网站  
2. 打开开发者工具（F12 或右键 - 检查）  
3. 进入 **Network** 标签页，刷新页面  
4. 在请求中找到 Cookie 信息（通常在请求头中）  
5. 更新 GitHub 仓库中的 `COOKIE` secret  

---

## ❓ 常见问题

**Q: 如何知道脚本是否正常运行？**  
A: 您会收到 IYUU 推送的通知，也可以在 GitHub Actions 页面查看运行日志。

**Q: 为什么没有收到签到通知？**  
A: 请检查 IYUU 令牌是否正确，也可以在 Actions 运行日志中查看详细错误信息。

**Q: 脚本突然无法工作了怎么办？**  
A: 最常见的原因是 Cookie 过期，请更新 Cookie。其次，网站可能变更了页面结构，需要更新选择器。

**Q: 如何调试脚本问题？**  
A: 查看 GitHub Actions 运行日志，或者在本地运行脚本进行调试。

---

## ⚠️ 注意事项

- 本脚本仅用于学习和个人使用，请勿用于任何商业目的  
- 频繁自动签到可能违反某些网站的使用条款，请阅读目标网站的相关规定  
- Cookie 中包含敏感信息，请确保安全存储在 GitHub Secrets 中，不要直接硬编码在脚本中  
- 建议每隔一段时间检查并更新 Cookie，以保证脚本正常运行  

---

## 🔧 维护和更新

如需适配其他网站或添加新功能，您可以：

- 在 `sign.py` 中更新网站 URL 和元素选择器  
- 根据需要调整等待时间和错误处理逻辑  
- 自定义通知内容格式  

---

## 💻 技术实现

- **Python + Selenium** - 实现网页自动化操作  
- **GitHub Actions** - 提供定时执行环境  
- **IYUU 推送** - 实现运行结果通知  

---

如有任何问题或建议，欢迎提交 Issue 或 Pull Request！  
🛠️ Happy Hacking！
