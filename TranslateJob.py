import pandas as pd
from google_trans_new import google_translator
import ThaiAddressParser

from IPython.display import display

def translation(df):
    translator = google_translator()
    unique_elements = df.unique()
    translations = {}

    for element in sorted(unique_elements):
        # add translation to the dictionary
        translation = translator.translate(element, lang_tgt='en')
        print(element + " -> " + translation)
        translations[element] = translation

    print(translations)
    return translations

def FindProvince(df):
    provinces = []
    for row in df:
        try:
            provinces.append(ThaiAddressParser.parse(row)['province']['en'])
        except:
            provinces.append('')

    return provinces

previous = pd.read_csv("previous_job_post.csv")
active = pd.read_csv("active_job_post.csv.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

############################# Role_name and Sub_role_name Part #########################################################

active.drop(active.columns[[0,1,2]], axis=1,inplace=True)
active.dropna(subset=['role_name','sub_role_name'], inplace=True)
previous.dropna(subset=['role_name','sub_role_name'], inplace=True)

active_translations = translation(active['role_name'])
previous_translations = translation(previous['role_name'])

active['role_name'].replace(active_translations, inplace=True)
previous['role_name'].replace(previous_translations, inplace=True)

active_translations = translation(active['sub_role_name'])
previous_translations = translation(previous['sub_role_name'])

active['sub_role_name'].replace(active_translations, inplace=True)
previous['sub_role_name'].replace(previous_translations, inplace=True)

active = active.dropna(subset=['location'])
previous = previous.dropna(subset=['location'])

########################################### Province Part #########################################################

previous['location'] = previous['location'].astype('str')
active['location'] = active['location'].astype('str')

previous['province'] = FindProvince(previous['location'])
active['province'] = FindProvince(active['location'])

print(sorted(previous['province'].unique))
print(sorted(active['province'].unique))

previous = previous.dropna(subset=['province'])
active = active.dropna(subset=['province'])

previous.to_csv("previous_en_sub.csv",index=False)
active.to_csv("active_en_sub.csv",index=False)
