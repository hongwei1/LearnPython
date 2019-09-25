b'ABC' # each char only take one byte
'ABC' # this is string, each take two.
'ABC'.encode('ascii')
'中文'.encode('utf-8')
# '中文'.encode('ascii') # can not make this. no mapping for chinese here.

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #--> '中文'

# len(str)--> 字符数
# len(b'ac') 00>字节数.

# 一个中文,经过UTF-8 编码后通常占用3个字节.

# 源码也是一个文本,遇到中文,必须保存为 UTF-8. 一般在开头指定:
#! /usr/bin/env python3 -->告诉 Linux/OS X 是一个 python. windows 会忽略
# -*- coding: utf-8 -*- --> 安装 UTF-8 读取源码.

'Hi, %s, you have $%d.' % ('Michael', 1000000)

# %运算符用来格式化字符串的.在字符串内部,%s用于字符串, %d 用整数, %? 

