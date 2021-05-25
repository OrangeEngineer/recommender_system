import pandas as pd
import gower

user = pd.read_csv("user_applications.csv")
previous_cluster = pd.read_csv("previous_clustered.csv")
active_cluster = pd.read_csv("active_clustered.csv")

active_cluster.drop(active_cluster.columns[[0]], axis=1,inplace=True)
clusters = previous_cluster[['job_id','cluster']]
df = pd.merge(user,previous_cluster,how="left",left_on='job_id',right_on='job_id')

df.dropna(subset=['cluster'],inplace=True)
df['recommendation'] = ""

for ind in df.index:

    searching_previous = previous_cluster.loc[previous_cluster.job_id == df.job_id[ind]]
    searching_active = active_cluster.loc[active_cluster.cluster == df.cluster[ind]]

    searching = pd.concat([searching_previous,searching_active])
    searching = searching[['job_id','role_name','sub_role_name','province','company_name']]
    first_row = gower.gower_matrix(searching)[0]
    values = []
    try:
        first_min = min(first_row[first_row != min(first_row)])
        second_min = min(first_row[(first_row != first_min) & (first_row != min(first_row))])
        res = searching[first_row == first_min]
        res2 = searching[first_row == second_min]
        values = list(res.job_id.values) + list(res2.job_id.values)
        print(values)

    except:
        try:
            samp_value = active_cluster['job_id'].loc[active_cluster['cluster'] == int(df['cluster'][ind])].sample(n=2,
                                                                                                                   random_state=1,
                                                                                                                   replace=True).values
            values = values + list(set(samp_value) - set(values))
        except:
            samp_value = active_cluster['job_id'].loc[active_cluster['cluster'] == int(df['cluster'][ind])].values
            values = values + list(set(samp_value) - set(values))
        print("no similar Job")
    print(values)
    df['recommendation'][ind] = values

recommendation = df[['user_id','recommendation']]
recommendation['recommendation'] = recommendation['recommendation'].str.strip('[]')
res = recommendation.groupby('user_id').agg({'recommendation': lambda x: ','.join(x) })
res.to_csv("result.csv",index=False)


