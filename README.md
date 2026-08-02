# engineering-learning-2026
个人工程学习仓库，持续记录课程实验、算法练习、技术笔记与项目实践。
依托 WSL Ubuntu + VSCode 作为主力开发环境，所有内容使用 Git 版本控制并托管至 GitHub。

## 📁 仓库目录结构
engineering-learning-2026
├── exercises # 课后习题、小型实验、零散代码练习
├── notes # 知识点笔记、文档、资料摘录、思路草稿
├── week01 # 第一周学习内容
└── README.md # 仓库总说明
plaintext
> 后续按学习进度新增 `week02` / `week03` 等目录，对应每周任务。

## 🎯 学习目标
1. 夯实编程基础，规范代码书写与工程目录管理习惯
2. 熟练使用 Git 完成本地版本管理 + GitHub 远程托管
3. 持续沉淀可复用笔记与实验代码，方便复盘、检索
4. 形成标准化学习流程：实践 → 记录 → 提交归档

## 📝 提交规范
每次改动统一遵循工作流：
```bash
git status
git add .
git commit -m "简短清晰的修改说明"
git push
提交信息建议分类前缀，示例：
[NOTE] 补充xxx知识点笔记
[CODE] 新增week01练习代码
[FIX] 修正代码逻辑/文档笔误
[STRUCT] 调整目录结构
💻 开发环境
操作系统：Windows + WSL2 Ubuntu
编辑器：VS Code（WSL 远程连接）
版本控制：Git
远程托管：GitHub
📅 学习进度记录
DAY1：搭建 WSL+VSCode 开发环境；初始化 Git 仓库；创建基础目录骨架；关联并推送至 GitHub；清理冗余文件；完善仓库 README 文档。
📌 后续规划
每周固定在对应 weekXX 目录存放练习与笔记
重要实验附带简要说明、运行思路
定期整理笔记，提炼成可复用知识库
plaintext

### 执行命令
粘贴保存后运行：
```bash
git add .
git commit -m "update README: 扩充项目简介、环境与学习规范"
git push