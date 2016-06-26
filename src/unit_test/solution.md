# 单元测试

### 【解决思路】

1. 首先，你要定义一个待测试的类，实现几个简单的、待测试的方法。

2. 然后你要定义一个专门用于测试的类，继承自`unittest.TestCase`类。编写一些以test开头的方法，这样单元测试模块会在进行测试时自动调用这些方法。

3. 在这些方法中，你需要加入一些断言，即假设程序运行结果和你预想的一致。

4. 最后，调用`unittest.main()`方法，自动进行测试，而不要自己手动调用各个方法。系统进行单元测试时，屏幕上会打印一些信息，以供调试使用。当然，最后输出一个“OK”，就代表测试成功啦！

5. 要注意一下测试覆盖率的问题，即要尽可能将原程序代码中各个函数都测试到。并且尽可能编写一些“刁钻”的测试用例，来提升你程序的鲁棒性。

6. 最后一个建议：每次编程时，先写测试，后写代码。

   ​
