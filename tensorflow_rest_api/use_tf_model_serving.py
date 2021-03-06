# -*- coding: utf-8 -*-
"""use_tf_model_serving.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1czpTrfmv9vLqgsqEb9pU-otry4sfCdXa
"""

import json
import requests

import numpy as np

!wget https://github.com/futurexskill/ml-model-deployment/raw/main/sc.pickle

import pickle

scaler_colab = pickle.load(open('sc.pickle','rb'))

scaler_colab.transform(np.array([[20,40000]]))

scaler_colab.transform(np.array([[42,50000]]))

url = 'http://35.238.92.68:8501/v1/models/customer_behavior_model:predict'

request_data = json.dumps({"signature_name": "serving_default",
                   "instances": [[-1.43318661, -0.47466685],[0.2345214460208433, 0.03675871227617118]]
})

json_response = requests.post(url,request_data)

print (json_response.text)

