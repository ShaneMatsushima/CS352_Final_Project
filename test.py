import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

# initial opening to data
file_path = '/Users/shanematsushima/Dev/CS352_Final_Project/files/USvideos.csv'

df = pd.read_csv(file_path, delimiter=',', low_memory=False)
df = pd.DataFrame(df) # set df to a pandas dataframe 

# global variables
bar_graph_width = 0
bar_graph_height = 0

# initial page config
st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

def cs_sidebar():
    global bar_graph_width
    global bar_graph_height
    st.sidebar.header('Put files here (or something)')
    bar_graph_width = st.sidebar.slider("bar graph width", 1, 50, 1)
    bar_graph_height = st.sidebar.slider("bar graph hieght", 1, 50, 1)
    return None

def cs_body():
    # display title
    st.title('CS352 Final Project (Streamlit + Pandas)')

    #display text about the project
    st.markdown("""This projects purpose is to showcase the different applications of utilizing streamlit and pandas. 
                   The data being used as an example comes from video data in the US for YouTube videos.
                   """)
    st.header('Data Visualization')

    st.subheader('Channel Video Count')

    st.markdown("""The following graph and dataframe displayed represent the number of videos 
                    each channel in this data set has produced over the time that the dataset
                    was recorded. 
                """)

    channel_data = pd.DataFrame()

    channel_name= df['channel_title'].value_counts().keys().tolist()
    channel_count = df['channel_title'].value_counts().tolist()

    channel_data['channel_name'] = channel_name
    channel_data['channel_count'] = channel_count

    st.write(channel_data)  

    fig, ax = plt.subplots(figsize=(bar_graph_width, bar_graph_height))
    ax.bar(channel_name, channel_count,width=1.0, tick_label='vertical')

    st.pyplot(fig)





    # st.bar_chart(get_channel_count)
    # st.write(df.loc[df['views'] == df['views'].max()])



    return None


def get_likes():
    return df['likes'].sort_values()

if __name__ == '__main__':
    main()








