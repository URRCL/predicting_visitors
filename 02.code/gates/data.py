import numpy as np
import pandas as pd
import seaborn as sns

data_input = '../01.data/PeopleCountData.txt'
data_output = '../01.data/PeopleCountData_wide.txt'


def reshape_toWide(data_input, data_output):

    column_names = ['date','time','ip','entrypoint','incoming','outgoing']
    data_raw = pd.read_csv(data_input,names=column_names)

    data = data_raw.copy()
    data['timestamp'] = pd.to_datetime(data.date+' '+data.time)

    columns_values = ['incoming', 'outgoing']

    data_wide = data.pivot_table(values = columns_values,
                                 index = ['timestamp'],
                                 columns = 'entrypoint',
                                 aggfunc = 'mean').diff()

    data_wide.columns = ['_'.join(t) for t in data_wide.columns]
    data_wide = data_wide.dropna()

    return(data_wide)

data_wide = reshape_toWide(data_input,data_output)

data_wide.to_csv(path_or_buf=data_output, sep='|')
