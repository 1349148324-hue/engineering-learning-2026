    # Git 高频命令清单（直接追加进笔记）
## 一、基础状态查看
```bash
git status          # 查看文件变动、暂存状态（最常用）
git log             # 查看提交记录
git log --oneline   # 精简单行日志，方便查看commit编号
```

## 二、提交三步标准流程
```bash
# 1. 将文件加入暂存区
git add 文件名.py
git add notes/xxx.md       # 指定文件夹
git add .                  # 当前目录所有变动文件（谨慎使用）

# 2. 本地提交，必须写清晰备注
git commit -m "[NOTES] 补充Linux命令"

# 3. 推送到远程GitHub
git push
```

## 三、仓库远程相关
```bash
git remote -v  # 查看当前远程仓库地址（区分SSH/HTTPS）
# 切换远程为SSH地址（解决你之前TLS网络报错）
git remote set-url origin git@github.com:1349148324-hue/engineering-learning-2026.git
```

## 四、撤销/回退（慎用）
```bash
git restore 文件名.py        # 放弃本地未暂存的修改
git reset HEAD 文件名.py     # 把文件从暂存区撤出来，保留本地改动
```

## 五、规范约定（咱们项目统一遵守）
- `[CODE]`：代码练习新增/修改
- `[NOTES]`：学习笔记
- `[STRUCT]`：目录结构、.gitignore、README骨架修改

## 六、你经常遇到的坑
1. **提交备注 `-m` 前后必须有空格**
   ❌ `git commit -m"xxx"`
   ✅ `git commit -m "xxx"`
2. 网络TLS报错：确认远程地址切换为SSH
3. 不要频繁 `git add .`，尽量精确指定文件，防止误上传垃圾文件

## 七、完整示范（本次笔记提交）
```bash
cd ~/code/engineering-learning-2026
git add notes/python_basic_summary.md
git commit -m "[NOTES] 追加Linux命令 + Git常用清单"
git push
```

---
全部粘贴保存后直接执行上面一套命令推上GitHub。
提交完毕，我们就继续 **ex06 密码验证程序**！