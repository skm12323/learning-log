# learn/ 工作区导航

> 位置：`D:\learn`（Windows 本地）。在 WSL 终端里访问同一目录用路径 `/mnt/d/learn`。
> 日常用 VS Code 直接打开 `D:\learn` 工作即可；跑计算密集的任务（Ising 大网格、小 GPT 训练）时，
> 建议把该项目的文件夹临时拷进 WSL 主目录再运行（`cp -r /mnt/d/learn/projects/ising ~/ && cd ~/ising`），跑完把结果拷回来——跨系统文件 IO 慢，纯计算要避开。

## 目录 ↔ 阶段/任务对应

| 目录 | 放什么 | 对应任务 |
|---|---|---|
| `log/` | **learning-log 仓库**（T04 在这里 git init），每周笔记 | T04 + 每周日晚复盘 |
| `log/weekly/` | 每周笔记，命名 `w2-2026-09-21.md` | 全程 |
| `log/refs/` | 三份计划文档的副本 + 速查表（原件也在本目录根） | T04 |
| `courses/ai/` | 高阳课：讲义笔记、编程作业 | 【课】固定动作 |
| `courses/cpp/` | 张焕晨课：课件笔记、作业 | 【课】固定动作 |
| `courses/linalg/` | 宋一凡线代：笔记、习题 | 跟课 |
| `courses/phys2/` | 普物(2)英：笔记 | 跟课 |
| `practice/leetcode/01-array … 06-dp/` | 刷题线①~⑥，命名 `0001-two-sum.py` | T13/T19/T24/T30/T36/T41 |
| `practice/kr-exercises/` | K&R 习题，按 `ch5/e5-03.c` 分章放 | C 长线 |
| `practice/drills/` | 语法/NumPy 向量化/装饰器等小练习 | T15/T17/T18 |
| `labs/bomb-lab/` | bomb lab 文件 + `notes.md` 拆弹笔记 | 每周 1 关 |
| `projects/ising/` | ★T20：2D Ising 蒙特卡洛 | 阶段 1 |
| `projects/micrograd/follow/` | T23 跟敲 Karpathy 的版本 | 阶段 2 |
| `projects/micrograd/rewrite/` | ★T25 合卷重写版（只有这份算数） | 阶段 2 |
| `projects/cn-gpt/` | ★★T37~T40：中文小 GPT 大作业 | 阶段 3 |
| `projects/qsim/` | ★T44：量子态矢量模拟器 | 阶段 4 |
| `papers/` | 论文/讲义 PDF + 阅读笔记：`aiayn.md`、`preskill-ch1.md` | T33/T42 |

根目录另有的三份文件（`两个月学习计划.md`、`学习任务清单.md`、`学习资源对照表.md`）是计划原件，日常勾选直接改根目录这份。

## 命名约定

- 周笔记：`log/weekly/w{周号}-{周一日期}.md`，如 `w6-2026-10-19.md`
- 刷题：`practice/leetcode/{NN-topic}/{题号}-{slug}.{py|c|cpp}`，一题一文件
- K&R：`practice/kr-exercises/ch{N}/e{N}-{M}.c`
- 项目 README 一律写：目的 / 结构 / 怎么跑 / 结果（对应 T40e 的模板）

## 项目"毕业"流程（portfolio 之路）

1. 项目完成后：在项目目录内 `git init`，写好 README（按上面模板）
2. GitHub 建同名空仓库，`git remote add origin … && git push`
3. 在当周周笔记里记下仓库链接
4. W8/T52 时 `projects/` 下应至少有 4 个毕业仓库：ising / micrograd(rewrite) / cn-gpt / qsim

## 日常动线

- 开始一天：打开本目录，看 `log/weekly/` 最新一篇的"下周计划"
- 写代码：文件进对应子目录，别散在根目录
- 周日晚 30 分钟：勾任务清单 → 写周笔记 → commit + push `log/`
