# Prolog 笔记

!!! abstract "一分钟版本"
    Prolog 用「事实 + 规则」描述**关系**，用「查询」求解。你不写步骤，只写**什么成立**；怎么搜、怎么回溯，交给引擎。

## 0. 先跑起来

```bash
# Windows：官方 Installer，或 scoop install swi-prolog
# macOS：brew install swi-prolog
swipl --version
swipl
```

进入交互环境（`?-` 是提示符）：

```prolog
?- X is 2 + 3.
X = 5.

?- [family].              % 加载 family.pl（不用写引号和扩展名）
true.

?- make.                 % 改过文件后重新加载
?- listing(parent).       % 看看已加载的子句
?- halt.                  % 退出
```

也可以直接从命令行脚本化运行：

```bash
swipl -s family.pl -g "ancestor(tom, X), writeln(X)" -t halt
```

## 1. 三个基本概念

!!! tip "事实 / 规则 / 查询"
    - **事实** `parent(tom, bob).` —— 「tom 是 bob 的父亲」成立
    - **规则** `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` —— 「X 是 Z 的祖父，**如果**存在 Y……」
    - **查询** `?- grandparent(tom, Who).` —— 让引擎去证明，并把 `Who` 补上

一次「执行」就是：给出目标 → 尝试统合 → 遇分支记下回溯点 → 失败就退回去试下一个。

## 2. 词法：原子、变量、复合项、表

| 形式 | 例子 | 说明 |
|---|---|---|
| 原子 atom | `tom` `[]` `'+'` | 小写开头；要保留大小写/空格就加单引号 |
| 变量 | `X` `Who` `_` `_Tmp` | 大写或 `_` 开头；`_` 每次出现都是**新**变量 |
| 整数 / 浮点 | `42` `-3` `2.5` | 整数和浮点**不统合** |
| 复合项 | `point(1, 2)` `parent(tom, bob)` | 仿函数 functor + 参数个数（arity） |
| 表 list | `[]` `[a, b]` | 由头和尾组成（见下面那段） |

表的「头 + 尾」写法是 `[H|T]`：`H` 绑到第一个元素，`T` 绑到剩下的表。所以 `[a, b]` 其实就是 `'.'(a, '.'(b, []))` 的语法糖。

!!! warning "字符串在 SWI 里是「字符码表」"
    默认 `"abc"` 等于 `[0'a, 0'b, 0'c]`（整数表）。写解析器时通常想要字符表：

    ```prolog
    :- set_prolog_flag(double_quotes, chars).
    ```

    之后 `"abc"` 才是 `[a, b, c]`。这条 flag 建议写在文件开头。

注释用 `%`（单行）和 `/* ... */`（多行）。

## 3. 标点各是什么意思

| 符号 | 含义 |
|---|---|
| `.` | 子句结束（少了它就报错，最常见的手误） |
| `,` | 「与」——子目标从左到右依次证明 |
| `;` | 「或」——或者「再要一个解」（回溯） |
| `:-` | 「如果」——规则头 `:-` 规则体 |
| `\+` | 否定（否定即失败） |
| `!` | 切割（丢弃选择点） |

```prolog
% X 的父辈的兄弟，就是 X 的叔叔
uncle(X, Y) :- parent(P, X), sibling(P, Y), male(Y), X \= Y.
```

## 4. 统合：Prolog 唯一的「赋值」

`=/2` 不是赋值，而是**统合**：找让两边相同的**最一般替代**。变量一旦绑上，就可以顺藤摸瓜地绑定到别处。

```prolog
?- f(X, b) = f(a, Y).
X = a, Y = b.

?- [H|T] = [1, 2, 3].
H = 1, T = [2, 3].

?- X = Y, Y = 3.
X = Y, Y = 3.        % 两者指向同一个变量，最终都是 3

?- 1 = 1.0.
false.                  % 整数与浮点不统合

?- X = 1, X = 2.
false.                  % 已经绑成 1，不能再变
```

!!! danger "`\=` 不是「数值不等」"
    `X \= Y` 的含义是「**无法统合**」。

    - `1 \= 2` 成立
    - 但 `X \= 2` 在 `X` 未绑定时**失败**（因为 `X = 2` 可统合）

    比较数值请用 `=\=`；比较两项是否是同一个用 `==`。

## 5. 回溯：一个查询可以有很多解

```prolog
parent(tom, bob).
parent(bob, ann).
parent(bob, pat).

?- parent(bob, C).
C = ann ;
C = pat ;
false.
```

`;` 是「再来一个」，也就是**回溯**到上一个选择点重试。想要一次收齐就用 `findall/3`：

```prolog
?- findall(C, parent(bob, C), Cs).
Cs = [ann, pat].
```

## 6. 算术：只有 `is` 会求值

```prolog
?- X is 2 + 3 * 4.
X = 14.

?- 2 + 3 =:= 5.
true.

?- 2 =:= 2.0.
true.

?- 2 == 2.0.
false.
```

运算符：`+ - * / // mod rem **`；比较：`=:=` `=\=` `<` `>` `=<` `>=`（注意是 `=<`，不是 `<=`）。

!!! danger "三个经典坑"
    1. `X is X + 1` —— 永远失败：右边有未绑定的 `X`，`is` 不猜。
    2. `1 + 2 = 1 + 2` —— **成立**，但只是统合了两个复合项，没有算。
    3. 用 `=` 代替 `is`：`X = 2 + 3` 得到的是项 `2+3`，不是 `5`。

## 7. 表：Prolog 的主场

```prolog
% append/3：把前两个表接起来得到第三个
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

% member/2：某项在表里
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% 求和
sum_list([], 0).
sum_list([H|T], S) :- sum_list(T, S0), S is H + S0.
```

`append/3` 是**多方向的**：能合并、能拆分，甚至能枚举「一个表的所有拆法」——

```prolog
?- append(X, Y, [1, 2, 3]).
X = [], Y = [1, 2, 3] ;
X = [1], Y = [2, 3] ;
X = [1, 2], Y = [3] ;
X = [1, 2, 3], Y = [].
```

!!! tip "写递归谓词的三段式"
    1. **基准**：`p([], ...)` 直接给答案，不再递归
    2. **递归**：`p([H|T], ...) :- ..., p(T, ...)`
    3. **参数方向**：先想清楚哪个参数「进」、哪个「出」；同一谓词往往能多方向用（`length/2` 就是典型）

## 8. 尾递归与累加器

```prolog
% 非尾递归：递归回来之后还要做 is
sum_list([H|T], S) :- sum_list(T, S0), S is H + S0.

% 尾递归：把中间结果一路往下传
sum_acc([], Acc, Acc).
sum_acc([H|T], Acc, S) :- Acc1 is Acc + H, sum_acc(T, Acc1, S).
sum_list(L, S) :- sum_acc(L, 0, S).
```

SWI 会做 last-call optimization（LCO），但**前提**是递归调用是最后一个目标、且不留选择点。十万级的表，请用累加器写法，否则容易堆栈爆炸。

## 9. 切割 `!`：到此为止，别再回溯

```prolog
max(A, B, A) :- A >= B, !.
max(_, B, B).
```

`!` 会**丢弃「当前位置到调用点之间」的选择点**。常见三种用法：

1. 表示子句互斥（写成 if-else 链）
2. 已经确定答案，提前成功
3. 阻止回溯进入不该再试的分支

!!! danger "切割是「不纯」的"
    它让谓词的可回溯行为依赖调用顺序，也会让「本该失败」的测试留下变量绑定。经验法则：**只在「子句互斥」和「确定的 if-else」里用**，别拿它当性能开关。

想要表达 if-then-else，`->` 通常比手写切割干净：

```prolog
sign(X, S) :-
    ( X > 0 -> S = positive
    ; X < 0 -> S = negative
    ;           S = zero
    ).
```

## 10. 否定：`\+`

```prolog
?- \+ parent(tom, bob).
false.

?- \+ man(X).
false.          % 因为 man(某个东西) 可证
```

`\+ Goal` = 「`Goal` **不可证**」（closed-world 假设）。它**不产生绑定**，只是失败即否定。

!!! warning "`\+` 用在未绑定变量上会反直觉"
    `\+ X = 2` 在 `X` 未绑定时**失败**，因为 `X = 2` 是可证的。所以：

    - 判断「两个项不同」用 `\=` 或 `==`，不要用 `\+ =`
    - `\+` 里的目标，变量最好已经绑定（比如先 `parent(P, X)` 再 `\+ X = Y`）

## 11. 收齐所有解：`findall` / `bagof` / `setof`

```prolog
?- findall(C, parent(bob, C), Cs).        % Cs = [ann, pat]
?- bagof(C, parent(P, C), Cs).             % 按 P 分组，逐个 P 给解
?- setof(C, parent(P, C), Cs).             % 分组 + 去重 + 排序
?- findall(Y, (member(X, [1,2,3]), Y is X*X), Ys).
```

`bagof` / `setof` 会把**自由变量**当分组键；用 `^` 显式说「它不参与分组」：

```prolog
?- setof(C, P^parent(P, C), Cs).   % 所有子女，去重排序
```

需要计数、求和这类汇总，`library(aggregate)` 更顺手：

```prolog
?- aggregate_all(count, parent(_, _), N).
?- aggregate_all(sum(Age), person(_, Age), Total).
```

## 12. 常用内置与高阶谓词

| 谓词 | 作用 |
|---|---|
| `length/2` | 表长（也能反过来「生成指定长度的表」） |
| `nth0/3` `nth1/3` | 按下标取元素（从 0 / 1 开始） |
| `reverse/2` `msort/2` `sort/2` | 反转、按标准序排序、去重排序 |
| `between/3` `numlist/3` | 整数枚举 |
| `maplist/2..` | 逐元素应用 |
| `foldl/4` | 折叠（带累加器） |
| `include/3` `exclude/3` | 按谓词过滤 |
| `atom_string/2` `atom_number/2` `number_string/3` | 类型转换 |
| `format/2` `writeln/1` | 输出 |
| `read/1` | 读入一个项 |

```prolog
even(X) :- 0 is X mod 2.

?- maplist(atom_length, [ab, abc, a], Ls).
Ls = [2, 3, 1].

?- numlist(1, 5, Ns), include(even, Ns, Evens).
Evens = [2, 4].
```

## 13. 输出与格式化

```prolog
?- format("~w + ~w = ~w~n", [2, 3, 5]).
2 + 3 = 5
```

| 格式 | 说明 |
|---|---|
| `~w` | 项，`write` 风格（不加引号） |
| `~q` | 项，`writeq` 风格（**加引号**，调试首选） |
| `~a` | 原子 / 字符串内容 |
| `~d` `~f` `~e` | 整数 / 浮点 / 科学计数 |
| `~n` | 换行 |

## 14. 动态子句：当状态用

```prolog
:- dynamic counter/1.
counter(0).

inc :-
    retract(counter(N)),
    N1 is N + 1,
    assertz(counter(N1)).
```

| 谓词 | 作用 |
|---|---|
| `asserta/1` / `assertz/1` | 加到最前 / 最后 |
| `retract/1` | 删掉一条 |
| `retractall/1` | 删掉全部匹配的 |
| `abolish/1` | 删掉整个谓词的定义 |

它破坏了逻辑纯粹性（同一查询结果可能影响后续查询），但做计数器、缓存、简单状态机很方便。

## 15. DCG：用文法写解析器

```prolog
:- set_prolog_flag(double_quotes, chars).

sentence --> noun_phrase, verb_phrase.
noun_phrase --> det, noun.
verb_phrase --> verb, noun_phrase.
verb_phrase --> verb.

det --> [the] ; [a].
noun --> [cat] ; [dog].
verb --> [chased] ; [saw].
```

```prolog
?- phrase(sentence, "the cat chased the dog").
true.

?- phrase(sentence, "the cat chased").
true.

?- phrase(sentence, "cat the").
false.
```

`{...}` 里可以插普通目标，参数和可选成分也能直接写成规则：

```prolog
digits([D|T]) --> digit(D), digits(T).
digits([])     --> [].

digit(D) --> [D], { between(0, 9, D) }.
```

`library(dcg/basics)` 里已经有 `integer//1`、`number//1`、`blank//0`、`nonblanks//1` 这些常用零件，写小语言时省很多事。

## 16. 调试

```prolog
?- trace.            % 单步：creep / skip / redo / fail / exit
?- spy(parent/2).    % 只观察这个谓词
?- nospy(parent/2).
?- gtrace.           % 图形化调试器（需要 GUI 环境）
```

调试口诀：
1. **该成立的失败了** → 用 `trace` / `spy` 看是哪一步统合不上；把子目标单独拎出来查
2. **该失败的多给了答案** → 多半是切割位置不对，或 `\+` 用在了未绑定变量上

## 17. 常见坑清单

| 现象 | 常见原因 |
|---|---|
| 查询一直 `false.` | 少了句号；`double_quotes` 没设；`is` 右边有未绑定变量 |
| 解的顺序很怪 | 子句顺序 + 从左到右深度优先；没有切割就会继续回溯 |
| 同一个解给两次 | 递归没收缩（如 `ancestor(X, X)`）；子句互相重叠 |
| `\+` 结果反直觉 | 目标里的变量未绑定 |
| 大表爆栈 | 没写累加器/尾递归；选择点太多 |
| 单例变量警告 | 某个变量只出现一次（多半是拼写错误），真不用就写 `_` |

## 18. 两个完整例子

!!! example "家谱：递归关系"
    ```prolog
    male(tom).   male(bob).   male(pat).
    female(ann). female(liz).

    parent(tom, bob). parent(tom, liz).
    parent(bob, ann). parent(bob, pat).

    father(X, Y) :- parent(X, Y), male(X).
    mother(X, Y) :- parent(X, Y), female(X).
    sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
    grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

    ancestor(X, Y) :- parent(X, Y).
    ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).
    ```

    ```prolog
    ?- findall(Y, ancestor(tom, Y), L).
    L = [bob, ann, pat, liz].
    ```

!!! example "图上找路：带访问表，避免绕圈"
    ```prolog
    edge(a, b). edge(b, c). edge(c, d). edge(a, d).

    path(X, Y, Path) :- path(X, Y, [X], Path).
    path(X, Y, Seen, [Y|Seen]) :-
        edge(X, Y), \+ member(Y, Seen).
    path(X, Y, Seen, Path) :-
        edge(X, Z), \+ member(Z, Seen),
        path(Z, Y, [Z|Seen], Path).
    ```

    ```prolog
    ?- findall(P, path(a, d, P), Ps).
    Ps = [[d, a], [d, c, b, a]].
    ```

    这是**深度优先**的路径枚举；要最短路径，用 `library(heaps)`（Dijkstra）或对每个解取 `length/2` 比较。

## 19. 练习

1. 自己实现 `last/2`（取表最后一个元素），不用内置。
2. 用累加器实现 `reverse/2`，和内置版本比较长表的表现。
3. 实现 `max_list/2`：空表要**失败**，而不是抛异常。
4. 实现 `count/3`（某元素出现次数），分别用递归和 `foldl/4` 写一遍。
5. 用 `between/3` + `findall/3` 求 1..100 中同时被 3 和 7 整除的数。
6. 用 DCG 写「算术表达式 → AST」：支持 `+ - * /` 与括号，注意左结合。
7. 用 `setof/3` 求「每个父亲有多少个孩子」。
8. 写 `different/2`：两项不同，并处理好「变量未绑定」的情况（提示：`==` 与 `\=`）。

!!! quote ""
    写完记得 `halt.`；想脚本化就 `swipl -s file.pl -g "goal" -t halt`。
