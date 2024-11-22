# 한개의 행을 6개로 나눔
import pandas as pd

df = pd.read_csv('E:\\업무지시\\백석1동_기온_20230111_20241031.csv')
df_repeated = df.loc[df.index.repeat(6)].reset_index(drop=True)
df_repeated.to_csv('E:\\업무지시\\six_백석1동_기온_20230111_20241031.csv', index=False)
