import pandas as pd
import numpy as np
import math
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

chat_id = 298754188 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha=0.01
    
    p_value=proportions_ztest([x_success, y_success], [x_cnt, y_cnt])[1] / 2
    
    if (p_value < alpha) and (x_success/x_cnt < y_success/y_cnt):
      return True
    else: 
      return False
    
# def solution(x_success: int, 
#              x_cnt: int, 
#              y_success: int, 
#              y_cnt: int) -> bool:
#     # Измените код этой функции
#     # Это будет вашим решением
#     # Не меняйте название функции и её аргументы
#     _, pval = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
#     alpha = 0.01
#     effect = (pval < alpha)
    
#     return effect # Ваш ответ, True или False
