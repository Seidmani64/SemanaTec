import pandas as pd

def read_vanilla(filepath):
    with open(filepath, 'r') as fp:
        data_unsorted = fp.read()
    data_lines = data_unsorted.split('\n')
    data = [f.split(',') for f in data_lines]
    return data


def read_pandas(filepath, names):
    """
    Read a csv in pandas
    returns a pandas dataframe
    """
    df = pd.read_csv(filepath, names = names)

    return df


if __name__ == "__main__":
    filepath = "./data/iris.data"
    names = ['sepal_length','sepal_width',
            'petal_length','petal_width',
            'class']
    df = read_pandas(filepath, names)
    print(df.head(10))

    df['sl+pl'] = df['sepal_length'] + df['petal_length']

    print(df.head())

    df_filtered = df[df['sepal_length']>=5]

    print(df_filtered)
