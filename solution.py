import pandas as pd
import numpy as np


chat_id = 462449141 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    a = 0.04
    mean1 = x_success/ x_cnt
    mean2 = y_success/ y_cnt
    answer = True
    if mean2-mean1 < a:
      answer = True
    else:
      answer = False
    return answer
