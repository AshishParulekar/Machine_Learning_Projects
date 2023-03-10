import pickle
import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

saved_Data=pickle.load(open('Spam-mail-Detector/model.pkl','rb'))

Cv=saved_Data[1]
Log=saved_Data[0]
# function for Data processing 
def process(text):
  token=word_tokenize(text)
  stop_world=list(stopwords.words('english'))
  punctuation=set(string.punctuation)
  result=[]
  for i in token:
    if (i.strip() in stop_world) or (i.strip()in punctuation) :
      continue
    elif i=='Subject':
      continue
    else :   
      la=WordNetLemmatizer()
      i=la.lemmatize(i)
      result.append(i)
  strings=" ".join(result)
  return strings

#Function for Pridiction

def Spam_Detection(text):
    text=process(text)
    Vector=Cv.transform([text]).toarray()
    result=Log.predict(Vector)
    if(result==1):
        st.image('Spam-mail-Detector/SPAM.png')
        #return '** Spam **'
    else:
        st.image('Spam-mail-Detector/NO_SPAM.png')
        #return '** Not_Spam **'

#Streamlit_Code

st.title('SPAM MAIL DETECTOR !')
ip=st.text_input('Please enter the Subject')
bu=st.button('Check')
if bu==True:
    check=Spam_Detection(ip)
    






