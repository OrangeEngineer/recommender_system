import pandas as pd
from fuzzywuzzy import process
import pickle
from sklearn.preprocessing import LabelEncoder

previous = pd.read_csv("previous_en_sub.csv")
active = pd.read_csv("active_en_sub.csv")

all_data = pd.concat([previous, active])

all_data.dropna(subset=['role_name', 'sub_role_name', 'company_name', 'province'], inplace=True)
all_data = all_data[~all_data.province.str.contains("Nan")]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

all_data['sub_role_name'] = all_data['sub_role_name'].str.split("/", n = 1, expand = True)[0]
all_data['sub_role_name'] = all_data['sub_role_name'].str.lower()
all_data['sub_role_name'] = all_data['sub_role_name'].str.strip()

all_data['role_name'] = all_data['role_name'].str.split("/", n = 1, expand = True)[0]
all_data['role_name'] = all_data['role_name'].str.lower()
all_data['role_name'] = all_data['role_name'].str.strip()

def matching_process(df):
    role_dict = {}
    roles = sorted(df.unique())
    for n,role in enumerate(roles):
        print(str(n) +" " + role)
        if len(role)>= 5:
            matches = process.extract(role, df.unique(), limit = len(df.unique()))
            for match in matches:
              # Check whether the similarity score is greater than or equal to 80
              if match[1] >= 90 and len(match[0])>=5 and match[1] < 100:
                if len(match[0]) < len(role):
                    print(match[0] + " -> " + role + ": " +str(match[1]))
                    role_dict[match[0]] = role
                else:
                    print(role + " -> " + match[0] + ": " + str(match[1]))
                    role_dict[role] = match[0]
    print(role_dict)
    return (role_dict)

roles = matching_process(all_data['role_name'])

################################## Senstive Cases for role name ############################################

del roles["administration"]
del roles["business development"]
del roles["design"]

roles['warehouse'] = 'transportation - warehouse'
roles['transport and warehouse'] = 'transportation - warehouse'
roles['banking banking '] = 'bank'

a_file = open("roles.pkl", "wb")
pickle.dump(roles, a_file)
a_file.close()

all_data['role_name'] = all_data['role_name'].replace(roles)
all_data['sub_role_name'] = all_data['sub_role_name'].replace(roles)

print(all_data.head(10))

df = pd.DataFrame(all_data, columns=['role_name','sub_role_name','province','company_name'])

lab_enc = LabelEncoder()
for column in df.columns:
    df[column] = lab_enc.fit_transform(df[column])
    pkl_file = column + "_LabelEncoder.pkl"
    with open(pkl_file, 'wb') as file:
        pickle.dump(lab_enc, file)