# 序列化

### 【解决思路】

1. 因为Python中所有数据都是对象，如果我们能够实现将对象进行序列化/反序列化，即代表我们可以将程序运行时所有的数据都保存下来。不用再对不同类型进行不同处理。
2. 和很多语言一样，Python也原生支持序列化，只要使用[pickle](https://docs.python.org/3/library/pickle.html)这个包即可。然后只要使用 `dump` `load`方法即可进行序列化/反序列化。
3. 同样，Python也未能避免序列化带来的安全问题（有关序列化带来的安全隐患，Java程序员一定不陌生），所以还是尽量少使用序列化交换数据，只保存/传输真正有效的数据。毕竟序列化的时间/空间成本都是要高得多的。
4. 目前比较流行的数据交换格式：json，本质上也是一种序列化的手段，但是它和Python默认的序列化对象之间是不兼容的，他们之间的比较可以看[这里](https://docs.python.org/3/library/pickle.html#comparison-with-json)。不过你依然可以使用json来序列化Python对象，不过这稍微有些复杂，有兴趣可以自己研究。

