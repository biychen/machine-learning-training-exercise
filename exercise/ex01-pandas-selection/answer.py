import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

if __name__ == '__main__':
    print(df)
    print(df['2013-01-02':'2013-01-03'])
    print(df.loc[:, 'B':'C'])
    print(df.loc['2013-01-04':'2013-01-06', 'A':'B'])
    print(df[(df.B > 0) & (df.C > 0)])