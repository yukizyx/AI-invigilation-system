import pandas as pd
import re
import Timestamp

def convert_json(filename, filepath):
    df = pd.read_json(filename, lines=True)
    df = df.transform_data(filename, filepath)
    df = df.to_csv(filepath+filename)
    return 



def transform_data(filename, filepath):
    # find the first occurrence of 8 digits in the filename
    match = re.search(r"\d{8}", filename)   
    if match:
        digits = match.group()  

    df['timestamp'] = Timestamp(digits)
    # df['timestamp'] = pd.to_datetime(df['timestamp_column'])
    df = df.sort_values(by='timestamp')

    # Calculate the difference between consecutive timestamps and store in a new column
    df['time_diff'] = df['timestamp'].diff()
    average_time_diff = df['time_diff'].mean()
    df['average_trigger_time'] = average_time_diff