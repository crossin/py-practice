# 图像处理

### 【解决思路】

1. 很遗憾的是，Python标准库里并没有可以直接处理图像的库（不过也也是Python比Matlab之类的大锅烩更简洁优雅的原因）。所以我们需要先安装第三方库。
2. Python图像处理的事实标准是`PIL(Python Imaging Library)`，Pythoners基本上都是在用它进行图像处理。
3. 首先是要安装这个库。注意，这个库在Python2/3 下是不同的，准确来说，PIL是不支持Python3的，但是Python3下有一个完全相同的实现`Pillow`，它们的api几乎完全相同，所以这并不是大问题。只是使用不同Python版本的同学记得安装不同的库就好。
4. 然后你应该先了解[基本用法](https://pillow.readthedocs.io/en/3.2.x/handbook/tutorial.html)，当你了解最基本的用法示例后，下面你就可以开始动手做你想做的事情了。如果遇到不懂的地方，及时搜索[文档](https://pillow.readthedocs.io/en/3.2.x/)，PIL的文档是非常详细的，并且都配有示例代码，对新手很友好
5. 本次实验要求的三个功能，对应着`convert()`, `resize()`, `rotate()` 三个函数，具体怎么用，参加示例代码，或看官方文档吧！

