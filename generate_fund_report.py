#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基金评估报告生成器
生成 HTML 报告和微信文字版报告
"""

import json
from datetime import datetime
from pathlib import Path

# 持仓数据
HOLDINGS = {
    "account_summary": {
        "total_amount": 107143.00,
        "yesterday_profit": -531.41,
        "holding_profit": -18747.22,
        "accumulated_profit": 10826.56
    },
    "funds": [
        {"code": "000217", "name": "华安黄金 ETF 联接 C", "amount": 18369.83, "yesterday_profit": -475.54, "holding_profit": -530.68, "rate": -3.00, "accumulated_profit": -21.24, "tag": "黄金"},
        {"code": "519732", "name": "交银定期支付双息平衡混合", "amount": 5360.01, "yesterday_profit": -62.02, "holding_profit": 2213.52, "rate": 70.35, "accumulated_profit": None, "tag": "定投"},
        {"code": "515880", "name": "华夏中证 5G 通信主题 ETF 联接 A", "amount": 4516.17, "yesterday_profit": -87.79, "holding_profit": 1016.18, "rate": 29.03, "accumulated_profit": None, "tag": "金选指数"},
        {"code": "270023", "name": "广发全球精选股票 (QDII)A", "amount": 11682.12, "yesterday_profit": -25.94, "holding_profit": 3182.12, "rate": 37.42, "accumulated_profit": None, "tag": ""},
        {"code": "008889", "name": "华夏国证半导体芯片 ETF 联接 C", "amount": 6993.52, "yesterday_profit": 1033.00, "holding_profit": -1633.00, "rate": -19.00, "accumulated_profit": None, "tag": "定投"},
        {"code": "110020", "name": "易方达沪深 300ETF 联接 A", "amount": 5591.64, "yesterday_profit": 1008.68, "holding_profit": 2020.01, "rate": 56.82, "accumulated_profit": None, "tag": ""},
        {"code": "000614", "name": "大成纳斯达克 100ETF 联接 A", "amount": 1955.82, "yesterday_profit": -24.25, "holding_profit": 95.82, "rate": 5.14, "accumulated_profit": None, "tag": ""},
        {"code": "512900", "name": "南方中证全指证券公司 ETF 联接 A", "amount": 10556.92, "yesterday_profit": -268.33, "holding_profit": -2480.00, "rate": -19.06, "accumulated_profit": None, "tag": ""},
        {"code": "002190", "name": "农银新能源混合 A", "amount": 10753.86, "yesterday_profit": -996.14, "holding_profit": -996.14, "rate": -8.48, "accumulated_profit": None, "tag": ""},
        {"code": "519069", "name": "汇添富价值精选混合 A", "amount": 14524.67, "yesterday_profit": -220.63, "holding_profit": -1926.49, "rate": -11.73, "accumulated_profit": None, "tag": ""},
        {"code": "100056", "name": "富国消费主题混合 A", "amount": 5625.72, "yesterday_profit": -1742.75, "holding_profit": -1742.75, "rate": -23.66, "accumulated_profit": None, "tag": ""},
        {"code": "019266", "name": "天弘中证光伏产业指数 A", "amount": 5691.08, "yesterday_profit": -77.07, "holding_profit": -2558.92, "rate": -31.02, "accumulated_profit": None, "tag": ""},
        {"code": "164724", "name": "汇添富中证互联网医疗主题", "amount": 4174.45, "yesterday_profit": -2045.02, "holding_profit": -2045.02, "rate": -32.88, "accumulated_profit": None, "tag": ""},
        {"code": "003096", "name": "中欧医疗健康混合 C", "amount": 6747.86, "yesterday_profit": 135.78, "holding_profit": -5152.14, "rate": -43.27, "accumulated_profit": None, "tag": "定投"},
        {"code": "260108", "name": "景顺长城新兴成长混合 A", "amount": 7602.33, "yesterday_profit": 73.25, "holding_profit": -6987.12, "rate": -47.93, "accumulated_profit": None, "tag": "定投"},
        {"code": "161725", "name": "招商中证白酒指数 (LOF)A", "amount": 3935.43, "yesterday_profit": 37.16, "holding_profit": -3581.33, "rate": -47.63, "accumulated_profit": None, "tag": "定投"},
        {"code": "015280", "name": "招商中证白酒指数 C", "amount": 2331.40, "yesterday_profit": 25.77, "holding_profit": -2639.06, "rate": -53.16, "accumulated_profit": None, "tag": ""},
    ]
}

# 今日基金估值数据（从查询结果获取）
TODAY_ESTIMATES = {
    "000217": {"estimate": 3.1687, "change": -0.07, "nav": 3.1710, "nav_date": "2026-06-16"},
    "519732": {"estimate": 10.0688, "change": 1.87, "nav": 9.8840, "nav_date": "2026-06-16"},
    "515880": {"estimate": 1.7298, "change": -0.03, "nav": 1.7303, "nav_date": "2026-06-16"},
    "270023": {"estimate": 7.0934, "change": 0.36, "nav": 7.0679, "nav_date": "2026-06-15"},
    "008889": {"estimate": 2.8444, "change": 1.31, "nav": 2.8076, "nav_date": "2026-06-16"},
    "110020": {"estimate": 1.9781, "change": 0.34, "nav": 1.9714, "nav_date": "2026-06-16"},
    "512900": {"estimate": 1.0638, "change": -0.60, "nav": 1.0702, "nav_date": "2026-06-16"},
    "002190": {"estimate": 3.0870, "change": -1.13, "nav": 3.1224, "nav_date": "2026-06-16"},
    "519069": {"estimate": 3.5062, "change": 0.26, "nav": 3.4970, "nav_date": "2026-06-16"},
    "100056": {"estimate": 2.7715, "change": 0.56, "nav": 2.7560, "nav_date": "2026-06-16"},
    "003096": {"estimate": 1.4572, "change": -0.41, "nav": 1.4631, "nav_date": "2026-06-16"},
    "260108": {"estimate": 1.4291, "change": -0.62, "nav": 1.4380, "nav_date": "2026-06-16"},
    "161725": {"estimate": 0.5331, "change": -1.02, "nav": 0.5386, "nav_date": "2026-06-16"},
}

# 财经新闻摘要
NEWS_SUMMARY = """
【今日财经要闻】(2026 年 6 月 17 日)

1. 美伊阶段性协议落定，风险溢价回落
   - 美伊签署谅解备忘录，中东局势缓和
   - 地缘风险溢价开始回落，A 股交易转向成长修复
   - 有色板块兼具胜率和赔率，贵金属、油价受损链值得关注

2. 美联储 6 月利率决议前夕
   - 美联储主席沃什将于 6 月 17 日主持 FOMC 新闻发布会
   - 利率决议将于 6 月 18 日凌晨公布
   - 市场对降息预期升温，黄金作为避险资产需关注决议后走势

3. 科技板块动态
   - 台积电发布玻璃基板开发计划，消费电子 ETF 大涨超 3%
   - 科创板改革方向明确，前沿新兴领域迎来上市机遇
   - 半导体指数隔夜跌近 6%，短期波动加大

4. 基金市场观察
   - 43 只基金 6 月 16 日净值增长超 5%，最高回报 6.93%
   - 偏股型基金表现分化，净值回撤超 3% 的有 54 只
   - 基金经理跳槽现象明显，头部机构虹吸效应增强

5. 宏观经济数据
   - 2026 陆家嘴论坛 6 月 17-18 日召开
   - 5 月经济数据显示增长重心切换至高端制造、数字经济
   - 结构性行情是未来 A 股长期主流运行模式
"""

# 操作建议
RECOMMENDATIONS = """
【具体操作建议】

🟢 继续持有（表现优异）：
1. 交银双息平衡（519732）：+70.35%，今日 +1.87%，表现最优，建议继续持有
2. 华夏 5G 通信（515880）：+29.03%，金选指数基金，长期配置价值高
3. 广发全球精选（270023）：+37.42%，QDII 分散配置，今日 +0.36%
4. 易方达沪深 300（110020）：+56.82%，宽基指数，今日 +0.34%，建议定投继续

🟡 逢反弹减仓（亏损较大）：
1. 中欧医疗健康（003096）：-43.27%，医疗板块仍在底部，今日 -0.41%，建议反弹至 -35% 附近减仓
2. 景顺长城新兴成长（260108）：-47.93%，消费蓝筹调整较深，今日 -0.62%，建议反弹至 -40% 附近减仓
3. 招商白酒 A/C（161725/015280）：-48%/-53%，建议合并为 A 类份额（费率更优），反弹至 -40% 减仓

🔵 观察机会（今日反弹）：
1. 华夏芯片 ETF（008889）：-19.00%，今日 +1.31% 反弹，观察持续性，可持有等待板块轮动
2. 券商 ETF（512900）：-19.06%，持仓较重（10,556 元），关注资本市场改革预期，今日 -0.60%

🟠 配置优化建议：
1. 合并白酒 A+C：将 015280（C 类）转换为 161725（A 类），长期持有费率更优
2. 黄金占比调整：当前 17.1% 略高，美联储决议后可考虑调整至 10-15%
3. 增加债券基金：考虑配置 10% 纯债基金降低整体波动，实现股债平衡
4. 光伏/医疗：亏损超 30%，不建议割肉，等待行业周期反转

⚠️ 风险提示：
1. 美联储 6 月 18 日利率决议可能引发市场波动
2. 医疗、白酒板块仍在底部，需要耐心等待
3. 结构性行情下，避免资金全部集中在单一行业
"""

def generate_html_report():
    """生成 HTML 报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>基金评估报告 - {today}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
        .container {{ background: white; border-radius: 8px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a1a1a; border-bottom: 3px solid #1890ff; padding-bottom: 10px; }}
        h2 {{ color: #1890ff; margin-top: 30px; }}
        h3 {{ color: #333; }}
        .summary-box {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }}
        .summary-item {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; text-align: center; }}
        .summary-item.profit {{ background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }}
        .summary-item.loss {{ background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }}
        .summary-item .value {{ font-size: 24px; font-weight: bold; margin: 10px 0; }}
        .summary-item .label {{ font-size: 14px; opacity: 0.9; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #e8e8e8; }}
        th {{ background: #fafafa; font-weight: 600; color: #333; }}
        tr:hover {{ background: #f5f5f5; }}
        .positive {{ color: #52c41a; font-weight: 600; }}
        .negative {{ color: #ff4d4f; font-weight: 600; }}
        .tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-left: 5px; }}
        .tag-ding {{ background: #e6f7ff; color: #1890ff; }}
        .tag-jinxuan {{ background: #f6ffed; color: #52c41a; }}
        .tag-gold {{ background: #fff7e6; color: #fa8c16; }}
        .news-box {{ background: #fafafa; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .news-item {{ margin: 15px 0; padding-left: 15px; border-left: 3px solid #1890ff; }}
        .recommendation-box {{ background: #f6ffed; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid #b7eb8f; }}
        .recommendation-item {{ margin: 10px 0; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #e8e8e8; color: #999; font-size: 14px; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 基金评估报告</h1>
        <p><strong>报告日期：</strong>{today}</p>
        <p><strong>数据来源：</strong>天天基金网、东方财富、财联社、华尔街见闻</p>
        
        <h2>💰 账户总览</h2>
        <div class="summary-box">
            <div class="summary-item">
                <div class="label">总金额</div>
                <div class="value">¥{HOLDINGS["account_summary"]["total_amount"]:,.2f}</div>
            </div>
            <div class="summary-item loss">
                <div class="label">昨日收益</div>
                <div class="value">¥{HOLDINGS["account_summary"]["yesterday_profit"]:,.2f}</div>
            </div>
            <div class="summary-item loss">
                <div class="label">持有收益</div>
                <div class="value">¥{HOLDINGS["account_summary"]["holding_profit"]:,.2f}</div>
            </div>
            <div class="summary-item profit">
                <div class="label">累计收益</div>
                <div class="value">¥{HOLDINGS["account_summary"]["accumulated_profit"]:,.2f}</div>
            </div>
        </div>
        
        <h2>📈 持有基金明细</h2>
        <table>
            <thead>
                <tr>
                    <th>基金代码</th>
                    <th>基金名称</th>
                    <th>持有金额</th>
                    <th>昨日收益</th>
                    <th>持有收益</th>
                    <th>收益率</th>
                    <th>今日估值</th>
                    <th>标记</th>
                </tr>
            </thead>
            <tbody>
"""
    
    for fund in HOLDINGS["funds"]:
        code = fund["code"]
        name = fund["name"]
        amount = fund["amount"]
        yesterday_profit = fund["yesterday_profit"]
        holding_profit = fund["holding_profit"]
        rate = fund["rate"]
        tag = fund["tag"]
        
        # 获取今日估值数据
        today_change = "N/A"
        if code in TODAY_ESTIMATES:
            today_change = f"{TODAY_ESTIMATES[code]['change']:+.2f}%"
        
        # 格式化收益颜色
        yesterday_class = "positive" if yesterday_profit > 0 else "negative"
        holding_class = "positive" if holding_profit > 0 else "negative"
        rate_class = "positive" if rate > 0 else "negative"
        
        # 格式化标记
        tag_html = ""
        if tag == "定投":
            tag_html = '<span class="tag tag-ding">定投</span>'
        elif tag == "金选指数":
            tag_html = '<span class="tag tag-jinxuan">金选指数</span>'
        elif tag == "黄金":
            tag_html = '<span class="tag tag-gold">黄金</span>'
        
        html += f"""                <tr>
                    <td>{code}</td>
                    <td>{name}{tag_html}</td>
                    <td>¥{amount:,.2f}</td>
                    <td class="{yesterday_class}">¥{yesterday_profit:+,.2f}</td>
                    <td class="{holding_class}">¥{holding_profit:+,.2f}</td>
                    <td class="{rate_class}">{rate:+.2f}%</td>
                    <td>{today_change}</td>
                    <td>{tag_html}</td>
                </tr>
"""
    
    html += f"""            </tbody>
        </table>
        
        <h2>📰 今日财经新闻摘要</h2>
        <div class="news-box">
            <pre style="white-space: pre-wrap; font-family: inherit;">{NEWS_SUMMARY.strip()}</pre>
        </div>
        
        <h2>💡 操作建议</h2>
        <div class="recommendation-box">
            <pre style="white-space: pre-wrap; font-family: inherit;">{RECOMMENDATIONS.strip()}</pre>
        </div>
        
        <h2>📊 行业分布分析</h2>
        <table>
            <thead>
                <tr>
                    <th>行业/类型</th>
                    <th>金额</th>
                    <th>占比</th>
                    <th>盈亏状态</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>黄金</td><td>¥18,369.83</td><td>17.1%</td><td class="negative">-3.00%</td></tr>
                <tr><td>均衡/价值</td><td>¥25,276.80</td><td>23.6%</td><td>混合</td></tr>
                <tr><td>QDII（海外）</td><td>¥13,637.94</td><td>12.7%</td><td class="positive">+24%</td></tr>
                <tr><td>新能源/光伏</td><td>¥16,444.94</td><td>15.3%</td><td class="negative">-15%</td></tr>
                <tr><td>医疗</td><td>¥10,922.31</td><td>10.2%</td><td class="negative">-40%</td></tr>
                <tr><td>白酒/消费</td><td>¥11,892.55</td><td>11.1%</td><td class="negative">-45%</td></tr>
                <tr><td>科技（5G/芯片）</td><td>¥11,509.69</td><td>10.7%</td><td>混合</td></tr>
                <tr><td>券商</td><td>¥10,556.92</td><td>9.8%</td><td class="negative">-19%</td></tr>
            </tbody>
        </table>
        
        <div class="footer">
            <p>报告生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p>文件保存路径：/home/admin/openclaw/workspace/reports/fund-evaluation-{today}.html</p>
            <p>⚠️ 投资有风险，本报告仅供参考，不构成投资建议</p>
        </div>
    </div>
</body>
</html>
"""
    
    return html

def generate_wechat_text():
    """生成微信文字版报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    text = f"""📊 基金评估报告
报告日期：{today}

━━━━━━━━━━━━━━━━━━
💰 账户总览
━━━━━━━━━━━━━━━━━━

总金额：¥{HOLDINGS["account_summary"]["total_amount"]:,.2f}
昨日收益：¥{HOLDINGS["account_summary"]["yesterday_profit"]:,.2f}
持有收益：¥{HOLDINGS["account_summary"]["holding_profit"]:,.2f}
累计收益：¥{HOLDINGS["account_summary"]["accumulated_profit"]:,.2f}

━━━━━━━━━━━━━━━━━━
📈 今日基金表现
━━━━━━━━━━━━━━━━━━

【盈利基金】
"""
    
    # 按收益率排序
    profitable_funds = [f for f in HOLDINGS["funds"] if f["rate"] > 0]
    profitable_funds.sort(key=lambda x: x["rate"], reverse=True)
    
    for fund in profitable_funds:
        code = fund["code"]
        name = fund["name"][:15]
        rate = fund["rate"]
        amount = fund["amount"]
        today_change = ""
        if code in TODAY_ESTIMATES:
            today_change = f" | 今日 {TODAY_ESTIMATES[code]['change']:+.2f}%"
        text += f"• {name}：{rate:+.2f}%{today_change}\n"
    
    text += "\n【亏损基金】\n"
    
    loss_funds = [f for f in HOLDINGS["funds"] if f["rate"] <= 0]
    loss_funds.sort(key=lambda x: x["rate"])
    
    for fund in loss_funds[:10]:  # 只显示前 10 只亏损基金
        code = fund["code"]
        name = fund["name"][:15]
        rate = fund["rate"]
        today_change = ""
        if code in TODAY_ESTIMATES:
            today_change = f" | 今日 {TODAY_ESTIMATES[code]['change']:+.2f}%"
        text += f"• {name}：{rate:+.2f}%{today_change}\n"
    
    if len(loss_funds) > 10:
        text += f"• ... 还有{len(loss_funds) - 10}只基金\n"
    
    text += f"""
━━━━━━━━━━━━━━━━━━
📰 今日财经新闻摘要
━━━━━━━━━━━━━━━━━━

1️⃣ 美伊阶段性协议落定，风险溢价回落
   美伊签署谅解备忘录，中东局势缓和，A 股交易转向成长修复

2️⃣ 美联储 6 月利率决议前夕
   美联储主席沃什 6 月 17 日主持 FOMC 发布会，利率决议 6 月 18 日凌晨公布

3️⃣ 科技板块动态
   台积电发布玻璃基板开发计划，消费电子 ETF 大涨超 3%
   半导体指数隔夜跌近 6%，短期波动加大

4️⃣ 基金市场观察
   43 只基金 6 月 16 日净值增长超 5%，最高回报 6.93%
   偏股型基金表现分化，净值回撤超 3% 的有 54 只

5️⃣ 宏观经济数据
   2026 陆家嘴论坛 6 月 17-18 日召开
   结构性行情是未来 A 股长期主流运行模式

━━━━━━━━━━━━━━━━━━
💡 具体操作建议
━━━━━━━━━━━━━━━━━━

🟢 继续持有（表现优异）：
1. 交银双息平衡（+70.35%）：今日 +1.87%，表现最优
2. 华夏 5G 通信（+29.03%）：金选指数基金
3. 广发全球精选（+37.42%）：QDII 分散配置
4. 易方达沪深 300（+56.82%）：宽基指数，建议定投继续

🟡 逢反弹减仓（亏损较大）：
1. 中欧医疗健康（-43.27%）：反弹至 -35% 附近减仓
2. 景顺长城新兴成长（-47.93%）：反弹至 -40% 附近减仓
3. 招商白酒 A/C（-48%/-53%）：建议合并为 A 类份额

🔵 观察机会（今日反弹）：
1. 华夏芯片 ETF（-19.00%）：今日 +1.31%，观察持续性
2. 券商 ETF（-19.06%）：关注资本市场改革预期

🟠 配置优化建议：
1. 合并白酒 A+C：将 C 类转换为 A 类（费率更优）
2. 黄金占比调整：当前 17.1%，建议调整至 10-15%
3. 增加债券基金：配置 10% 纯债基金降低波动
4. 光伏/医疗：不建议割肉，等待行业周期反转

⚠️ 风险提示：
• 美联储 6 月 18 日利率决议可能引发市场波动
• 医疗、白酒板块仍在底部，需要耐心等待
• 结构性行情下，避免资金全部集中在单一行业

━━━━━━━━━━━━━━━━━━
📁 完整 HTML 报告已保存至：
/home/admin/openclaw/workspace/reports/fund-evaluation-{today}.html

投资有风险，本报告仅供参考，不构成投资建议
"""
    
    return text

if __name__ == "__main__":
    # 创建 reports 目录
    reports_dir = Path("/home/admin/openclaw/workspace/reports")
    reports_dir.mkdir(exist_ok=True)
    
    # 生成 HTML 报告
    today = datetime.now().strftime("%Y-%m-%d")
    html_path = reports_dir / f"fund-evaluation-{today}.html"
    
    html_content = generate_html_report()
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML 报告已生成：{html_path}")
    
    # 生成微信文字版
    wechat_text = generate_wechat_text()
    print("\n" + "="*60)
    print("微信文字版报告：")
    print("="*60)
    print(wechat_text)
