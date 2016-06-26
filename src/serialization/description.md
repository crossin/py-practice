# 序列化
### 【问题描述】

在程序运行过程中，我们经常需要将数据保存下来。一般的保存数据的方式是写入文件或者写入数据库，相信你已经很熟悉了。但是万一我们要保存的数据，是Python程序中的一个对象呢？在保存这个对象后，还能再次加载回来，并且保证任何成员变量/函数没有任何改变么？

要实现这一要求，就有点像把一个人完全冰冻起来，然后再解冻，并且保证这个人依然健康。这听起来很困难，但是也很有趣，不是么？

其实这个过程就叫做序列化/反序列化：将内存中的对象保存至磁盘，并在以后可以再次加载入内存，以实现数据的保存与传输。所以你的任务是：

* 定义一个类，创建一个类的对象，并将这个对象序列化/反序列化。
* 将上述的类也序列化/反序列化。（注意，这里是对“类”这个对象进行序列化！）





### 【[解决思路](solution.md)】
