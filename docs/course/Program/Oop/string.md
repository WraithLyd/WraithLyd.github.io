## 动态分配内存
new & delete
```cpp
new int;
```

#### const
`const` is equal to `#define` in C. 
It declares a variable to have a constant value. And it can't change in program.
```cpp
const int x = 4;
x = 13;		# illegal!
```

A const in C++ defaults to internal linkage.
- the compiler tries to avoiding creating storage for a const.
    - hold the value in its sample table
- unless you make an explicit extern declaration.
```cpp
extern const int buf = 4;
```
