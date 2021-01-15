
import pandas as pd
data = pd.read_csv('sample_prediction_last_26_rows.txt', sep=",", header=None)
data.columns = ['row_id', 'predictions']
