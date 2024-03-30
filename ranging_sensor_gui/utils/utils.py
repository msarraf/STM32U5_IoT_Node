import pandas as pd
from datasets.RangingSensor import RangingData
import logging
from Settings.GUI_settings import SAVE_DATA_MESSAGE


def save_data_to_csv(data:RangingData) -> None:
    data_df = pd.DataFrame(data)
    data_df.to_csv('data.csv', index=False)
    logging.info(SAVE_DATA_MESSAGE.SAVE_DATA_MESSEAGE)