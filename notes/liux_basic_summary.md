# Linux（WSL Ubuntu）高频目录操作命令
可以直接复制追加到 `python_basic_summary.md`

## 一、切换目录 cd
```bash
cd ..          # 返回【上一级】文件夹（最常用）
cd ../..       # 往上连续跳两级
cd .           # 当前目录（基本很少用）
cd ~           # 直接回到你的家目录 /home/mylinux
cd -           # 切换回【上一次所在目录】，来回跳转神器
cd 文件夹名     # 进入当前目录下的子文件夹
cd /home/mylinux/code  # 绝对路径直达
```
⚠️ 重点：`cd` 和 `..` 中间**必须有空格**
错误：`cd..`   正确：`cd ..`

## 二、查看当前位置
```bash
pwd    # 打印当前完整路径 print working directory
```

## 三、列出文件夹内容 ls
```bash
ls         # 列出文件、文件夹
ls -l      # 详细列表（权限、大小、修改时间）
ls -a      # 显示隐藏文件（以 . 开头，比如 .gitignore、.ssh）
ls -la     # 详细列表 + 显示隐藏文件
```

## 四、创建文件夹
```bash
mkdir 文件夹名
mkdir -p week01/code   # -p：多级目录一次性创建，不存在父目录也不会报错
```

## 五、创建空文件
```bash
touch test.py
touch README.md
```

## 六、删除（谨慎！Linux删除无回收站）
```bash
rm 文件名                  # 删除文件
rm -i 文件名               # -i 删除前询问（强烈推荐日常使用，防误删）
rm -r 文件夹名             # 删除文件夹（文件夹不为空必须加 -r）
```

## 七、复制文件/文件夹
```bash
cp 源文件 目标文件
cp test.py week01/
cp -r 文件夹A 文件夹B     # -r 复制整个文件夹（包含内部所有内容）
```

## 八、移动/重命名
```bash
# 移动文件到另一个目录
mv test.py week01/code/

# 重命名（同目录移动 = 改名）
mv old.py new.py
```

## 九、查找文件（简单用法）
```bash
find . -name "*.py"    # 在当前目录递归查找所有 .py 文件
find . -name "README*"
```

## 十、路径两种写法
1. **相对路径**：从你**现在所在位置**开始写
`notes/python_basic_summary.md`
2. **绝对路径**：从根目录完整地址，任何位置都能用
`/home/mylinux/code/engineering-learning-2026/notes/python_basic_summary.md`

## 十一、实用小技巧
1. **Tab自动补全**
输入文件夹/文件名前几个字母，按Tab一键补全，减少拼写错误。
2. 命令太长输错：Ctrl+C 终止当前命令，回到提示符
3. 上下方向键：调取历史命令，不用重复敲打

## 十二、和你项目配套示范
```bash
# 当前在 exercises，去 notes 放笔记
cd ..
cd notes

# 回到 exercises
cd ../exercises
```

## 十三、常见踩坑
1. 文件夹名称带空格：要用引号包裹 `"my folder"`，尽量命名不用空格，改用下划线 `week_01`
2. 区分大小写！Ubuntu：`Notes` 和 `notes` 是两个不同文件夹
3. 不要随便 `rm -rf`，风险极高，日常优先 `rm -i`

---
粘贴进 `notes/python_basic_summary.md` 之后，执行提交：
```bash
git add notes/python_basic_summary.md
git commit -m "[NOTES] 补充Linux基础目录操作命令"
git push
```

如果你想要，我再补充一份 **Git高频命令清单** 一并放进笔记。