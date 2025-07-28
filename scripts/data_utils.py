# datat utility script

import os
import kagglehub
from PIL import Image

path = kagglehub.dataset_download("nih-chest-xrays/data")

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

# function to view images based on index
def view_img(file_path, index):
    return Image.open(file_path.iloc[index,0])