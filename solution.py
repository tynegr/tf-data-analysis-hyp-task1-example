
 

import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 462449141 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    p_val = proportions_ztest(count, nobs, alternative='larger')[1]
    return True if p_val <= 0.04 else False
