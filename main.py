##########################
# CS352 Final Project : Visualizing youtube Trends with Pandas and Streamlit
# Created by: Shane Matsushima
# Date: 11/29/2021
# This project was created to teach and present the power that Pandas and Streamlit have
# when it comes to visualizing and analyzing data sets. This project uses the youtube trend 
# dataset found on Kaggle as an example to what kind of data sets could be used in these data
# analysis projects.
##########################

# Import libararies used
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

# initial opening to data
file_path = '/Users/shanematsushima/Dev/CS352_Final_Project/files/USvideos.csv'

df = pd.read_csv(file_path, delimiter=',', low_memory=False)
df = pd.DataFrame(df) # set df to a pandas dataframe 

# global variables
bar_graph_width = 20
bar_graph_height = 20



# initial page config
st.set_page_config(
     page_title='CS352 Project',
     layout="wide",
     initial_sidebar_state="expanded",
)
plt.rcParams.update({'font.size': 10})


################## Main Function ##################
def main():

    cs_sidebar()
    cs_body()

    return None


################## Sidebar ##################
def cs_sidebar():
    global bar_graph_width
    global bar_graph_height

    st.sidebar.header('Sidebar Widgets')
    st.sidebar.subheader('Adjust graph size')

    bar_graph_width = st.sidebar.slider("bar graph width", 1, 50, 20)
    bar_graph_height = st.sidebar.slider("bar graph hieght", 1, 50, 20)

    return None


################## Main Body of Page ##################
def cs_body():

    # Display logo
    st.image('/Users/shanematsushima/Dev/CS352_Final_Project/images/data_photo_header.png')
    # display title
    st.title('CS352 Final Project (Streamlit + Pandas)')

    #display text about the project
    st.markdown("""This projects purpose is to showcase the different applications of utilizing streamlit and pandas. 
                   The data being used as an example comes from video data in the US for YouTube videos. *The data used in this
                   project was from a dataset taken from 2017-2018. 
                   """)
    st.header('Data Visualization')

    st.subheader('Channel Video Count')

    st.markdown("""The following graph and dataframe displayed represent the number of videos 
                    each channel in this data set has produced over the time that the dataset
                    was recorded. Due to the size of the data set, the graph will showcase the top 5 channels.
                """)

    ################## Channel Count ##################

    channel_data = pd.DataFrame()

    channel_name= df['channel_title'].value_counts().keys().tolist()
    channel_count = df['channel_title'].value_counts().tolist()

    channel_data['channel_name'] = channel_name
    channel_data['channel_count'] = channel_count

    st.dataframe(channel_data)  

    fig, ax = plt.subplots(figsize=(bar_graph_width, bar_graph_height))
    ax.bar(channel_data['channel_name'].head(5), channel_data['channel_count'].head(5),width=0.5)

     

    st.pyplot(fig)

    ##############
    # The following analysis was found using the link bellow:
    # https://www.kaggle.com/raj5kumar5/video-statistics
    # This source was used as another way to analyze the csv data given
    ##############


    st.subheader('Video Popularity Analysis')
    st.markdown(""" The following data being visualized will be the top 10
                    most popular videos in the dataset using a popularity formula 
                    that follows: Popularity = (views + likes + comments - dislikes ) / 1000000.
                """)

    ################## Popularity Analysis ##################

    df['popularity'] = (df['views'] + df['likes'] + df['comment_count'] - df['dislikes']) / 1000000

    st.write(df.sort_values('popularity', ascending=False).head(10))

    st.subheader('By Category')
    st.markdown(""" The following data being visualized is top 5 videos in each category.
                    This will be utilizing the popularity formula as the prior analysis of total popularity. 
                """)
    
    top_cat_vid = (df[['category_id', 'channel_title', 'views', 'dislikes', 'comment_count', 'popularity']].sort_values('popularity', ascending=False).groupby('category_id'))
    top_cat_vid = top_cat_vid.head(5).sort_values(['category_id', 'popularity'], ascending=[True, False]).copy()
    top_cat_vid.reset_index(drop=True, inplace=True)

    st.dataframe(top_cat_vid)


    return None



if __name__ == '__main__':
    main()








