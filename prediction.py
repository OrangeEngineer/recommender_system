import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder

active = pd.read_csv("active_en_sub.csv")
active.dropna(subset=['role_name', 'sub_role_name', 'company_name', 'province'], inplace=True)
active = active[~active.province.str.contains("Nan")]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

active['sub_role_name'] = active['sub_role_name'].str.split("/", n = 1, expand = True)[0]
active['sub_role_name'] = active['sub_role_name'].str.lower()
active['sub_role_name'] = active['sub_role_name'].str.strip()

active['role_name'] = active['role_name'].str.split("/", n = 1, expand = True)[0]
active['role_name'] = active['role_name'].str.lower()
active['role_name'] = active['role_name'].str.strip()

a_file = open("roles.pkl", "rb")
roles = pickle.load(a_file)

active['role_name'] = active['role_name'].replace(roles)
active['sub_role_name'] = active['sub_role_name'].replace(roles)

print(active.groupby('role_name')['job_id'].nunique())

df = pd.DataFrame(active, columns=['role_name','sub_role_name','province','company_name'])

lab_enc = LabelEncoder()
for column in df.columns:
    pkl_file = column + "_LabelEncoder.pkl"
    with open(pkl_file, 'rb') as file:
        pickle_model = pickle.load(file)
    df[column] = pickle_model.transform(df[column])

print(df.head())


kmodes_model = "job_kmodes_model.pkl"
with open(kmodes_model, 'rb') as file:
    km = pickle.load(file)

y = km.predict(df)

print(y)

active['cluster'] = y

print(active[['role_name','sub_role_name','province','company_name','cluster']].head(10))

active.to_csv("active_clustered.csv",index=False)