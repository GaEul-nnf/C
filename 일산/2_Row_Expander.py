# 한개의 행을 6개로 복사(기온, 습도)

import pandas as pd

df = pd.read_csv('E:\\백석1동_습도_20230111_20241130.csv')
df_repeated = df.loc[df.index.repeat(6)].reset_index(drop=True)
df_repeated.to_csv('E:\\six_백석1동_습도_20230111_20241130.csv', index=False)
