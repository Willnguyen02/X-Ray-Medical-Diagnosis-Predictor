# create labels scripts

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import warnings
warnings.filterwarnings("ignore")


column_order=[
    'image_index',
    'Atelectasis',
    'Cardiomegaly',
    'Consolidation',
    'Edema',
    'Effusion',
    'Emphysema',
    'Fibrosis',
    'Hernia',
    'Infiltration',
    'Mass',
    'No Finding',
    'Nodule',
    'Pleural_Thickening',
    'Pneumonia',
    'Pneumothorax',
    'follow_up_number',
    'patient_id',
    'patient_age',
    'patient_gender',
    'view_position'
]

labels=[
    'Atelectasis',
    'Cardiomegaly',
    'Consolidation',
    'Edema',
    'Effusion',
    'Emphysema',
    'Fibrosis',
    'Hernia',
    'Infiltration',
    'Mass',
    'No Finding',
    'Nodule',
    'Pleural_Thickening',
    'Pneumonia',
    'Pneumothorax'
]

# y = target variable
# X = features

def create_labels(X, y):
    mlb = MultiLabelBinarizer()

    y_split = y.str.split('|')
    y_encoded = mlb.fit_transform(y_split)
    classes = mlb.classes_

    encoded_df = pd.DataFrame(columns=classes, data=y_encoded)
    labeled_df = X.join(encoded_df,how="inner").drop(columns=['original_img_height', 'img_pixel_spacing_x', 'img_pixel_spacing_y'], axis=1)
    labeled_df = labeled_df.reindex(columns=column_order)
    labeled_df[labels] = labeled_df[labels].fillna(0).astype(int) #fill missing data with 0

    return labeled_df



