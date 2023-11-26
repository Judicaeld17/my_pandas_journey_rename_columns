# TASK: Create a function which receive a pandas dataframe, a need_to_be_renamed and into_what as parameter and returns data frame with the column need_to_be_renamed rename with into_what.
import pandas as pd
def my_pandas_journey_rename_columns(df,current_col_name,wantted_col_name):
    df.rename(columns={current_col_name:wantted_col_name},inplace=True)
    return df