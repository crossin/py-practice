# -*- coding: utf-8 -*-

'''
这里是在交互式命令行下输入的内容：

sc.textFile('/xxxx/xx.txt').flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).collect()
(将xxxx，换成你要统计的文件，请使用绝对路径)

是的！只要这一行！函数式编程就是这么优雅！
如果你有兴趣的话，可以自己去搜索Spark的相关函数，理解上述代码的意思。
不过，光从字面上，也可以大体猜出来这行代码在做什么吧？

'''

# 这里是提交到spark-submit的内容：
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName('My wordcount')
    # 配置Spark参数，设置地址以及名称
    sc = SparkContext(conf=conf)
    # 新建一个Spark上下文，从这开始，就和命令行方式一样了。
    # 但是我们拆分开写，更清楚些
    file_in = sc.textFile('/xxxx/xx.txt')
    # (将xxxx，换成你要统计的文件，请使用绝对路径)

    words = file_in.flatMap(lambda x: x.split(' '))
    # 将每行字符串按照空格分割
    counts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    # 统计每个单词的个数
    result = counts.collect()
    # 真正开始计算
    print(result)
    # 在这种方式下，默认屏幕是不会输出的，因此我们手动输出结果。
