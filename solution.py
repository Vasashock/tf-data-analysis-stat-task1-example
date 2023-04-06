import pandas as pd
import numpy as np


chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = x.mean() / (10**2)
    s = ((np.exp(1) + 35)**2 - 1) / 12
    a_estimate = a - s / np.sqrt(len(x))
    return x.mean() # Ваш ответ
