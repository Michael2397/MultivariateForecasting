#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from pprint import pprint


if __name__ == "__main__":
    dataset = pd.read_csv('requestMultiFeatures.csv', header=0)
    dataset2 = pd.read_csv('requestMultiFeaturesShift.csv', header=0)
    x = dataset.values
    y = dataset2.values
    print(x)
    print(y)

    mpl.rcParams['font.sans-serif'] = ['simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x_train, y_train = x[0:7775, 0:13], y[0:7775, :]
    x_test, y_test = x[7797:7900, 0:13], y[7797:7900, :]

    # x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
    print(type(x_test))
    print(x_train.shape, y_train.shape)

    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print(model)
    print('回归系数=', linreg.coef_, '截距=', linreg.intercept_)

    y_hat = linreg.predict(x_test)

    print(y_test)
    print(y_hat)
    rmse = mean_squared_error(y_test, y_hat)
    print('RMSE = ', rmse)
    mean_absolute_error = mean_absolute_error(y_test, y_hat)
    print('mean_absolute_error = ', mean_absolute_error)
    r2Score = r2_score(y_test,y_hat)
    print('r2Score = ', r2Score)

    plt.figure(facecolor='w')
    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='真实数据')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='预测数据')
    plt.legend(loc='upper left')
    plt.title('线性回归预测请求量', fontsize=18)
    plt.grid(b=True, ls=':')
    plt.show()
