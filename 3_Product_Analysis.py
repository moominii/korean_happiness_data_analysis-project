# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:34:37 2025

@author: Jiyeon Baek

전처리 끝난 데이터 시각화 및 분석
danawa_data_final.xlsx

"""
### 무선청소기 모델별 비교 분석 ####
import pandas as pd
danawa_data = pd.read_excel("C:/Users/Admin/Desktop/JY/Python/20250220/danawa_data_final.xlsx")

# 흡입력 기준 정렬 : 평균
price_mean_value = danawa_data['가격'].mean()
suction_mean_value = danawa_data['흡입력'].mean()
use_time_mean_value = danawa_data['사용시간'].mean()

# 가성비 좋은 제품 탐색
condition_data = danawa_data[
                            (danawa_data['가격'] <= price_mean_value) &
                             (danawa_data['흡입력'] >= suction_mean_value) & 
                             (danawa_data['사용시간'] >= use_time_mean_value)]

#### 데이터 시각화 ####
import matplotlib.pyplot as plt 
import seaborn as sns

from matplotlib import font_manager, rc 
import platform 


if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')
# --------------여기까지 시각화 준비작업 -------------------

# 결측값 없애기
chart_data = danawa_data.dropna(axis=0)

# 흡입력, 사용시간 최대, 최소
suction_max_value = chart_data['흡입력'].max()
suction_mean_value = chart_data['흡입력'].mean()

use_time_max_value = chart_data['사용시간'].max()
use_time_mean_value = chart_data['사용시간'].mean()

# 청소기 성능 시각화
plt.figure(figsize=(20, 10))
plt.title("청소기 성능")
sns.scatterplot(
                x = '흡입력',
                y = '사용시간',
                size = '가격',
                hue = chart_data['회사명'],
                data = chart_data,
                sizes = (10, 1000),
                legend=False
                )
plt.plot([0, suction_max_value], [use_time_mean_value, use_time_mean_value],
         'r--',
         lw = 1 )



plt.plot([suction_mean_value, suction_mean_value],
         [0, use_time_max_value],
         'r--',
         lw = 1 )
plt.show()

# 인기 제품의 데이터 시각화
chart_data_selected = chart_data[:20]

suction_max_value = chart_data_selected['흡입력'].max()
suction_mean_value = chart_data_selected['흡입력'].mean()

use_time_max_value = chart_data_selected['사용시간'].max()
use_time_mean_value = chart_data_selected['사용시간'].mean()


plt.figure(figsize=(20, 10))
plt.title("무선 핸디/스틱청소기 TOP 20")

sns.scatterplot(
                x = '흡입력',
                y = '사용시간',
                size = '가격',
                hue = chart_data_selected['회사명'],
                data = chart_data_selected,
                sizes = (100, 2000),
                legend=False
                )

plt.plot([60, suction_max_value], [use_time_mean_value, use_time_mean_value],
         'r--',
         lw = 1 )



plt.plot([suction_mean_value, suction_mean_value],
         [20, use_time_max_value],
         'r--',
         lw = 1 )

for index, row in chart_data_selected.iterrows():
    x = row['흡입력']
    y = row['사용시간']
    s = row['제품'].split(' ')[0]
    plt.text(x, y, s, size=20)
    

plt.show()
















