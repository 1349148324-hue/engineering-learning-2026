# engineering-learning-2026
## 项目简介
本仓库用于系统记录工程编程学习全过程，主线以 **Ubuntu(WSL2) + VS Code + Python + Git/GitHub** 为基础环境，循序渐进夯实编程基础、工程规范与版本控制能力。

学习重心：Python基础语法、命令行程序开发、异常处理、文件IO、函数封装，后续延伸至数据处理、算法工程实践。

## 环境说明
- 运行环境：WSL2 Ubuntu
- 开发工具：VS Code（远程WSL连接）
- 语言：Python3
- 版本管理：Git + GitHub

## 仓库目录结构
```
engineering-learning-2026/
├── week01/                 # 第一周学习内容
│   ├── code/               # 课堂核心代码
│   │   ├── basic_demo.py   # 均值/最值/标准差 + 文件读写+异常捕获
│   │   ├── sensor_data.txt# 测试数据源
│   │   └── stats_result.txt# 程序输出结果
│   └── exercises/          # WEEK01 15道Python基础练习题
├── notes/                  # 学习笔记、命令汇总、踩坑记录
└── README.md               # 仓库说明文档
```

## WEEK01 学习目标
### 学习内容
1. WSL2 Ubuntu基础操作
2. VS Code远程开发、Python运行环境
3. Git基础操作与GitHub仓库协作
4. Python变量、类型、输入输出
5. 条件分支、循环、自定义函数
6. 文件读写、try-except异常处理

### 已完成
- WSL2 + VS Code远程开发环境搭建
- Git初始化，成功建立并推送代码至GitHub远程仓库
- 实现统计工具函数：平均值、最大最小值、总体标准差
- 封装带异常捕获的文本读取/结果写入函数
- 完成全套单元测试，兼容空数据、缺失文件、非法文本等异常场景
- 通过本周基础验收标准：独立写读取文本函数、带异常处理命令行程序、环境可复现运行

### 待完成
- 在 `week01/exercises/` 完成至少15道Python基础练习
- 完成新一轮完整Git提交并推送至远程仓库

## 提交规范
commit 信息格式参考：
```
[WEEKxx] 简短描述
```
示例：
```
[WEEK01] 完成均值/最值/标准差，文件读写与异常捕获
[WEEK01] 完成15道Python基础练习：输入输出/条件/循环/函数/异常
```

## 如何在新环境复现项目
1. Windows开启WSL2，安装Ubuntu
2. Ubuntu内安装基础工具
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv git
```
3. VS Code安装WSL扩展，连接远程Ubuntu
4. 克隆仓库
```bash
git clone https://github.com/你的用户名/engineering-learning-2026.git
cd engineering-learning-2026
```
5. 进入对应目录运行Python代码
```bash
cd week01/code
python3 basic_demo.py
```

## 后续规划
- 夯实Python基础，强化工程思维：函数封装、异常鲁棒性、代码可读性
- 逐步拓展：数据处理、简单算法、模块化项目结构
- 持续保持规范Git提交习惯，沉淀可追溯学习档案

## 个人验收标准（通用）
1. 不依赖AI独立完成基础函数与命令行程序
2. 代码具备基础异常处理，避免程序直接崩溃
3. 项目可在全新WSL环境直接复现运行
4. 遵循版本控制规范，提交信息清晰可读

---
你直接复制全部内容覆盖原有`README.md`，保存后可以执行：
```bash
git add README.md
git commit -m "[DOC] 更新仓库README，同步WEEK01最新进度"
git push
```

如果你想要更精简版本（适合GitHub首页简洁展示），我可以再压缩一版。