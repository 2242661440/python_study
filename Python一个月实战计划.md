# Python 一个月实战计划：数据处理与自动化

<a id="top"></a>

> 目标：一个月内掌握 Python 数据处理基础，能读取 CSV、检查数据质量、输出结果，并和 SQL 学习内容连接起来。

---

## 目录

- [1. 学习定位](#section-1)
- [2. 学习环境](#section-2)
- [3. 一个月学习节奏](#section-3)
- [4. 30 天实战安排](#section-4)
- [5. 每次对 Codex 的指令模板](#section-5)
- [6. 练习题型](#section-6)
- [7. 最终小项目](#section-7)
- [8. 日语面试表达](#section-8)
- [9. 检查表](#section-9)

---

<a id="section-1"></a>

## 1. 学习定位

Python 不是为了走纯开发路线，而是为了服务数据工程：

```text
读取 CSV
清洗数据
检查重复
检查 NULL
统计件数
输出检查结果
自动化日常操作
辅助 SQL / ETL 验证
```

[返回顶部](#top)

---

<a id="section-2"></a>

## 2. 学习环境

当前环境：

```text
Python 3.13
pip
VS Code
```

建议目录：

```text
C:\Lin\Study\python_study
  data\
  output\
  src\
  notes\
```

确认命令：

```powershell
python --version
pip --version
```

[返回顶部](#top)

---

<a id="section-3"></a>

## 3. 一个月学习节奏

每天 Python 建议投入 45 到 60 分钟。

```text
10分钟：复习语法
20分钟：写小代码
20分钟：处理 CSV / JSON
10分钟：整理错误点
```

[返回顶部](#top)

---

<a id="section-4"></a>

## 4. 30 天实战安排

| 天数 | 主题 | 实战目标 |
| --- | --- | --- |
| Day 1 | 变量 / print | 能输出检查结果 |
| Day 2 | if | 能判断金额异常 |
| Day 3 | for | 能循环处理数据 |
| Day 4 | list / dict | 能保存多条记录 |
| Day 5 | 函数 | 能封装检查逻辑 |
| Day 6 | 字符串处理 | 能处理空白和格式 |
| Day 7 | Week 1 复习 | 完成基础语法练习 |
| Day 8 | 文件读取 | 读取 txt |
| Day 9 | 文件输出 | 输出检查结果 |
| Day 10 | CSV 读取 | 读取 contracts.csv |
| Day 11 | CSV 输出 | 输出 check_result.csv |
| Day 12 | 重复检查 | 检查 contract_id 重复 |
| Day 13 | NULL 检查 | 检查必填字段为空 |
| Day 14 | Week 2 复习 | 完成 CSV 检查脚本初版 |
| Day 15 | JSON 基础 | 读取 API 风格数据 |
| Day 16 | 异常处理 | 使用 try / except |
| Day 17 | pathlib | 处理文件路径 |
| Day 18 | datetime | 处理日期 |
| Day 19 | pandas 读取 CSV | 使用 read_csv |
| Day 20 | pandas 筛选 | 过滤异常数据 |
| Day 21 | Week 3 复习 | 完成 pandas 数据检查 |
| Day 22 | groupby | 按 status 统计 |
| Day 23 | merge 概念 | 理解类似 JOIN 的处理 |
| Day 24 | 与 SQL 对照 | Python 检查结果和 SQL 比较 |
| Day 25 | 输出报告 | 输出 summary.csv |
| Day 26 | 综合任务 1 | 检查重复、NULL、异常金额 |
| Day 27 | 综合任务 2 | 按状态统计件数 |
| Day 28 | 综合任务 3 | 生成检查报告 |
| Day 29 | 面试整理 | 整理 Python 学习中说法 |
| Day 30 | 总复习 | 完成数据质量检查脚本 |

[返回顶部](#top)

---

<a id="section-5"></a>

## 5. 每次对 Codex 的指令模板

```text
今天是 Python 学习 Day X。请按照 C:\Lin\Study\python_study\Python一个月实战计划.md 带我学习。
请先说明今天目标，再讲解语法，给 3 个例子，出 5 道练习题。
练习要贴近 CSV、数据检查、ETL、自动化,最后整理今天笔记和日语面试表达。
```

批改代码：

````text
这是我写的 Python 代码，请帮我检查：
1. 能否运行
2. 是否符合题目
3. 有没有更简单写法
4. 实际项目中要注意什么

```python
-- 粘贴我的代码
```
````

[返回顶部](#top)

---

<a id="section-6"></a>

## 6. 练习题型

```text
读取 CSV 文件
统计总件数
检查重复主键
检查 NULL
过滤异常金额
按 status 统计
输出 CSV 检查结果
和 SQL 查询结果对照
```

[返回顶部](#top)

---

<a id="section-7"></a>

## 7. 最终小项目

项目名：

```text
CSV契約データ品質チェックツール
```

功能：

```text
1. 读取 contracts.csv
2. 检查 contract_id 重复
3. 检查 customer_id、contract_date、amount 的 NULL
4. 检查 amount 是否为 0 或负数
5. 按 status 统计件数
6. 输出 check_result.csv
7. 整理日语说明
```

最终文件：

```text
C:\Lin\Study\python_study\src\data_quality_check.py
C:\Lin\Study\python_study\output\check_result.csv
C:\Lin\Study\python_study\notes\Python数据处理总结.md
```

[返回顶部](#top)

---

<a id="section-8"></a>

## 8. 日语面试表达

```text
Pythonについては、現在データ処理や自動化の用途で学習しています。
CSVファイルの読み込み、データチェック、重複確認、NULL確認、集計処理など、ETLやデータ移行作業に近い内容を練習しています。
```

[返回顶部](#top)

---

<a id="section-9"></a>

## 9. 检查表

- [ ] 能写变量、if、for、函数
- [ ] 能读取和输出文件
- [ ] 能读取 CSV
- [ ] 能检查重复和 NULL
- [ ] 能按状态统计件数
- [ ] 能使用 pandas 做基础筛选
- [ ] 能完成数据质量检查脚本

[返回顶部](#top)
