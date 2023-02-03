# -*- coding: utf-8 -*-

!pip install streamlit
!pip install ipython==7.9.0
!pip install pyngrok

#Importing all necessary libraries 
import streamlit as st
import numpy as np
import pandas as pd
from tqdm import tqdm
import re

import warnings
warnings.filterwarnings("ignore")
import pickle

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk import ne_chunk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#Download necessary nltk kit
import nltk
nltk.download('punkt') 
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

# Title
st.title(" Text summarization with recommended suggestion based on sentiment analysis and text analytics")

# Create Data
data = "FF_dataset.csv"


# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(data):
    df = pd.read_csv(data)
    return df

df = explore_data(data)



