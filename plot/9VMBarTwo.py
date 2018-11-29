import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
plt.subplot(211)
rects1 =plt.bar(left = (0.1),height = (2306),color=('red'),width = 0.1,align="center",yerr=0.000001)
rects2 =plt.bar(left = (0.3),height = (2310),color=('green'),width = 0.1,align="center",yerr=0.000001)
rects3 =plt.bar(left = (0.5),height = (2345),color=('blue'),width = 0.1,align="center",yerr=0.000001)
rects4 =plt.bar(left = (0.7),height = (2370),color=('magenta'),width = 0.1,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.1,0.3,0.5,0.7),('Default','Linear','LSTM','LSTMQL'))
#plt.title('Pe')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
plt.title("NASA")
plt.ylabel('Total number of VMs')

plt.subplot(212)
rects1 =plt.bar(left = (0.1),height = (2812),color=('red'),width = 0.1,align="center",yerr=0.000001)
rects2 =plt.bar(left = (0.3),height = (2824),color=('green'),width = 0.1,align="center",yerr=0.000001)
rects3 =plt.bar(left = (0.5),height = (2818),color=('blue'),width = 0.1,align="center",yerr=0.000001)
rects4 =plt.bar(left = (0.7),height = (3002),color=('magenta'),width = 0.1,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.1,0.3,0.5,0.7),('Default','Linear','LSTM','LSTMQL'))
#plt.title('Pe')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
plt.title("ClarkNet")
plt.ylabel('Total number of VMs')
plt.show()