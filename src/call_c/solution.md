# 调用C语言函数

### 【解决思路】

1. 首先，需要编写一个 C 语言函数，然后将其编译为链接库，供Python加载使用。

   代码里实现的是一个对给定的数取 n 次模运算（因为模运算比较慢）的函数。

   ```C
   void modntimes(int c, int n) {
       for (int i = 0; i < n; i++) {
           i % c;
       }
   }
   ```

   然后输入编译指令（以GCC为例）：

   ```
   gcc -fPIC -shared mod.c -o mod.o
   ```

    如此便得到了`mod.o`这个库。

2. 然后我们要Python里加载这个库，并调用这个函数。

   Python标准库已经为我们提供了相关的功能，请参见文档或样例代码：[ctypes](https://docs.python.org/3.5/library/ctypes.html)

3. 接下来就是比较性能差异了，先用Python实现相同的功能的函数（这很容易，不是么？）

   然后分别执行，并记录两者运行时间。

   （友情提示：可以使用`timeit`模块来计时。但更建议使用之前学过的装饰器来“优雅地”计算程序运行时间）

