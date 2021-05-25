import pandas as pd

rec = pd.read_csv("recommendation_2.csv")

print(rec.head())

# print(list(rec['recommendation'][0]))

rec['recommendation'] = rec['recommendation'].str.strip('[]')

res = rec.groupby('user_id').agg({'recommendation': lambda x: ','.join(x) })

res.to_csv("Result.csv")

