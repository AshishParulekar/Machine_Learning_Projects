import streamlit as st
import pickle as pkl
import pandas as pd
#import requests
import bz2file as bz2
from IPython.display import HTML

# to load a cpmpressed Data 
def decompress_pickle(file):
     data = bz2.BZ2File(file,'rb')
     data = pkl.load(data)
     return data
    
simi=decompress_pickle('Movie-Recommender/Movie_Recommandtion_System.pbz2')

# to load Dataset
Movies=pkl.load(open('Data_Frame.pkl','rb'))


st.header('Movie Recommender System')
inp=st.selectbox('Select Movie Name ',Movies['title'])
yes=st.button('Recommend')
#A=HTML("<img src='http://image.tmdb.org/t/p/w185//btnl50ZDJDSCal2NLQIYWw0XxvH.jpg' style='height:100px;'>")
#st.write(A)

def recommendation_system(title_name):
    num=Movies[Movies['title']==title_name].index
    recommand=sorted(enumerate(simi[num[0]]),key=lambda x:x[1],reverse=True)
    recommand=recommand[1:6]
    Re=pd.DataFrame(recommand)
    Re=Re[0].values.tolist()
    result=Movies.iloc[Re,]
    return result

#['movie_id'].iloc[1]
    
Reco=recommendation_system(inp)
st.header('')
        
if yes==True:
    def Display():
        x=0
        while(x<5):
            col1,col2=st.columns((0.1,0.5))
            col2.write(' ')
            col2.write(' ')
            col2.write(Reco['title'].iloc[x])
            col1.write(HTML(Reco['poster_path'].iloc[x]))
            st.write(' ')
            x+=1
    Display()
            
        
        
        
