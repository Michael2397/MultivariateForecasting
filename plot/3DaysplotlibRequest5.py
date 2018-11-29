#coding:utf-8
import pandas as pd
import numpy as np
import  os
from pylab import *
from matplotlib.ticker import  MultipleLocator

from matplotlib.ticker import  FormatStrFormatter

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#x是第几个300秒
x = []
#y是需要几个虚拟机
y = []

for num in(range(864)):
    x.append(num)

#从文件读取虚拟机个数
yTxt = open('3Daysrequest5.txt')
yRead=yTxt.read()
yList = yRead.split(' ')

for str in yList:
    y.append(int(str))

print(y)
print(len(x))
print(len(y))

plt.plot(x, y, 'b-', label="1")  # b代表blue颜色  -代表直线
# group_labels = ['a', 'b','c','d','e']
# # plt.xticks(group_labels, rotation=0)
# xmajorLocator = MultipleLocator(72);
# ax = subplot(111)
# ax.xaxis.set_major_locator(xmajorLocator)

plt.title('Workload of NASA')
plt.xlabel('Time interval(5min)')
plt.ylabel('User requests(req/5min)')
plt.show()


#
#
#
#
# jiaodu = ['0', '15', '30', '15', '60', '75', '90', '105', '120']
# x = range(len(jiaodu))
#
# y = [85.6801, 7.64586, 86.0956, 159.229, 179.534, 163.238, 96.4436, 10.1619, 90.9262, ]
#
# # plt.figure(figsize=(10, 6))
#
# plt.plot(x, y, 'b-', label="1", marker='*', markersize=7, linewidth=3)  # b代表blue颜色  -代表直线
#
# plt.title('vm个数')
# plt.legend(loc='upper left',bbox_to_anchor=(1.0,1.0))
# # plt.xticks((0,1,2,3,4,5,6,7,8),('0', '15', '30', '15', '60', '75', '90', '105', '120'))
# plt.xlabel('角度')
# plt.ylabel('亮度')
# #plt.grid(x1)
# plt.show()
