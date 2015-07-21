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
data = open('../raw/raw.training')
out = []
count = 1
for line in data:
    ##  print count
    count += 1
    a = line.strip().split('\t')
    out1 = []
    ##  out2 = []
    for i in a:
        b = re.sub(r'\([^\)]*?name\)', '', i)
        c = re.search(r'\([^\)]*?name\)', i).group(0)
        if b == "" or c == "":
            print b,'\t', c[1:-1]
        out1.append((b.decode('utf8'), c[1:-1]))
        ##  for j in range(len(name)):
        ##      if name[j] in b:
        ##          temp = b.replace(name[j],'')
        ##          if temp != "":
        ##              out2.append((temp.decode('utf8'), c[1:-1]))
        ##              out.append(out2)
        ##          break
    out.append(out1)

data_prep_utils.appendListToXMLfile(out,'./labeled.xml')
