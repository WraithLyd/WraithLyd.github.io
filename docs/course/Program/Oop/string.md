## 动态分配内存
new & delete
```cpp linenums="1"
new int;
```

#### const
`const` is equal to `#define` in C. 
It declares a variable to have a constant value. And it can't change in program.
```cpp linenums="1"
const int x = 4;
x = 13;		# illegal!
```

A linenums="1" const in C++ defaults to internal linkage.
- the compiler tries to avoiding creating storage for a const.
    - hold the value in its sample table
- unless you make an explicit extern declaration.
```cpp linenums="1"
extern const int buf = 4;
```
