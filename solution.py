import pandas as pd
import numpy as np


chat_id = 462449141 # Ваш chat ID, не меняйте название переменной

from statsmodels.stats.proportion import proportions_ztest

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    alpha = 0.04
    
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    
    _, p_value = proportions_ztest(counts, nobs, alternative = 'smaller')

    return p_value < alpha # Ваш ответ, True или False
