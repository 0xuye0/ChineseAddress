# -*- coding: utf-8 -*-
import ChineseAddress
query = "黑龙江省 北京市 云南省 临沧市 临翔区"
query1 = "云南省 临沧市 临翔区"
query2 = "广西壮族自治区 南宁市"
query3 = "黑龙江省 齐齐哈尔市"
query4 = "不知道省 不知道市 sha区 unknown县"
query5 = "黑龙江 哈尔滨 齐齐哈尔 北京"
print '###########tokenize###########'
query = query5
a = ChineseAddress.tokenize(query)
for i in a:
    print i
print '#######tokens2features#######'
b = ChineseAddress.tokens2features(a)
for i in b:
    for j in i:
        print j, '\t', i[j]
print '#######tag#######'
a = ChineseAddress.tag(query)
for i in a:
    print i, '\t', a[i]

