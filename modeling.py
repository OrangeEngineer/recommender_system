import pandas as pd
from sklearn.preprocessing import LabelEncoder
from kmodes.kmodes import KModes
import pickle

previous = pd.read_csv("previous_en_sub.csv")

previous.dropna(subset=['role_name','sub_role_name','company_name','province'], inplace=True)
previous = previous[~previous.province.str.contains("Nan")]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

previous['sub_role_name'] = previous['sub_role_name'].str.split("/", n = 1, expand = True)[0]
previous['sub_role_name'] = previous['sub_role_name'].str.lower()
previous['sub_role_name'] = previous['sub_role_name'].str.strip()

previous['role_name'] = previous['role_name'].str.split("/", n = 1, expand = True)[0]
previous['role_name'] = previous['role_name'].str.lower()
previous['role_name'] = previous['role_name'].str.strip()


################################## Load Roles Dictionary ############################################

a_file = open("roles.pkl", "rb")
roles = pickle.load(a_file)

previous['role_name'] = previous['role_name'].replace(roles)
previous['sub_role_name'] = previous['sub_role_name'].replace(roles)

print(previous.head(10))
#
df = pd.DataFrame(previous, columns=['role_name','sub_role_name','province','company_name'])

lab_enc = LabelEncoder()
for column in df.columns:
    # df[column] = lab_enc.fit_transform(df[column])
    pkl_file = column + "_LabelEncoder.pkl"
    # with open(pkl_file, 'wb') as file:
    #     pickle.dump(lab_enc, file)
    with open(pkl_file, 'rb') as file:
        pickle_model = pickle.load(file)
    df[column] = pickle_model.transform(df[column])

################################## Clustering Part ############################################

# kmeans = KMeans(n_clusters=80,**kmeans_kwargs).fit(df)

km = KModes(n_clusters=80, init='Huang', n_init=5, verbose=1).fit(df)

kmodes_model = "job_kmodes_model.pkl"
with open(kmodes_model, 'wb') as file:
    pickle.dump(km, file)
# with open(pkl_file, 'rb') as file:
#     pickle_model = pickle.load(file)

y = km.predict(df)

print(y)

previous['cluster'] = y


print(previous[['role_name','sub_role_name','province','company_name','cluster']].head(10))

previous.to_csv("previous_clustered.csv")

# ################################## Evaluation Part ############################################
#
# kmeans_kwargs = {
#     "init": "random",
#     "n_init":10,
#     "max_iter":300,
#     "random_state":42
# }
#
# sse = []
# for k in range(1,150):
#     print('k = '+ str(k))
#     kmodes = KModes(n_clusters=k)
#     kmodes.fit(df)
#     sse.append(kmodes.cost_)
#
# plt.style.use("fivethirtyeight")
# plt.plot(range(1,150),sse)
# plt.xticks(range(1,150))
# plt.xlabel("Clusters")
# plt.ylabel("SSE")
# plt.show()
#############################################################################################
