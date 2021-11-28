
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

# initial opening to data
file_path = '/Users/shanematsushima/Dev/CS352_Final_Project/files/USvideos.csv'

df = pd.read_csv(file_path, delimiter=',', low_memory=False)
df = pd.DataFrame(df) # set df to a pandas dataframe 

fig = plt.subplots()

fig = df['channel_title'].value_counts().plot(kind='bar')

plt.show

# plt.bar(channel_np[:,0], channel_np[:,1])
# plt.show()