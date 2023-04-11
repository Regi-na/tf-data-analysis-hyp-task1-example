import pandas as pd
import numpy as np


chat_id = 947352272 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return proportions_ztest([x_success,y_success], [x_cnt,y_cnt], alternative = 'larger')[0] < 0 # Ваш ответ, True или False
