import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('performance.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
encoder = pickle.load(open('encode.pkl', 'rb'))
class_names = ['A','B','C','D']

def predict(df):
    df = df[['age', 'gender', 'height_cm', 'weight_kg', 'body fat_%', 'diastolic','systolic', 'gripForce', 'sit and bend forward_cm', 'sit-ups counts','broad jump_cm']]
    df.gender = encoder.transform(df.gender)
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output
