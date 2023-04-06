import pandas as pd
import numpy as np
from scipy.stats import expon

chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    loc, scale = -35, 1
    expon_rv = expon(loc=loc, scale=scale)
    mu = expon_rv.mean()
    return (x.mean()-mu)/10 ** 2
 # Ваш ответ
