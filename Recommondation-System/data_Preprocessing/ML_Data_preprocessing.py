# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 下午2:31
# @Author  : hai
# @FileName: ML_Data_preprocessing.py
# @Software: 
# @github    ：https://github.com/mo-hai/

import numpy as np
import pandas as pd
import re


def _judge_of_year(year):
    # 判断电影上映年份所属的年代
    # :param year: int, 电影上映年代
    # :return: str, 所属年代的字符串
    if isinstance(year, int):
        if year < 2000:
            return '90s'
        elif year < 2010:
            return '00s'
        else:
            return '10s'


if __name__ == '__main__':
    # 创建user-item评分矩阵
    print('Loading data...')
    rating_data = pd.read_csv('../data/ml-latest-small/ratings.csv')
    print(rating_data)
    user_id = rating_data['userId'].unique()
    movie_id = rating_data['movieId'].unique()
    rating_matrix = np.zeros([len(user_id), len(movie_id)])
    rating_matrix = pd.DataFrame(rating_matrix, index=user_id, columns=movie_id)

    print('Converting data...')
    count = 0
    user_num = len(user_id)
    for uid in user_id:
        user_rating = rating_data[rating_data['userId'] == uid].drop(['userId', 'timestamp'], axis=1)
        user_rated_num = len(user_rating)

        for row in range(0, user_rated_num):
            movieId = user_rating['movieId'].iloc[row]
            rating_matrix.loc[uid, movieId] = user_rating['rating'].iloc[row]

        count += 1
        if count % 100 == 0:
            completed_percentage = round(float(count) / user_num * 100)
            print("Completed %s" % completed_percentage + "%")

    rating_matrix.to_csv('../data/ml-latest-small/user-rating.csv')

    # 创建电影的年份特征
    print('Loading data..')
    movies_data = pd.read_csv('../data/ml-latest-small/movies.csv')
    movies_num = len(movies_data)

    print('Creating te feature of years/n')
    years = ["Unknowyear", "90s", "00s", "10s"]  # 定义年份的划分区间
    for year in years:
        movies_data[year] = np.zeros([movies_num, 1])
    count = 0

    for i in range(0, movies_num):
        title = movies_data.loc[i]['title']

        pattern = re.compile(r'\d{4}')
        result = pattern.findall(title)

        # 判断电影所属年份区间
        if len(result) != 0:
            year_of_movie = result[-1]
            year_col = _judge_of_year(int(year_of_movie))
            movies_data.loc[i, year_col] = 1
        else:
            movies_data.loc[i, 'Unknowyear'] = 1

        count += 1
        if count % 1000 == 0:
            completed_percentage = round(float(count) / movies_num * 100)
            print("Completed %s" % completed_percentage + "%")

    # 创建电影分类特征
    print('Creating the feature of genres /n')
    # 得到该电影数据集中分类的类别列表
    genres_list = set()

    for genre in movies_data['genres']:
        genres_list = genres_list | set(genre.split('|'))
    # 给每个类别创建一个维度加到原电影数据集中
    genres_list = list(genres_list)
    for genre in genres_list:
        movies_data[genre] = np.zeros([movies_num, 1])

    count = 0
    for j in range(0, movies_num):
        movie_genres = movies_data.loc[j, 'genres'].split('|')
        for k in movie_genres:
            movies_data.loc[j, k] = 1

        count += 1
        if count % 1000 == 0:
            completed_percentage = round(float(count) / movies_num * 100)
            print("Completed %s" % completed_percentage + "%")

    movies_data.set_index('movieId', inplace=True)
    movies_data.drop(['title', 'genres'], axis=1, inplace=True)
    movies_data.to_csv('../data/ml-latest-small/movies_feature.csv')
