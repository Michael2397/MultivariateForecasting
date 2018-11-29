import pandas as pd
import numpy as np
import time,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import importlib

def get_week_day(date):
    week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]

def get_datelist(starttime,endtime):
    #get_datelist('20150811','20150922')
    startdate = datetime.datetime(int(starttime[0:4]),int(starttime[5:7]),int(starttime[8:10]))
    #now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    # my_yestoday = startdate + delta
    # my_yes_time = my_yestoday.strftime('%Y%m%d')
    n = 0
    date_list = []
    while 1:
        if starttime<=endtime:
            days = (startdate  + delta*n).strftime('%Y-%m-%d')
            n = n+1
            date_list.append(days)
            if days == endtime:
                break
    data = pd.DataFrame({'开始时间':date_list})
    return data

def loadDataSet(pathName):
	dataset = pd.read_excel(pathName)
	#to datetime
	dataset['开始时间'] = pd.to_datetime(dataset['开始时间'])
	dataset['开始时间'] = dataset['开始时间'].apply(lambda x: str(x)[:10])
	dataset['rentNumber'] = 1
	df = dataset.groupby('开始时间').aggregate('sum').reset_index()[['开始时间','rentNumber']]
	tmp = pd.to_datetime(df['开始时间'])
	week = [get_week_day(item) for item in tmp]
	df['week'] = list(week)
	return df

def stationarity_test(dataset,number):
    data = dataset.copy()
    data = data.iloc[: len(data)-number] #不检测最后number个数据
    #平稳性检测
    from statsmodels.tsa.stattools import adfuller as ADF
    diff = 0
    adf = ADF(data['rentNumber'])
    while adf[1] > 0.05:
        diff = diff + 1
        adf = ADF(data['rentNumber'].diff(diff).dropna())
    print(u'原始序列经过%s阶差分后归于平稳，p值为%s' %(diff, adf[1]))

def month_data(dataset):
    dataset['开始时间']= dataset['开始时间'].apply(lambda x: str(x)[:7])
    df = dataset.groupby('开始时间').aggregate('sum').reset_index()[['开始时间','rentNumber']]
    return df

def plot_monthdata(df):
    df.rentNumber.plot(kind='bar',figsize=(16,4))
    plt.show()

def plot_daydata(dataset):
    dataset.rentNumber.plot(kind='bar',figsize=(100,4))
    plt.show()

def whitenoise_test(dataset,number):
    data = dataset.copy()
    data = data.iloc[: len(data)-number] #不使用最后5个数据
    #白噪声检测
    from statsmodels.stats.diagnostic import acorr_ljungbox
    [[lb], [p]] = acorr_ljungbox(data['rentNumber'], lags = 1)
    if p < 0.05:
        print(u'原始序列为非白噪声序列，对应的p值为：%s' %p)
    else:
        print(u'原始该序列为白噪声序列，对应的p值为：%s' %p)
    [[lb], [p]] = acorr_ljungbox(data['rentNumber'].diff().dropna(), lags = 1)
    if p < 0.05:
        print(u'一阶差分序列为非白噪声序列，对应的p值为：%s' %p)
    else:
        print(u'一阶差分该序列为白噪声序列，对应的p值为：%s' %p)

def plot_acfandpacf(dataset):
    D_data = dataset.rentNumber
    from statsmodels.graphics.tsaplots import plot_acf
    from statsmodels.graphics.tsaplots import plot_pacf
    fig = plt.figure(figsize=(20,10))
    ax1=fig.add_subplot(211)
    plot_acf(D_data,lags=40,ax=ax1).show()
    ax2=fig.add_subplot(212)
    plot_pacf(D_data,lags=40,ax=ax2).show()
    plt.show()

def plot_results(predicted_data, true_data):
    fig = plt.figure(facecolor='white',figsize=(10,5))
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()

def arma_predict(dataset,number):
    data = list(dataset.rentNumber)
    from statsmodels.tsa.arima_model import ARMA
    """
    import statsmodels.tsa.stattools as st
    order = st.arma_order_select_ic(data,max_ar=2,max_ma=2,ic=['aic', 'bic', 'hqic'])
    """
    model = ARMA(data, order=(1,1))
    result_arma = model.fit(disp=-1, method='css')
    predict = result_arma.predict(len(data)-number,len(data))
    RMSE = np.sqrt(((predict-data[len(data)-number-1:])**2).sum()/(number+1))
    plot_results(predict,data[len(data)-number-1:])
    return predict,RMSE

def plot_date(business):
    xs = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in business['开始时间'][:10]]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    # Plot
    plt.plot(xs,business.rentNumber[:10])
    plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    plt.show()


if __name__ == '__main__':
    print('arma prediction')
    path = 'data/business.xls'
    business = loadDataSet(path)

    test = pd.read_excel(path)
    test.head()

    business.tail(7)

