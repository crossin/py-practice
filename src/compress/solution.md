# 文件压缩/解压

### 【解决思路】

1. 首先了解常见的文件压缩格式：

   1. tar/gzip：这两者往往合起来使用，前者只能打包，后者只能单文件压缩。linux下常用。
   2. rar：windows下常用（winrar也是windows平台下盗版率仅次于office的存在），但是由于这种压缩算法是有版权约束的，因此实际使用得较少，因为还要安装额外的库。
   3. zip：算是比较折衷的选择，跨平台性较好，windows和linux都提供比较原生的支持，Python标准库里也支持此算法。并且可以多文件压缩，相对比较方便些。
   4. 还有其他的压缩格式，就不一一介绍了。



2. 此次我们选择zip格式做演示，其实原理都是相同的，有兴趣的话可以尝试一下（可能需要安装额外的库）

3. 压缩文件夹比压缩一个文件复杂的地方在于要多一个目录遍历的操作，目录遍历操作在之前`随机选片`一节特意讲过，可以去复习复习。

   ​
