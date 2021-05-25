Recommender System files

Preprocessing programm
- TranslateJob.py
    using files
    - previous_job_post.csv
    - active_job_post.csv
    output files
    - previous_en_sub.csv
    - active_en_sub.csv
- LabelEndcoding.py
    using files
    - previous_en_sub.csv
    - active_en_sub.csv
    output files
    - roles.pkl
    - role_name_LabelEncoder.pkl
    - sub_role_name_LabelEncoder.pkl
    - province_LabelEncoder.pkl
    - company_name_LabelEncoder.pkl

Modeling programm
- modeling.py
    using files
    - previous_en_sub.csv
    output files
    - previous_clustered.csv
    - job_kmodes_model.pkl

Prediction programm
- prediction.py
    using files
    - actve_en_sub.csv
    - job_kmodes_model.pkl
    output files
    - active_clustered.csv

Recommendation Generater
-searching.py
     using files
    - user_applications.py
    - previous_clustered.csv
    - active_clustered.csv
    output files
    - Recommendation.csv