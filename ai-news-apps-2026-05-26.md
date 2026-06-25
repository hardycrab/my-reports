# AI 新闻和应用方案分享

**生成时间**：2026-05-26 16:31
**信息来源**：阮一峰科技爱好者周刊（第 397 期）

---

## 🤖 AI 行业动态

### 1. 财富正在向 AI 集中

AI 相关的所有领域都在快速上涨：内存、存储、CPU、服务器、液冷、光通信、变压器等股价全部在涨。

- **三星和 SK 海力士**：两家韩国内存厂商把韩国股市从 2600 点拉到 7600 点。SK 海力士员工今年平均可拿到奖金**610 万人民币**。
- **OpenAI**：去年向 600 个员工回购了 66 亿美元股票，平均每人拿到近**1000 万美元**。
- **影响**：社会财富正在重新分配，快速向 AI 集中。即使不使用 AI 的人，也会面临成本上升、资金从本行业流向 AI 的影响。

**资源**：[阮一峰周刊第 397 期](https://www.ruanyifeng.com/blog/2026/05/weekly-issue-397.html)

### 2. 不要用 AI 估算医疗数据

一位英国医生做了实验，把 13 张食物照片提交给四个大模型（GPT-5.4、Claude Sonnet 4.6、Gemini 2.5 Pro、Gemini 3.1 Pro）估计碳水含量。

- **结果**：四个模型给出的回答不一样，同一张照片多次提交给同一个模型，回答也不一样。
- **波动最大**：Gemini 2.5 Pro 估计值从 55 克到 484 克，相差 429 克。
- **结论**：别用大模型估算食物的碳水含量，也不要让大模型做任何精确的医疗估算。

**资源**：[实验原文](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

### 3. 微软淘汰短信验证码

微软确认将放弃短信验证码，改用 Passkey、一次性时间码（TOTP）和验证过的邮件地址。

- **原因**：短信验证码有 SIM 卡欺骗和明文泄漏风险。
- **替代方案**：Passkey 密钥将成为 Windows 11 以后主要的验证方式，通过面部识别、指纹扫描器或 PIN 码唤起私钥验证。

---

## 🛠️ AI 应用方案分享

### 方案 1：AI Agent 终端交互增强

**工具**：[AVC (Agent View Controller)](https://github.com/study8677/Agent_View_Controller-AVC)

- **功能**：将 AI Agent 终端的确认文字变成可交互的网页弹窗，可以作为 Agent 的 Skill 使用。
- **适用场景**：需要用户确认的自动化任务、Agent 审批流程、交互式 AI 应用。
- **优势**：提升用户体验，让 Agent 输出更直观、可操作。

### 方案 2：本地 AI Agent 接入微信/Telegram

**工具**：[Lucarne](https://github.com/tuchg/Lucarne)

- **功能**：把本地运行的 AI Agent 接到微信/Telegram，让你离开电脑也能收到进展、审批权限、回复问题、接续会话。
- **适用场景**：远程监控 Agent 任务、移动端审批、随时与 Agent 交互。
- **优势**：打破设备限制，实现随时随地的 AI 协作。

---

## 📈 行业趋势（一句话）

AI 正引发前所未有的财富重新分配，推进速度快、力度大；同时 AI 在医疗等精确领域的局限性也提醒我们：AI 是强大的辅助工具，但不能替代专业判断，建议关注 AI Agent 和自动化工作流，同时保持对 AI 能力的理性认知。

---

## 🔗 推荐学习资源

1. **AI Agent 入门**：https://www.promptingguide.ai/zh/agents
2. **Passkey 介绍**：https://kerkour.com/passkeys
3. **GitHub AI 主题**：https://github.com/topics/artificial-intelligence
4. **阮一峰周刊**：https://www.ruanyifeng.com/blog/weekly/

---

*注：本报告基于阮一峰科技爱好者周刊（第 397 期）生成，实时新闻请访问上述资源链接。*
