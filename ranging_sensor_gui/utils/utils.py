import pandas as pd
from datasets.RangingSensor import RangingData

def save_data_to_csv(data:RangingData) -> None:
    data_df = pd.DataFrame(data)
    data_df.to_csv('data.csv', index=False)