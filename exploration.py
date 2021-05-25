import pandas as pd
import googletrans
from google_trans_new import google_translator
from IPython.display import display
from pythainlp.tokenize import word_tokenize
import ThaiAddressParser
from sklearn.preprocessing import LabelEncoder


# user = pd.read_csv("user_applications.csv")
# previous = pd.read_csv("previous_job_post.csv")
active = pd.read_csv("active_en_sub.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# display(previous['location'].unique())
#
# symbols = '{}()[].,:;+-*/&|<>=~$1234567890'
# previous['token_location'] = previous['location'].map(lambda x: word_tokenize(x, engine="newmm",keep_whitespace=False))
# previous['token_location'] = previous['token_location'].map(lambda x: [item.translate(str.maketrans('','',symbols)).strip() for item in x] )
# print(previous['token_location'])

######################################################################################################################

# previous = previous.dropna(subset=['location'])
# previous['location'] = previous['location'].astype('str')
#
# provinces = []
# for row in previous.location:
#     print(row)
#     try:
#         provinces.append(ThaiAddressParser.parse(row)['province']['en'])
#     except:
#         provinces.append('')
#
# previous['province'] = provinces
#
# print(previous['province'].sort_values())
#
# previous = previous.dropna(subset=['province'])
# lab_enc = LabelEncoder()
# previous["province_code"] = lab_enc.fit_transform(previous[["province"]])
# print(previous[["province", "province_code"]].head(11))

######################################################################################################################

active = active.dropna(subset=['location'])
active['location'] = active['location'].astype('str')

provinces = []
for row in active.location:
    print(row)
    try:
        provinces.append(ThaiAddressParser.parse(row)['province']['en'])
    except:
        provinces.append('')

active['province'] = provinces

print(active['province'].sort_values())

active = active.dropna(subset=['province'])

active.to_csv("active_en_sub.csv")
# lab_enc = LabelEncoder()
# previous["province_code"] = lab_enc.fit_transform(previous[["province"]])
# print(previous[["province", "province_code"]].head(11))

# my_pivot = pd.pivot_table(user,values=['count'], index=['user_id'],columns=['job_id'],aggfunc=np.sum,fill_value=0)
# display(my_pivot)

# print(user.columns)
# print(previous.columns)
# print(active.columns)
#
# print(previous['role_name'].unique())

# translator = google_translator()
# df = pd.DataFrame({'Thai':['หมา', 'แมว']})
# df['English'] = df['Thai'].map(lambda x: translator.translate(x, lang_tgt = 'en'))
#
# translations = {}
# for column in previous.columns:
#     # unique elements of the column
#     unique_elements = previous[column].unique()
#     for element in unique_elements:
#         # add translation to the dictionary
#         translations[element] = translator.translate(element,lang_tgt = 'en')
#
# # previous['role_name'] = previous['role_name'].map(lambda x: translator.translate(x, lang_tgt = 'en'))
#
# print(translations)
# previous.replace(translations, inplace = True)
#
# previous.to_csv("previous_en.csv")

# # Checking number of rows
# print(active['job_id'].count())
# print (pd.merge(active['job_id'],user['job_id'], indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1).count())


# display(user.sort_values("user_id"))
# print(previous.head())
# print(active.head())

# apps_info = user.merge(previous,left_on='job_id',right_on='job_id',how='left')
#
# # display(apps_info.head())
#
# # print(apps_info.columns)
#
# print(active.columns)
#
# # print(previous['role_name'].count())
# # print(previous.groupby('role_name')['company_name'].nunique())
# # print(apps_info.groupby('role_name')['job_id'].nunique().sort_values())
#
# print(user.groupby('user_id')['job_id'].nunique())
#
