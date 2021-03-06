# 生成二维码

### 【解决思路】

1. 在Python中，推荐使用[qrcode](https://pypi.python.org/pypi/qrcode/5.3)这个包来生成二维码，注意到生成二维码和图像有关，因此还需要Python图像处理的“事实标准库”——PIL，所以首先我们使用pip安装它们。

2. 参照官方的样例，我们可以很轻易地用一行代码生成一个二维码：

   `img = qrcode.make('Some data here')`

3. 对于比较复杂的任务，譬如要求纠错率、二维码的尺寸等等，其实也很简单，只要修改相应参数即可。

4. 有关二维码的原理，推荐[这篇文章](http://coolshell.cn/articles/10590.html)

5. 类比之前“验证码识别”那一题，你或许应该可以想到，可以使用在线的API来帮助我们实现我们想要的功能。有关在线生成二维码的接口有很多，你可以自己去探索。

   ​

