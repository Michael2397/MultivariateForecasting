from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import r2_score
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers import LSTM
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from keras.layers import Dropout

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

neurons = 512                 # number of hidden units in the LSTM layer
activation_function = 'tanh'  # activation function for LSTM and Dense layer
loss = 'mse'                  # loss function for calculating the gradient, in this case Mean Squared Error
optimizer= 'adam'             # optimizer for appljying gradient decent
dropout = 0.25                # dropout ratio used after each LSTM layer to avoid overfitting
batch_size = 128
epochs = 5
window_len = 7               # is an intiger to be used as the look back window for creating a single input sample.
training_size = 0.8

def build_model(inputs, output_size, neurons, activ_func=activation_function, dropout=dropout, loss=loss, optimizer=optimizer):
  """
  inputs: input data as numpy array
  output_size: number of predictions per input sample
  neurons: number of neurons/ units in the LSTM layer
  active_func: Activation function to be used in LSTM layers and Dense layer
  dropout: dropout ration, default is 0.25
  loss: loss function for calculating the gradient
  optimizer: type of optimizer to backpropagate the gradient
  This function will build 3 layered RNN model with LSTM cells with dripouts after each LSTM layer
  and finally a dense layer to produce the output using keras' sequential model.
  Return: Keras sequential model and model summary
  """
  model = Sequential()
  model.add(LSTM(neurons, return_sequences=True, input_shape=(inputs.shape[1], inputs.shape[2]), activation=activ_func))
  model.add(Dropout(dropout))
  model.add(LSTM(neurons, return_sequences=True, activation=activ_func))
  model.add(Dropout(dropout))
  model.add(LSTM(neurons, activation=activ_func))
  model.add(Dropout(dropout))
  model.add(Dense(units=output_size))
  model.add(Activation(activ_func))
  model.compile(loss=loss, optimizer=optimizer, metrics=['mae'])
  model.summary()
  return model

# load dataset
dataset = read_csv('requestMultiFeatures.csv', header=0)
dataset2 = read_csv('requestMultiFeaturesShift.csv', header=0)
values = dataset.values
valuesY = dataset2.values

# ensure all data is float
values = values.astype('float32')
valuesY = valuesY.astype('float32')
print(values.shape)
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
scaledY = scaler.fit_transform(valuesY)

# split into train and test sets
x = scaled[0:7940, :]
y = scaledY[0:7940, :]

##交叉验证
train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=1, train_size=0.8)


train_x = train_x.reshape((train_x.shape[0], 1, train_x.shape[1]))
test_x = test_x.reshape((test_x.shape[0], 1, test_x.shape[1]))
print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)

# design network
model = build_model(train_x, output_size=1, neurons=neurons)
history = model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1, validation_data=(test_x, test_y), shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

# make a prediction
yhat = model.predict(test_x)

print(yhat.shape)
test_x = test_x.reshape((test_x.shape[0], test_x.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_x[:, 1:]), axis=1)
print(inv_yhat.shape)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_x[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]



# calculate RMSE
mean_absolute_error = sqrt(mean_absolute_error(inv_y, inv_yhat))
r2_score = sqrt(r2_score(inv_y,inv_yhat))
print("inv_yhat的值：")
print(inv_yhat)
print("inv_y的值：")
print(inv_y)
print('Test mean_absolute_error: %.3f' % mean_absolute_error)
print('Test r2_score: %.3f' % r2_score)

x = []
for num in(range(len(test_x))):
    x.append(num)

plt.plot(x, inv_y, color='black', linestyle='-.', label="真实值",marker=".")
plt.plot(x, inv_yhat, color='green', linestyle='-.', label="预测值",marker="o")
plt.legend() # 显示图例
plt.show()