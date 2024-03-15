import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/fmcg")

files=['dim_campaigns','dim_products','dim_stores','fact_events']

for file in files:
    df = pd.read_csv(f"D:/Project/FMCG Project/C9_Input_Files/dataset/{file}.csv")
    df.to_sql(file, con=engine, if_exists='replace',index=False)