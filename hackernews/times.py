import read

from dateutil.parser import parse


df = read.load_data()

def return_hour(timestamp):
    p = parse(timestamp)
    return p.hour

hours = df['submission_time'].apply(return_hour)

print(hours.value_counts())