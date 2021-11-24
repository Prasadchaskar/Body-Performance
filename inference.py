import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('BodyPerformance\performance.pkl', 'rb'))
scaler = pickle.load(open('BodyPerformance\scalar.pkl', 'rb'))
encoder = pickle.load(open('BodyPerformance\encode.pkl', 'rb'))
class_names = ['A','B','C','D']

def predict(df):
    df = df[['age', 'gender', 'height_cm', 'weight_kg', 'body fat_%', 'diastolic','systolic', 'gripForce', 'sit and bend forward_cm', 'sit-ups counts','broad jump_cm']]
    df.gender = encoder.transform(df.gender)
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

age = 27
gender = 'M'
height_cm = 172.3
weight_kg = 75.14
fat = 21.3
diastolic = 80
systolic = 130
gripForce = 54.9
sit  = 18.4
ups = 60
jump_cm = 217

df = pd.DataFrame({ 
    'age':[age],
    'gender':[gender], 
    'height_cm':[height_cm], 
    'weight_kg':[weight_kg], 
    'body fat_%':[fat],
    'diastolic':[diastolic],
    'systolic':[systolic],
    'gripForce':[gripForce],
    'sit and bend forward_cm':[sit],
    'sit-ups counts':[ups],
    'broad jump_cm':[jump_cm]

})
print(predict(df))