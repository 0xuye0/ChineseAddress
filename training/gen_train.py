# -*- coding: utf-8 -*-
import data_prep_utils
import re
sheng = set()
shi = set()
qu = set()
xian = set()
zizhizhou = set()
zizhixian = set()
zizhiqu = set()
qi = set()
meng = set()
zhou = set()

all_set = [zizhizhou, zizhiqu, zizhixian,
           qi, meng, zhou, xian, qu, shi, sheng]

name = ['自治州',
        '自治区',
        '自治县',
        '旗',
        '盟',
        '州',
        '县',
        '区',
        '市',
        '省']

label = ['zizhizhou',
         'zizhiqu',
         'zizhixian',
         'qi',
         'meng',
         'zhou',
         'xian',
         'qu',
         'shi',
         'sheng',
         'not'
         ]
data = open('../raw/uniq_quanguo_qu_xian_data.1')
out = []
for line in data:
    a = line.strip().split('\t')
    out1 = []
    out2 = []
    for i in a:
        b = re.sub(r'\(.*?\)','',i)
        for j in range(len(name)):
            if name[j] in b:
                out1.append((b.decode('utf8'), label[j]))
                temp = b.replace(name[j],'')
                if temp != "":
                    out2.append((temp.decode('utf8'), label[j]))
                break
    out.append(out1)
    out.append(out2)

data_prep_utils.appendListToXMLfile(out,'./labeled.xml')
