import pandas as pd
import math


def load_and_process():
    result = pd.read_csv('./data/nba-player-2014.csv', na_values='-')
    result.fillna(0, inplace=True)
    return result


def euclidean_distance(row1, row2, columns):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in columns:
        inner_value += (row1[k] - row2[k]) ** 2
    return math.sqrt(inner_value)


def filter_columns(dataframe, excluded):
    return dataframe.drop(excluded, axis='columns')


def normalize(dataframe):
    return (dataframe - dataframe.mean()) / dataframe.std()


def test_knn(core_name, k, normalize_stat=True):
    distance_excluded_columns = ['fullname']
    players = load_and_process()
    if normalize_stat:
        stat = normalize(filter_columns(players, distance_excluded_columns))
    else:
        stat = filter_columns(players, distance_excluded_columns)
    core = stat[players.fullname == core_name]
    distance_series = stat.apply(lambda r: euclidean_distance(core, r, core.columns), axis='columns')
    distances = pd.DataFrame({
        'dist': distance_series
    }, index=distance_series.index)
    distances.sort_values(by='dist', inplace=True)
    neighbors = players.iloc[distances[0:k+1].index].copy()
    neighbors['Distance'] = distances[0:k+1].dist
    return neighbors


if __name__ == '__main__':
    print(test_knn('James, LeBron', 5, normalize_stat=False))
    print(test_knn('James, LeBron', 5))