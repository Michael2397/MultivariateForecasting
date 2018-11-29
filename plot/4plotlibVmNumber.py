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

#最坏的
xWorst = []
yWorst = []

#线性
xLinear = []
yLinear = []

#lstm的
xLSTM = []
yLSTM = []

#lstmQ-learning的
xLSTMQL = []
yLSTMQL = []

for num in(range(288)):
    xWorst.append(num)
    xLSTM.append(num)
    xLSTMQL.append(num)
    xLinear.append(num)
#从文件读取虚拟机个数
yTxt = open('4plotlibVmNumber.txt')  #worst
yRead=yTxt.read()
yList = yRead.split(' ')

yTxt4 = open('4plotlibVmNumberLinear.txt')  #线性
yRead4=yTxt4.read()
yList4 = yRead4.split(' ')

yTxt2 = open('4plotlibVmNumberLSTM.txt')  #lstm
yRead2=yTxt2.read()
yList2 = yRead2.split(' ')

yTxt3 = open('4plotlibVmNumberLSTMQL.txt')  #lstmQl
yRead3=yTxt3.read()
yList3 = yRead3.split(' ')

for str1 in yList:
    yWorst.append(int(str1))
for str2 in yList2:
    yLSTM.append(int(str2))
for str3 in yList3:
    yLSTMQL.append(int(str3))
for str4 in yList4:
    yLinear.append(int(str4))


plt.plot(xWorst, yWorst, color='yellow', linestyle='-.', label="Default",marker=".")
plt.plot(xWorst, yLinear, color='green', linestyle='-.', label="Linear",marker="+")
plt.plot(xLSTM, yLSTM, color='blue', linestyle='-.', label="LSTM",marker="x")
plt.plot(xLSTMQL, yLSTMQL, color='magenta', linestyle='-.', label="LSTMQL",marker="*")
plt.legend() # 显示图例

plt.title('Number of VMs')
plt.xlabel('Time interval(5min)')
plt.ylabel('Number of VMs')
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
