# 打包为可执行文件

### 【解决思路】

曾经非常流行的一个Python打包程序叫py2exe，但是看名字你也猜得出来，它只能将Python程序打包为Windows下的exe文件，跨平台性很差。此外，它对Python3的支持不太友好，需要安装不同的版本以支持Python2/3。所以强烈建议你使用另一款打包工具：[PyInstaller](https://pypi.python.org/pypi/PyInstaller/3.2)

PyInstaller在各个平台下支持性都还不错，并且同时支持Py2/3，还支持很多第三方库。当然，支持程度并不是非常完美，你要做好心理准备。不过对于常见的小型应用是足够用了。

它的基本语法很简单：

```
pyinstaller -F your_python_file.py
```

`-F`表示生成单文件，还有很多选项供你选择。你试着生成一些程序，并比较一下执行速度，你认为这种方式生成的可执行文件，速度会有提升么？

***注意，如果你的Python安装目录中有空格的话，可能会遇到“failed to create process”的问题，可以参考[这篇解答](http://stackoverflow.com/questions/31808180/installing-pyinstaller-via-pip-leads-to-failed-to-create-process)。***

在绝大多数情况下，建议你不要以可执行文件的方式发布程序，一是兼容性可能存在问题，尤其是依赖大量第三方库的程序。另外由于把“Runtime”信息都打包进了可执行文件中，因此生成的文件要远大于以源码形式发布的程序。



