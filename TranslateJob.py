import pandas as pd
from google_trans_new import google_translator
from IPython.display import display

active = pd.read_csv("active_en_sub.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
active.drop(active.columns[[0,1,2]], axis=1,inplace=True)
print(active.head())
# active.dropna(subset=['role_name'], inplace=True)
# print(active.head())

#
# translator = google_translator()
#
# translations = {}
# unique_elements = active['role_name'].unique()
#
# print(unique_elements)
# for element in sorted(unique_elements):
#     # add translation to the dictionary
#     translation = translator.translate(element, lang_tgt='en')
#     print( element + " -> " + translation)
#     translations[element] = translation
#
# print(translations)
#
# active['role_name'].replace(translations, inplace = True)
#
# active.to_csv("active_en_sub.csv")
