# Python 一个月实战计划：数据工程强化版

<a id="top"></a>

> 目标：在兼顾 SQL、Linux、网络、AWS 学习的前提下，用 1 个月把 Python 学到“能实际处理数据”的程度。重点不是做纯 Python 开发，而是能写数据处理脚本、自动化检查脚本，并能把成果用于数据工程、ETL、数据迁移和面试表达。

---

## 目录

- [1. 大纲确认](#section-1)
- [2. 学习定位](#section-2)
- [3. 环境配置路线](#section-3)
- [4. 学习资料使用范围](#section-4)
- [5. 每天学习节奏](#section-5)
- [6. 30 天实战计划](#section-6)
- [7. 每周成果物](#section-7)
- [8. 最终小项目](#section-8)
- [9. 每次让 Codex 带学的指令模板](#section-9)
- [10. 日语面试表达](#section-10)
- [11. 检查表](#section-11)

---

<a id="section-1"></a>

## 1. 大纲确认

本计划参考：

```text
C:\Lin\职业规划\职业规划_一个月学习计划.md
C:\Lin\Study\python_study\README.md
C:\Lin\Study\python_study\learning-notes
C:\Lin\Study\python_study\Python一个月实战计划.md
```

总学习方向确认如下：

```text
第 1 周：SQL 强化
第 2 周：Linux + 网络基础
第 3 周：Python 数据处理
第 4 周：AWS + 小项目 + 面试整理
```

但是 Python 不能只放到第 3 周才开始。建议从 Day 1 开始每天安排 45 到 60 分钟 Python，前两周打基础，第 3 周集中做数据处理，第 4 周和 SQL / AWS / 项目说明连接起来。

Python 的主线是：

```text
环境配置
基础语法
文件处理
CSV / JSON
异常处理
pandas
数据质量检查
SQL 对照
小项目整理
日语面试表达
```

[返回顶部](#top)

---

<a id="section-2"></a>

## 2. 学习定位

Python 的学习目标不是转向纯开发岗位，而是服务你的数据工程方向：

```text
读取 CSV
清洗数据
检查重复
检查 NULL
检查异常金额
统计件数
输出结果文件
自动化日常检查
辅助 SQL / ETL 验证
整理项目成果
```

你最终要达到的状态：

```text
看到一个数据文件，能用 Python 快速读取、检查、统计、输出结果。
看到一个数据检查需求，能判断用 SQL 做还是用 Python 做更合适。
面试时能自然说明：我正在把 ETL / SQL 经验扩展到 Python 自动化和数据处理。
```

[返回顶部](#top)

---

<a id="section-3"></a>

## 3. 环境配置路线

### Day 1 先确认环境

在 PowerShell 执行：

```powershell
python --version
pip --version
where python
```

目标结果：

```text
能看到 Python 版本
能看到 pip 版本
能确认 Python 安装路径
```

### 推荐目录结构

继续使用当前目录：

```text
C:\Lin\Study\python_study
  data\
  output\
  src\
  notes\
  learning-notes\
```

建议新增练习文件：

```text
C:\Lin\Study\python_study\src\day01_hello.py
C:\Lin\Study\python_study\src\data_quality_check.py
C:\Lin\Study\python_study\data\contracts.csv
C:\Lin\Study\python_study\output\check_result.csv
C:\Lin\Study\python_study\notes\Python学习记录.md
```

### VS Code 配置重点

先确认 3 件事：

```text
1. VS Code 能打开 C:\Lin\Study\python_study
2. 右下角或命令面板能选择 Python 解释器
3. 能在终端运行 python src\day01_hello.py
```

### 第一次安装库

第 1 周先不急着装很多库。到 pandas 学习前再安装：

```powershell
pip install pandas
```

验证：

```powershell
python -c "import pandas as pd; print(pd.__version__)"
```

[返回顶部](#top)

---

<a id="section-4"></a>

## 4. 学习资料使用范围

不要从 `python100` 第 1 篇一路学到第 100 篇。这个月只筛选和数据工程有关的内容。

### 必学资料

```text
01.初识Python.md
02.语言元素.md
03.分支结构.md
04.循环结构.md
05.构造程序逻辑.md
06.函数和模块的使用.md
07.字符串和常用数据结构.md
11.文件和异常.md
12.字符串和正则表达式.md
16-20.Python语言进阶.md
66.数据分析概述.md
67.环境准备.md
72.深入浅出pandas-1.md
73.深入浅出pandas-2.md
74.深入浅出pandas-3.md
75.深入浅出pandas-4.md
76.深入浅出pandas-5.md
77.深入浅出pandas-6.md
44.Python接入MySQL数据库.md
PEP8风格指南.md
Python编程惯例.md
```

### 选学资料

```text
57.接入三方平台.md
61.网络数据采集概述.md
62.用Python获取网络资源-1.md
62.用Python解析HTML页面-2.md
59.单元测试.md
96.软件测试和自动化测试.md
94.网络API接口设计.md
Python数据分析师面试题.md
100.Python面试题实录.md
```

### 暂时不作为重点

```text
Django / DRF
GUI / 游戏开发
机器学习 / 深度学习
Scrapy / Selenium 深入
Docker 深入
项目上线深入
```

原因：这些内容有价值，但和你这个月的主目标“数据工程基础 + Python 数据处理小项目”关系不如 CSV、pandas、SQL 对照直接。

[返回顶部](#top)

---

<a id="section-5"></a>

## 5. 每天学习节奏

如果当天总学习 4 到 6 小时，Python 建议这样安排：

```text
10分钟：复习昨天代码
15分钟：学习一个语法点
25分钟：写一个小练习
10分钟：整理错误和日语表达
```

如果当天只有 2 小时总学习时间，Python 最少保留：

```text
10分钟：看昨天代码
25分钟：写一个小练习
10分钟：记录 3 行笔记
```

每天固定输出：

```text
1. 一个 .py 练习文件
2. 三条学习笔记
3. 一个和数据处理有关的小例子
4. 一句日语技术表达
```

[返回顶部](#top)

---

<a id="section-6"></a>

## 6. 30 天实战计划

| 天数 | Python 主题 | 实战目标 | 对应总学习主线 |
| --- | --- | --- | --- |
| Day 1 | 环境确认 / print | 跑通第一个 Python 文件 | SQL 周开始 |
| Day 2 | 变量 / 数据类型 | 保存合同ID、金额、状态 | SQL 条件查询 |
| Day 3 | if 判断 | 判断金额是否异常 | SQL WHERE |
| Day 4 | for 循环 | 循环处理多条合同数据 | SQL GROUP BY |
| Day 5 | list / dict | 用字典保存一条合同记录 | SQL JOIN |
| Day 6 | 函数 | 封装 `check_amount()` | SQL 数据检查 |
| Day 7 | Week 1 复习 | 完成基础语法小练习 | SQL 模板整理 |
| Day 8 | 字符串处理 | 去掉空格、统一状态值 | Linux 文件操作 |
| Day 9 | 文件读取 | 读取 txt 日志或数据文件 | Linux grep / find |
| Day 10 | 文件输出 | 输出简单检查结果 | Linux 日志确认 |
| Day 11 | CSV 读取 | 读取 `contracts.csv` | Shell 基础 |
| Day 12 | CSV 输出 | 输出 `check_result.csv` | 网络基础 |
| Day 13 | JSON 基础 | 读取 API 风格 JSON | API / JSON |
| Day 14 | Week 2 复习 | 完成 CSV 读写脚本初版 | Linux + 网络整理 |
| Day 15 | 异常处理 | 用 `try / except` 处理文件不存在 | Python 集中周 |
| Day 16 | pathlib | 用路径对象管理 data / output | Python 集中周 |
| Day 17 | datetime | 检查日期格式 | Python 集中周 |
| Day 18 | 重复检查 | 检查 `contract_id` 重复 | Python 集中周 |
| Day 19 | NULL 检查 | 检查必填字段为空 | Python 集中周 |
| Day 20 | pandas 读取 CSV | 用 `read_csv()` 读取数据 | Python 集中周 |
| Day 21 | Week 3 复习 | 完成 pandas 数据检查脚本 | Python 成果整理 |
| Day 22 | pandas 筛选 | 筛选异常金额数据 | AWS 整体结构 |
| Day 23 | groupby | 按 `status` 统计件数 | S3 / RDS |
| Day 24 | merge | 理解 Python 里的 JOIN | Lambda / CloudWatch |
| Day 25 | SQL 对照 | 对比 Python 检查和 SQL 检查 | Glue / Athena |
| Day 26 | 综合任务 1 | 设计数据质量检查流程 | 小项目设计 |
| Day 27 | 综合任务 2 | 实现 `data_quality_check.py` | 小项目实现 |
| Day 28 | 输出报告 | 生成 `check_result.csv` 和 summary | 项目总结 |
| Day 29 | 面试整理 | 写日语项目说明 | 模拟面试 |
| Day 30 | 总复习 | 整理 Python 数据处理总结 | 下月计划 |

[返回顶部](#top)

---

<a id="section-7"></a>

## 7. 每周成果物

### 第 1 周成果

```text
src\day01_hello.py
src\day03_check_amount.py
src\day06_functions.py
notes\Python基础语法笔记.md
```

会说清楚：

```text
变量、if、for、list、dict、函数分别用来做什么。
```

### 第 2 周成果

```text
src\day11_read_csv.py
src\day12_write_csv.py
src\day13_read_json.py
notes\Python文件处理笔记.md
```

会做：

```text
读取文件
输出文件
读取 CSV
读取 JSON
```

### 第 3 周成果

```text
src\day18_check_duplicate.py
src\day19_check_null.py
src\day21_pandas_check.py
notes\Python数据检查笔记.md
```

会做：

```text
重复检查
NULL 检查
异常值过滤
pandas 基础筛选
```

### 第 4 周成果

```text
src\data_quality_check.py
output\check_result.csv
output\summary.csv
notes\Python数据处理总结.md
notes\project_summary_ja.md
```

会说明：

```text
这个脚本解决什么问题
输入是什么
处理逻辑是什么
输出是什么
和 SQL / ETL 工作有什么关系
```

[返回顶部](#top)

---

<a id="section-8"></a>

## 8. 最终小项目

项目名：

```text
CSV契約データ品質チェック・集計ツール
```

### 输入文件

```text
C:\Lin\Study\python_study\data\contracts.csv
```

建议字段：

```text
contract_id
customer_id
contract_date
amount
status
updated_at
```

### 处理内容

```text
1. 读取 contracts.csv
2. 检查总件数
3. 检查 contract_id 是否重复
4. 检查 customer_id、contract_date、amount 是否为空
5. 检查 amount 是否为 0 或负数
6. 按 status 统计件数
7. 输出 check_result.csv
8. 输出 summary.csv
9. 写一份日语项目说明
```

### 最终文件

```text
C:\Lin\Study\python_study\src\data_quality_check.py
C:\Lin\Study\python_study\output\check_result.csv
C:\Lin\Study\python_study\output\summary.csv
C:\Lin\Study\python_study\notes\project_summary_ja.md
```

### 和 SQL 的连接

同样的检查也要能用 SQL 表达：

```sql
SELECT COUNT(*) FROM contracts;

SELECT contract_id, COUNT(*) AS cnt
FROM contracts
GROUP BY contract_id
HAVING COUNT(*) > 1;

SELECT *
FROM contracts
WHERE customer_id IS NULL
   OR contract_date IS NULL
   OR amount IS NULL;

SELECT status, COUNT(*) AS cnt
FROM contracts
GROUP BY status;
```

[返回顶部](#top)

---

<a id="section-9"></a>

## 9. 每次让 Codex 带学的指令模板

### 每天开始学习

```text
今天是 Python 学习 Day X。请按照 C:\Lin\Study\python_study\Python一个月实战计划_数据工程强化版.md 带我学习。
请先说明今天目标，再讲解必要语法，给 3 个贴近数据处理的例子，最后出 5 道练习题。
练习要贴近 CSV、JSON、数据质量检查、SQL 对照、ETL、自动化。
最后请整理今天笔记和一句日语面试表达。
```

### 让 Codex 检查代码

````text
这是我写的 Python 代码，请帮我检查：
1. 能否运行
2. 是否符合题目
3. 有没有更简单写法
4. 是否适合实际项目
5. 和 SQL / ETL 工作有什么关系

```python
-- 粘贴我的代码
```
````

### 让 Codex 出实战题

```text
请根据我今天学的内容，出 5 道 Python 数据处理练习题。
难度从简单到稍难。
题目要围绕 contracts.csv、数据检查、重复检查、NULL检查、状态统计。
```

[返回顶部](#top)

---

<a id="section-10"></a>

## 10. 日语面试表达

### Python 学习中

```text
Pythonについては、現在データ処理や自動化の用途で学習しています。
CSVファイルの読み込み、データチェック、重複確認、NULL確認、集計処理など、ETLやデータ移行作業に近い内容を練習しています。
```

### 完成小项目后

```text
Pythonとpandasを使用して、契約データの品質チェックツールを作成しました。
CSVデータを読み込み、重複チェック、NULLチェック、金額の異常値チェック、ステータス別の件数集計を行い、結果をCSVとして出力しました。
ETL処理やデータ移行時の検証作業を想定して実装しました。
```

### 不要夸大经验的说法

```text
実務でPythonを深く使った経験はまだ多くありませんが、SQLやETLの経験を活かして、データ処理や自動化の用途で学習を進めています。
```

[返回顶部](#top)

---

<a id="section-11"></a>

## 11. 检查表

### 环境

- [ ] `python --version` 能正常显示
- [ ] `pip --version` 能正常显示
- [ ] VS Code 能选择 Python 解释器
- [ ] 能运行 `src\day01_hello.py`
- [ ] 能安装并导入 pandas

### 基础语法

- [ ] 能写变量和 `print`
- [ ] 能写 `if`
- [ ] 能写 `for`
- [ ] 能使用 `list`
- [ ] 能使用 `dict`
- [ ] 能定义函数

### 文件和数据处理

- [ ] 能读取 txt
- [ ] 能输出 txt
- [ ] 能读取 CSV
- [ ] 能输出 CSV
- [ ] 能读取 JSON
- [ ] 能处理文件不存在等异常

### 数据质量检查

- [ ] 能统计总件数
- [ ] 能检查重复 `contract_id`
- [ ] 能检查 NULL
- [ ] 能检查异常金额
- [ ] 能按 `status` 统计件数
- [ ] 能用 pandas 完成基础筛选

### 项目和面试

- [ ] 完成 `data_quality_check.py`
- [ ] 输出 `check_result.csv`
- [ ] 输出 `summary.csv`
- [ ] 写好 `project_summary_ja.md`
- [ ] 能用日语说明项目目标、处理内容和结果

[返回顶部](#top)
