# Python 第 2 讲（详细版 v2）：条件、循环、dict、set 与推导式

> 对应廖雪峰教程 5.4~5.6（推导式来自 7.1，提前学）。v2 扩充版：每个概念按"为什么需要 → 怎么用 → 什么时候用 → 陷阱"展开，示例全部实测。
> 用法：`(learn)` 环境 jupyter lab 里逐段跟敲，**每个代码块都亲手跑**；课后做 ex1~ex8 发回批改。
> 2026-09-11 首版 / 2026-09-11 v2 扩充

---

## 0. 这一讲在整门课里的位置

第 1 讲解决"**数据放哪**"（变量、str、list、tuple）；本讲解决两件新事：**程序怎么动起来**（条件 = 分支，循环 = 重复），以及**数据怎么组织得查得快**（dict、set）。加上把"循环+收集"压成一行的推导式，学完你就能写出真正的数据处理程序：遍历一批能量、筛出超阈值的、统计每个词出现几次——这正是高阳课编程作业的基本形态。

四个主角一句话：**if 让程序会拐弯，for/while 让程序会重复，dict 让查找一步到位，推导式让三行变一行。**

## 1. 条件判断 if / elif / else

### 1.1 为什么需要：程序不能只会走直线

直线程序只能"输入→算→输出"。真实逻辑充满分支：能量高于阈值做吸收处理、否则透射；分数 90 以上给 A……**分支 = 让程序根据数据的值选择不同的路**。

### 1.2 基本形态：冒号 + 缩进

```python
E = 2.5
if E > 1.0:
    action = "absorbed"
elif E < 0.5:
    action = "transmitted"
else:
    action = "partial"
```

五条语法规则，一条都不能省：

1. 条件行末尾**冒号**
2. 下一行**缩进 4 个空格**——缩进就是 Python 的"块"，没有大括号
3. `elif`（不是 else if），可以连续多个
4. `else` 兜底，可省略（省略 = 什么都不匹配就跳过）
5. 回到上一层的缩进 = 块结束

**elif 链从上往下短路，命中即止**——这个顺序本身就是逻辑。经典的成绩分级：

```python
score = 85
if score >= 90:        # 85 < 90，False，往下
    grade = "A"
elif score >= 80:      # 85 ≥ 80，命中！grade = "B"
    grade = "B"        # 之后的分支看都不看——所以不需要写 80 <= score < 90
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

正因为短路，条件**不需要写全区间**（`elif score >= 80` 而非 `elif 80 <= score < 90`）——能走到这一行就意味着前面都不成立。把区间写全反而是冗余坏味道。

### 1.3 真值：什么算 False

只有这些对象是假：`False`、`None`、`0`、`0.0`、`''`、`[]`、`{}`、`set()`、`()`。**其他一切都为真**——包括 `"False"` 这个非空字符串、`-1`、`[0]`（非空列表）。

```python
bool(0), bool(""), bool([])       # (False, False, False)
bool(-1), bool("False"), bool([0])  # (True, True, True)
```

由此得到三个地道写法（读代码天天见）：

```python
if results:              # 等价 len(results) > 0："有结果才处理"
if not samples:          # "没有样本"：空列表 → 假 → not 后为真
value = name or "匿名"   # 短路 or：name 非空取 name，空/None 取"匿名"
```

第三个值得展开：`A or B` 在 A 为真时**直接返回 A 本身**（不求 B），A 假时返回 B。所以 `x or 默认值` 是"x 有值用 x，没值用默认"的惯用法。对应地 `A and B`：A 假时直接返回 A。`and`/`or` 返回的不是 True/False 而是**其中一边的原值**——这是 Python 的设计，先记住现象，用途以后会反复见到。

### 1.4 三元表达式：赋值里的 mini-if

```python
label = "pass" if score >= 60 else "fail"

# 求符号
sign = 1 if x >= 0 else -1

# 文件名后缀判断
kind = "数据文件" if fname.endswith(".csv") else "其他"
```

读法："**条件成立取前面，不成立取后面**"。什么时候用：一行写得下的二选一；条件复杂、或需要三选一以上 → 回去写普通 if。

### 1.5 嵌套与拍平

```python
# 能写成平的就不要嵌套（左：嵌套版；右：拍平版）
if x > 0:                      if x <= 0:
    if y > 0:                      quadrant = "x 轴及以下"
        quadrant = "第一象限"  →  elif y > 0:
    else:                          quadrant = "上方"
        quadrant = "第四象限"   else:
                                    quadrant = "下方"
```

**能用 elif 拍平的嵌套就拍平**——每多一层缩进，读者的脑子多压一层栈。嵌套超过两层，通常说明逻辑该重新组织（或拆成函数，第 3 讲）。

### 1.6 陷阱清单

1. **判 None 永远 `x is None` / `x is not None`**：`==` 比较值，`is` 比较是不是同一个对象；None 全宇宙只有一个，按约定用 `is`
2. float 不用 `==`：`abs(a - b) < 1e-12` 容差法（第 1 讲 §2.3，条件里同样适用）
3. `if x = 5:` 是语法错误——条件里不能赋值（Python 替你挡住了 C 里最常见的笔误）
4. 链式比较可以连写：`0 <= x < 1` ✓（数学写法直接搬）

## 2. 循环

### 2.1 为什么需要：重复是计算的本质

对一千万个粒子做同样的事、迭代到收敛、逐行处理文件——**写一行、跑一万次**就是循环存在的意义。手工复制粘贴一万行代码在数学上等价，在实践中是灾难（改一个 bug 要改一万处）。

### 2.2 for-in：遍历一切可迭代

```python
for e in [1.2, 3.4, 0.5]:     # list → 依次取出每个元素
    print(e)

for ch in "spin":              # str → 依次取出每个字符 s/p/i/n
    print(ch)

mass = {"electron": 0.511, "proton": 938.3}
for k in mass:                 # dict → 默认遍历【键】
    print(k, mass[k])
for k, v in mass.items():      # dict → 遍历 (键, 值) 对并解包
    print(k, v)
```

for-in 的心智模型："**容器里有什么，我就对每个做什么**"。不需要自己管下标。

### 2.3 range：数的序列（含头不含尾）

```python
range(1, 31)      # 1, 2, ..., 30   终点取不到——和切片 s[1:31] 同一条规则！
range(0, 10, 2)   # 0, 2, 4, 6, 8   第三个参数是步长
range(5, 0, -1)   # 5, 4, 3, 2, 1   负步长倒着走
range(10)         # 0, 1, ..., 9    起点默认 0
```

两件事：

1. range 是**惰性**的——不真生成一串数，边走边产。`for i in range(10**8)` 不吃内存；想看内容得 `list(range(1, 31))`
2. 什么时候用 range：**只有"要走 n 次"而没有现成容器时**（如打表 1~100）。有容器就直接 `for x in 容器`

### 2.4 两大基本模式（本讲的内功）

**模式一：累加器——许多值合成一个**

```python
total = 0
for e in [1.2, 3.4, 0.5]:
    total += e          # 5.1 —— 出发前清零，循环里逐步累加

# 变体满天飞，骨架一模一样：
count = 0               # 计数（ex8 要用）
p = 1
for f in [2, 3, 4]:
    p *= f              # 24 —— 连乘（阶乘就这样写）
biggest = samples[0]    # 打擂台求最大（ex8 要用）：先立擂主，逐个挑战
for s in [5, -3, 12]:
    if s > biggest:
        biggest = s     # 12
```

**模式二：收集器——从一批里挑出/变换出一批**

```python
above = []                          # 出发前备好空列表
for e in [1.2, 3.4, 0.5]:
    if e > 1.0:
        above.append(e)             # [1.2, 3.4] —— 挑选
in_joules = []
for e in [1.0, 2.5]:                # 变换：eV → J
    in_joules.append(e * 1.602e-19)
```

**你以后写的每个程序，八成是这两个模式的变体。**认出它们，代码就不再是天书而是填空题。

### 2.5 enumerate 与 zip：循环的两个好搭档

```python
# enumerate：又要元素又要下标
for i, name in enumerate(["up", "down", "strange"]):
    print(i, name)                  # 0 up / 1 down / 2 strange
for i, name in enumerate(["a", "b", "c"], start=1):   # 下标从 1 开始（打排名用）
    print(i, name)

# zip：两条等长列表并行走，自动配对
names = ["sample_A", "sample_B"]
temps = [300, 350]
for n, T in zip(names, temps):
    print(n, T)                     # sample_A 300 / sample_B 350
```

两条规则：需要下标用 `enumerate`，**不要写 `for i in range(len(names))`**（能用，但被视为坏味道）；`zip` 长度不齐时**以短的为准**（多的悄悄丢弃）。zip 的完整展开见**附录 A**。

### 2.6 while：不知道要循环多少次时

选择标准一句话：**for 走容器，while 等条件**。

```python
# 例 1：猜数字——"猜中为止"，次数未知
answer, guess = 42, 0
while guess != answer:
    guess = int(input("你的猜测: "))
    if guess < answer:
        print("小了")
    elif guess > answer:
        print("大了")
print("答对")

# 例 2（物理人专属）：牛顿迭代开根号——"收敛为止"，迭代次数未知
a = 2.0
x = 1.0                       # 初值
while abs(x * x - a) > 1e-12: # 停机条件：误差足够小
    x = (x + a / x) / 2       # 牛顿更新公式
print(x)                      # 1.4142135623730951 —— 5 次迭代就收敛
```

例 2 是数值计算的**原型程序**：初值 + 迭代公式 + 停机条件。下个月的 Ising 模拟、以后所有的数值实验，循环骨架都是它。

### 2.7 break / continue / for-else

```python
# break：提前跳出（找到就收工）
primes = [2, 3, 5, 7, 11]
for p in primes:
    if 9 % p == 0:
        print(f"9 的最小素因子是 {p}")
        break                  # 找到即停，后面的白看

# continue：跳过本轮，直接进下一轮（过滤脏数据）
readings = [1.2, -999, 3.4, -999, 0.5]     # -999 是仪器缺测标记
good = []
for r in readings:
    if r == -999:
        continue              # 这个不要，跳过去
    good.append(r)            # [1.2, 3.4, 0.5]

# for-else：循环自然走完（没被 break）才进 else —— "查找失败"分支
for p in primes:
    if 13 % p == 0:
        print(f"13 的因子 {p}")
        break
else:
    print("13 是素数")        # 没有 break → 走到这里
```

for-else 是 Python 特色，初学**见到能认即可**；等价写法（立个 found 标志变量）也完全可以。

### 2.8 嵌套循环：二维数据的标配

```python
m = [[1, 2, 3],
     [4, 5, 6]]

row_sums = []
for row in m:                 # 外层：一行一行走
    s = 0
    for v in row:             # 内层：行里一个一个走
        s += v
    row_sums.append(s)        # [6, 15]

# 找最大值的位置（enumerate 双层版）
best, bi, bj = m[0][0], 0, 0
for i, row in enumerate(m):
    for j, v in enumerate(row):
        if v > best:
            best, bi, bj = v, i, j
print(f"最大值 {best} 在第 {bi} 行第 {bj} 列")   # 6 在第 1 行第 2 列
```

嵌套循环 = **外层慢变量、内层快变量**（像二重积分 ∫∫ 的次序）。二维表、图像、矩阵，全是这个骨架——第 1 讲 §4.6 的嵌套 list 从此活了。

### 2.9 循环陷阱清单

1. **边遍历边增删列表**——元素挪位会漏处理：

   ```python
   nums = [1, 2, 3, 4]
   for x in nums:        # 想删掉所有偶数
       if x % 2 == 0:
           nums.remove(x)
   nums                   # [1, 3, 4] —— 4 漏网！（2 被删后 4 前移，指针跳过了它）
   ```

   正确做法：遍历副本 `for x in nums[:]`，或**先收集后处理**（循环里只 append，循环外统一删）
2. 死循环三件套：忘了 `i += 1`、break 条件永假、`while True` 没出口
3. 同样**不要在遍历 dict 时增删它的键**（直接 RuntimeError），要改就先收集 `to_del = []`，循环后统一删

## 3. dict：键 → 值的映射（本讲主角）

### 3.1 为什么需要：从"翻遍全表"到"直捣黄门"

物理常数表用 list 存会怎样？查质子质量得从头翻到尾，n 条数据平均翻 n/2 次。dict 像纸制字典的**部首索引**：由"键"直接算出值的存放位置（哈希表）——一万条、一亿条都是一步（O(1)）。

```python
mass = {"electron": 0.511, "proton": 938.3, "neutron": 939.6}   # MeV/c²
mass["proton"]        # 938.3   一步取出
mass["muon"] = 105.7  # 增：新键直接赋值
mass["muon"] = 105.66 # 改：同键再赋值 = 覆盖
del mass["muon"]      # 删
"tau" in mass         # False  —— in 查的是【键】不是值
```

**什么时候用 dict**：任何"由 A 查 B"的关系——名字查分数、单词查次数、状态查能量、单位查换算率。真实世界的配置文件、JSON、数据库记录，剥开全是 dict。

### 3.2 四种建法（都见过就不怕）

```python
d1 = {"a": 1, "b": 2}                  # 字面量：手写小表
d2 = dict(zip(names, ages))            # 两条列表配对成 dict（ex4）
d3 = dict(electron=0.511, proton=938.3) # 关键字参数式：键必须是合法标识符
d4 = {w: len(w) for w in words}        # 推导式：批量生成（§5.3）
```

### 3.3 KeyError 与 `.get()`（最高频报错点）

```python
mass.get("tau")           # None      —— 不炸，查不到给 None
mass.get("tau", 0.0)      # 0.0       —— 查不到给指定默认值
mass["tau"]               # ✕ KeyError —— 直接炸
```

选择原则：**确定键存在**用 `[]`（该炸就炸，炸了说明数据或逻辑有问题）；**键可能不存在**用 `.get(键, 默认)`。完整展开见**附录 B**。

### 3.4 计数器范式（全讲最重要的三行）

```python
freq = {}
for w in "quantum mechanics says quantum states evolve under quantum rules".split():
    freq[w] = freq.get(w, 0) + 1
# {'quantum': 3, 'mechanics': 1, 'says': 1, ...}
```

逐帧拆解它为什么对：第一次遇到 quantum，`freq.get("quantum", 0)` 返回默认 0，存 1；第二次遇到，get 返回现有值 1，存 2；……**词频统计、直方图、状态计数、高阳课的统计类作业，全是这三行。**现在合上讲义，在 notebook 里默写一遍。

### 3.5 遍历与解包（tuple 解包的用武之地）

```python
d = {"electron": 0.511, "proton": 938.3}
for k in d:                  # 默认遍历键（等价 d.keys()）
    print(k)
for k, v in d.items():       # (键, 值) 元组成对取出 → 解包成两个名字
    print(f"{k} 的质量是 {v}")
for v in d.values():         # 只遍历值
    print(v)
```

`d.items()` 每次吐出一个 `(键, 值)` 二元组——第 1 讲 §5.3 的解包语法在这里正好接住它。

### 3.6 配套惯用法四件（先照抄，lambda 下讲细讲）

```python
d = {"electron": 0.511, "proton": 938.3, "neutron": 939.6}

max(d, key=d.get)     # 'neutron' —— 值最大的【键】
min(d, key=d.get)     # 'electron'

sorted(d.items(), key=lambda kv: kv[1], reverse=True)
# [('neutron', 939.6), ('proton', 938.3), ('electron', 0.511)]
# 按【值】降序的 (键, 值) 列表 —— top-k 统计的标准姿势（ex3 选做）

v = d.pop("proton")   # 删除并【返回】值（del 只删不返回）—— v = 938.3

d.update({"tau": 1777, "proton": 938.27})   # 批量增改；合并另一个 dict
merged = {**d, "tau": 1776.9}               # ✓ ** 展开旧表 + 直接写新键值（同键覆盖）
merged = {**d, {"tau": 1776.9}}             # ✕ 语法错：** 后面只能跟 dict，不能塞个花括号字面量
```

### 3.7 分组惯用法：把散件装进桶（进阶但常用）

```python
pairs = [("fermion", "electron"), ("boson", "photon"), ("fermion", "muon")]
groups = {}
for kind, name in pairs:
    groups.setdefault(kind, []).append(name)
# {'fermion': ['electron', 'muon'], 'boson': ['photon']}
```

`setdefault(键, [])`：键存在返回现有值，不存在就先存入空列表再返回。于是这行 = "没有这个桶就先造一个，然后往里放"。**按类别归档**（按能级归档粒子、按日期归档事件）都用它，和计数器是姊妹范式：计数器往桶里放数字，分组往桶里放列表。

### 3.8 键必须不可变（为什么）

```python
d = {[1, 2]: "x"}    # ✕ TypeError: unhashable type: 'list'
d = {(1, 2): "x"}    # ✓ tuple 可以 —— 第 1 讲埋的伏笔在此兑现
```

原因：dict 靠"键算出的**指纹**（哈希值）"决定存放位置。list 可变——今天指纹是 3 号抽屉，改完内容指纹变 7 号，存进去的东西就找不回了。所以**字符串、数字、tuple 能当键，list 和 dict 不能**。（真想冻结一个集合当键，有 `frozenset`，见到能认即可。）

### 3.9 有序性与两个小坑

- Python 3.7+ dict 保持**插入顺序**，但请把它当纯"映射"用，要有序就 `sorted()`
- `in` 查键不查值：`938.3 in mass` 是 False；要查值得 `938.3 in mass.values()`

## 4. set：去重与集合运算

### 4.1 为什么需要 set：三个场景

```python
# 场景 1：去重（一行）
tags = ["sc", "ai", "qi", "sc", "ai"]
uniq = set(tags)              # {'sc', 'ai', 'qi'}

# 场景 2：极速成员判断 —— 与 dict 同为哈希表，in 是 O(1)
"qi" in uniq                  # True；list 的 in 是 O(n)，百万级数据差一万倍

# 场景 3：集合运算（下节）
```

什么时候用：**需要"有没有"而不是"是第几个"** 时。去重、黑名单白名单、visited 标记（以后写 BFS 的 visited 集合就是它）。

### 4.2 集合运算：两份名单的所有关系

```python
phys = {"Alice", "Bob", "Carol", "Eve"}
ai   = {"Bob", "Carol", "Dave", "Frank"}

phys & ai   # {'Bob', 'Carol'}                交集：都选
phys | ai   # 8 人全集                          并集：至少选一门
phys - ai   # {'Alice', 'Eve'}                 差集：只选物理
phys ^ ai   # {'Alice','Eve','Dave','Frank'}   对称差：恰好选一门
phys <= ai  # False                            子集判断
```

记号就是数学课的 ∩ ∪ − ：`& | - ^`。**用的时候不需要记"谁的补集"**——`phys ^ ai` 与 `ai ^ phys` 结果相同。

### 4.3 增删与两个易错点

```python
s = {"a", "b"}
s.add("c")         # 增
s.remove("z")      # ✕ 不存在 → KeyError
s.discard("z")     # ✓ 不存在也安静通过（查不到就算了）
```

三个坑：

1. **`{}` 是空 dict！** 空 set 必须写 `set()`
2. set 无序无下标：`uniq[0]` ✕；要有序输出 `sorted(uniq)`
3. 保序去重的正确姿势是 `dict.fromkeys`：`list(dict.fromkeys(tags))` → `['sc', 'ai', 'qi']`（set 去重会打乱顺序，dict 记住插入顺序）

### 4.4 seen 惯用法：边走边记（BFS 预告）

```python
data = [1, 3, 1, 2, 3]
seen, out = set(), []
for x in data:
    if x not in seen:      # 没见过才处理
        seen.add(x)        # 记下来：见过了
        out.append(x)
out                        # [1, 3, 2] —— 保序去重的手写版
```

"**处理前先查 seen、处理后登记**"——以后图搜索、避免重复访问，全是这个骨架的变体。今天先混个脸熟。

## 5. 推导式：收集器的压缩写法

### 5.1 从四行到一行（为什么值得学）

```python
energies = [1.2, 3.4, 0.5, 2.2]

above = []
for e in energies:              # §2.4 的收集器……
    if e > 1.0:
        above.append(e)

above = [e for e in energies if e > 1.0]   # ……压成一行，[1.2, 3.4, 2.2]
```

读法从 for 开始向两边："**对 energies 里的每个 e，若 e > 1.0，收下 e**"。左边是"收什么"（变换），右边是"从哪收"（来源+筛选）。读代码的 Python 程序员十个里十个用推导式——不认识它就读不懂别人的代码。

### 5.2 两种 if 的位置（本讲最易混点，必考）

```python
[x**2 for x in nums if x > 0]            # 【筛选】if 在尾部 —— 挑人，不要 else
[x**2 if x > 0 else 0 for x in nums]     # 【映射】if-else 在前 —— 改造每个人，必须 else
```

口诀：**尾 if 是"挑人"，前 if-else 是"改造每个人"**。映射版的经典应用——把值**截断**（clamp）在物理合理区间：

```python
xs = [0.3, 1.7, -0.2, 0.9]                        # 归一化溢出的透过率
[x if 0 <= x <= 1 else (0 if x < 0 else 1) for x in xs]
# [0.3, 1.0, 0.0, 0.9] —— 超界全部截回 [0,1]
```

筛选条件可以连写两个 if（等于 and）：

```python
[n for n in range(1, 101) if n % 7 == 0 if '7' not in str(n)]   # 7 的倍数且不含 7
```

### 5.3 家族全家福：list / dict / set 推导

```python
words = ["electron", "muon", "tau"]

[w.upper() for w in words]              # ['ELECTRON', 'MUON', 'TAU']      list：变换
{w: len(w) for w in words}              # {'electron': 8, 'muon': 4, ...}  dict：配对
{x % 3 for x in range(10)}              # {0, 1, 2}                        set：取全部不同余数
```

### 5.4 双 for 与嵌套

```python
[m + n for m in "ab" for n in "12"]     # ['a1', 'a2', 'b1', 'b2']
# 双 for 从左到右嵌套 = 外层 m、内层 n（和 §2.8 嵌套循环同序）

nested = [[1, 2], [3, 4]]
[v for row in nested for v in row]      # [1, 2, 3, 4] —— 展平一层

m = [[1, 2, 3], [4, 5, 6]]
[[row[j] for row in m] for j in range(3)]   # [[1, 4], [2, 5], [3, 6]] —— 转置！
# 内层推导是"取每一行的第 j 列"，外层让 j 走 0..2
```

转置这个例子建议亲手跑 + 手指头比划一遍——它是"推导式里套推导式"的合法上限。

### 5.5 生成器表达式：不要列表时要省着用

```python
sum(e**2 for e in energies)          # 只要求和，中间列表纯属浪费 —— 去掉 [] 边产边算
max(abs(x) for x in residuals)       # 残差最大模
any(x > 1.0 for x in energies)       # 有没有超阈值的？True/False
all(x > 0 for x in energies)         # 是不是全为正？
```

`any` / `all` + 生成器 = "**存在**/任意"两个数学问句的代码化，比手写循环+break 优雅得多，值得立刻收编。

### 5.6 可读性红线

推导式超过两个 for、或你自己十秒内读不懂 → **回去写普通循环**。它是给简单变换省纸的，不是炫技场；列表要分步构造时，普通收集器循环永远是对的。

## 6. 组合拳：今天内容的两个完整小程序

**程序 1：词频 top-k**（dict 计数 + 排序，数据处理的入门全流程）

```python
text = "quantum mechanics says quantum states evolve under quantum rules"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
for w, c in sorted(freq.items(), key=lambda kv: -kv[1])[:3]:
    print(f"{w}: {c}")
# quantum: 3 / mechanics: 1 / says: 1
```

**程序 2：数据清洗**（continue 跳脏值 + 收集器 + any/all 验收）

```python
readings = [1.2, -999, 3.4, -999, 0.5, -999]
good = []
for r in readings:
    if r == -999:          # 缺测标记：跳过
        continue
    good.append(r)
print(len(good), sum(good) / len(good))     # 4 个有效值与均值 1.625
print(any(r < 0 for r in good))             # False —— 有效数据里没有负值，验收通过
```

两个程序都不超过十行——**所谓编程能力，一大半就是把这几讲的基本件组合流畅**。

## 7. 概念总结表

| 工具 | 一句话 | 高频陷阱 |
|---|---|---|
| if / elif / else | 分支；缩进即块；elif 链上往下短路 | 判 None 用 `is None`；float 用容差 |
| for-in | 对容器每个元素做一件事 | 要下标用 enumerate，别 `range(len())` |
| while | 条件成立就一直做（走容器别用它） | 先想好出口；`i += 1` 别忘 |
| dict | 键→值映射，O(1) 直查 | KeyError→`.get`；键必须不可变 |
| set | 去重 + 交并差 + O(1) 成员判断 | `{}` 是空 dict；无下标 |
| 推导式 | 收集器的压缩写法 | 尾 if 筛选、前 if-else 映射，别混 |

## 8. 练习 ex1~ex8

1. **FizzBuzz**：打印 1~30，3 的倍数打 `Fizz`、5 的倍数打 `Buzz`、都是倍数打 `FizzBuzz`、否则打数字，每行一个（提示：先判 15，想想为什么）
2. `nums = [12, 5, 8, 131, 44, 3, 27, 15]`：先用 for + if 收集出**偶数列表**和**大于 10 的奇数列表**；再用两条**推导式**重写，核对与循环版一致
3. **词频统计**：统计 `"quantum mechanics says quantum states evolve under quantum rules"` 每个单词出现次数存入 dict；输出出现最多的单词和次数（提示：`max(d, key=d.get)`）。选做：用 `sorted(d.items(), key=lambda kv: -kv[1])[:3]` 输出前三名
4. `names = ["Alice", "Bob", "Carol", "Dave"]`，`ages = [19, 21, 20, 21]`：用 `zip` 合成 {姓名: 年龄}；输出年龄最大的人名（思考：并列时 `max` 返回谁？）
5. 两个名单 `phys = ["Alice", "Bob", "Carol", "Eve"]`，`ai = ["Bob", "Carol", "Dave", "Frank"]`：用 set 求**两门都选**的人和**恰好选一门**的人，`sorted()` 后输出
6. 一条**推导式**：找出 1~100 中 7 的倍数**或**数字里含 7 的数（提示：`'7' in str(n)`）；输出总数和前 10 个
7. `ws = ["electron", "muon", "tau", "photon"]`：dict 推导生成 {单词: 长度}；再反转成 {长度: 单词}。**思考题**：如果两个单词长度相同，反转时会发生什么？
8. **读数统计器**：程序反复让用户输入整数，直到输入 `0` 停止；`0` 只是结束信号，**不算数据**。结束后输出：有效数字数、总和、最大值。示例运行（冒号后为用户输入）：
   ```
   输入整数（0 结束）: 5
   输入整数（0 结束）: -3
   输入整数（0 结束）: 12
   输入整数（0 结束）: 0
   共读入 3 个数，总和 14，最大值 12
   ```
   要点：循环次数事先未知 → 用 while（`0` 称为**哨兵值**——约定的结束暗号）；最大值用**打擂台**骨架（§2.4），擂主初值用 `None` 而非 `0`（想想输入全是负数时会怎样）；三个统计量**边读边更新**。自测边界：`5 -3 12 0` / `-5 -3 -8 0`（全负）/ 直接 `0`（无数据）

存 `practice/drills/python-02/exN.py`（ex8 也可是 notebook），**做完贴回会话批改**。

## 附录 A：zip 深入（2026-09-12 追问展开）

**本质**：zip 把多条序列"按位置配对"——像拉链，几排齿逐个咬合，每个咬合点产出一个 tuple。

```
names = ["Alice", "Bob", "Carol"]     第 1 排齿
ages  = [   19,     21,     20   ]    第 2 排齿
             ↓ zip 拉上
       ("Alice",19) ("Bob",21) ("Carol",20)
```

**四个关键性质**（示例全部实测）：

1. 惰性：`zip(a, b)` 本身不是列表，是"边走边产"的迭代器——看内容要 `list(zip(a,b))`
2. **只能消费一次**：`z = zip(a,b); list(z)` 拿到内容后，`list(z)` 再来一次得 `[]`！要反复用就先 `pairs = list(zip(a,b))` 存下来
3. 长度不齐**以最短为准**（多的悄悄丢弃）；`zip(a, b, strict=True)` 不齐直接 ValueError（防错好习惯）
4. 可以同时咬 2~n 条序列，也可单条：`list(zip([1,2,3]))` → `[(1,), (2,), (3,)]`

**核心用法谱**：

```python
list(zip(names, ages))                       # 配对列表
for n, a in zip(names, ages): ...            # 并行遍历（配 tuple 解包）
dict(zip(names, ages))                       # 两条列表 → dict（ex4）
sum(x*y for x, y in zip(a, b))               # 点积：数学的逐分量配对
[(p2-p1)/(t2-t1) for t1,t2,p1,p2 in zip(ts, ts[1:], ps, ps[1:])]   # 逐段差商
zip(*pairs)                                  # 逆操作：配好的对拆回两条（* 是解包）
[list(col) for col in zip(*m)]               # 矩阵转置
list(zip(range(len(xs)), xs)) == list(enumerate(xs))   # enumerate 的本质
```

**什么时候用**：数据"天然成对/成组且等长"（样品-温度、时间-位置、键列表-值列表）就想到 zip；要下标配元素用 enumerate（= zip(range(len), xs)）。**什么时候别用**：长度本就不齐还指望它替你凑——它只会静默截断，用 strict=True 让它报错。

## 附录 B：dict.get 深入（2026-09-12 追问展开）

**本质**：`.get(键, 默认值)` 是**不炸版查表**——键在返回值，不在返回默认值（默认值省略时返回 None），且**绝不写入**。

三种查询的层级：

| 写法 | 键存在 | 键不存在 | 语义 |
|---|---|---|---|
| `d[k]` | 值 | **KeyError** | 断言式："我确信它存在，不在就是 bug，炸给我看" |
| `d.get(k)` | 值 | None | 试探式："可能没有" |
| `d.get(k, 默认)` | 值 | 默认 | 缺省式："没有就当它是默认值" |

**核心事实（全部实测）**：

1. 等价展开：`d.get(k, v)` ≡ `d[k] if k in d else v`
2. **只读**：查完 dict 不变（想要"没有就写入"用 `setdefault`，见 §3.7）
3. **None 歧义**：`d = {"h": None}` 时 `d.get("h")` 与 `d.get("zzz")` 都是 None，分不清"存在但值为 None"和"不存在"——要区分用 `k in d`
4. **默认值总被求值**：`d.get(k, 贵重计算())` 即使 k 存在，`贵重计算()` 也会执行——默认值保持便宜
5. 链式安全取值：`cfg.get("model", {}).get("layers", 8)`——上一层缺失给空 dict，下一层继续 get，一层都不炸

**高频场景**：计数器 `freq.get(w, 0) + 1`（§3.4）｜配置缺省 `config.get("lr", 1e-3)`（以后训练脚本标配）｜查表补录 `conv.get(unit)` 返回 None 后走明确分支｜环境变量 `os.environ.get("X", "fallback")`。

**原则**：该炸的地方用 `[]`（让 bug 当场现形），不确定的地方才用 `.get`——滥用 `.get` 会让 None 一路传下去，在离事故现场很远的地方炸出 `AttributeError`，更难查。

## 下一讲预告

**函数**（廖雪峰第 6 章）：def、返回值、默认参数、作用域、lambda——把这两讲的代码打包成可复用的工具；随后走向 IO 与异常（第 12/13 章）。说"**继续**"开课。
