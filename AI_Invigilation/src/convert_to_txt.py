import pandas as pd

def convert_json(filename, filepath):
    df = pd.read_json(filename, lines=True)
    df = df.to_csv(filepath+filename)
    return 


