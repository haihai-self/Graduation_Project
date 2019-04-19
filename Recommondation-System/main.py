# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 下午5:16
# @Author  : hai
# @FileName: main.py
# @Software: 
# @github    ：https://github.com/mo-hai/

import numpy as np
import pandas as pd

from data_Preprocessing import ML_Data_preprocessing
from MF_Recommendation import Matrix_Factorization
from measure import measure_method
if __name__ == '__main__':
    ML_Data_preprocessing.data_preprecess()
    path = '/home/mo/workspace/Graduation_Project/Recommondation-System/'

    # 导入数据
    movies_feature = pd.read_csv(path+'data/ml-latest-small/movies_feature.csv', index_col=0)
    user_rating = pd.read_csv(path+'data/ml-latest-small/user_rating.csv', index_col=0)

    train, test = ML_Data_preprocessing.train_test_split(user_rating)

    
    # 使用矩阵分解算法来估计评分
    MF_estimate = Matrix_Factorization.Matrix_Factorization(K=10, epoch=5)
    MF_estimate.fit(train)
    R_hat = MF_estimate.start()
    non_index = test.values.nonzero()
    pred_MF = R_hat[non_index[0], non_index[1]]
    actual = test.values[non_index[0], non_index[1]]

    print('MSE of MF is %s' % measure_method.comp_mse(pred_MF, actual))
    print('RMSE of MF is %s' % measure_method.comp_rmse(pred_MF, actual))
