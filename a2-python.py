# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

csv_data = pd.read_csv('cars-sample.csv')  # 读取训练数据
print(csv_data.shape)
N = 5
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data.shape)  # (5, 9)
manufacturer = csv_batch_data[list(range(0, 1))]  # 取这20条数据的3到5列值(索引从0开始)
print(manufacturer)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('Weight')
plt.ylabel('MPG')
plt.xlim(xmax=5000, xmin=1500)
plt.ylim(ymax=47, ymin=10)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.random.normal(2000, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
x2 = np.random.normal(2500, 1.2, 300)
x3 = np.random.normal(3000, 1.2, 300)
x4 = np.random.normal(3500, 1.2, 300)
x5 = np.random.normal(4000, 1.2, 300)
y1 = np.random.normal(20, 1.2, 300)
y2 = np.random.normal(25, 1.2, 300)
y3 = np.random.normal(30, 1.2, 300)
y4 = np.random.normal(35, 1.2, 300)
y5 = np.random.normal(40, 1.2, 300)
colors1 = '#FFFF00'  # 点的颜色
colors2 = '#FF4500'
colors3 = '#00FF00'
colors4 = '#FF69B4'
colors5 = '#00BFFF'

area = np.pi * 4 ** 2  # 点面积
# 画散点图
plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='BMW')
plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='ford')
plt.scatter(x3, y3, s=area, c=colors3, alpha=0.4, label='honda')
plt.scatter(x4, y4, s=area, c=colors4, alpha=0.4, label='mercedes')
plt.scatter(x5, y5, s=area, c=colors5, alpha=0.4, label='toyota')
#plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
plt.legend()
plt.savefig(r'C:\Users\Lenovo\Desktop\573\A2\a2-DataVis-5ways\test1.png', dpi=300)
plt.show()