import pandas as pd


data = pd.read_csv('hn_stories.csv')

cols = ['submission_time', 'upvotes', 'url', 'headline']


def load_data():
    df = pd.DataFrame(data)
    df.columns = cols
    return df


if __name__ == '__main__':
    load_data()