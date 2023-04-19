#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#import language detector
from langdetect import detect
from googletrans import Translator
import re

# import libraries for text analysis
import nltk
from nltk import word_tokenize
# nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.corpus import stopwords

# import ml libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.metrics import brier_score_loss
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer


# In[2]:


# text preprocessing

# create function for cleaning the text

# parts of speech tagging
def get_wordnet_pos(pos_tagger):
    if pos_tagger.startswith('J'):
        return wordnet.ADJ
    elif pos_tagger.startswith('V'):
        return wordnet.VERB
    elif pos_tagger.startswith('N'):
        return wordnet.NOUN
    elif pos_tagger.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Use NOUN as the default tag


def text_processing(review):
    translator = Translator()
    if detect(review) != "en":
        review = translator.translate(review, dest="en").text
    
    # change all reviews into lower case
    review = review.lower()
    
    #remove all new line and tab character, as well as split words joined with hyphen into two(2)
    review = review.replace("\n", " ").replace("\t", " ").replace("-", " ").replace("show", "")
    
    #remove all punctuations
    review = re.sub(r'[^\w\s]', ' ', review)
    
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    
    #tokenize text
    tokens = word_tokenize(review)
    tokens = [token for token in tokens if token not in stop_words]
    
    #parts of speech tagging
    pos_tags = nltk.pos_tag(tokens)
    
    #lemmatize texts
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word, pos in pos_tags:
        wordnet_tag = get_wordnet_pos(pos)
        lem_word = lemmatizer.lemmatize(word, pos=wordnet_tag)
        lemmatized_words.append(lem_word)
    
    processed_review = " ".join(lemmatized_words)
       
    return processed_review

# build an iterable collection of strings required for TfidfVectorizer in spam_detector_pipeline
def text_preprocessing(rev):
    # function only takes a string or list, dataframe or series of strings
    
    # return a list of clean values for string argument. This is because the TfidfVectorizer
    list_ = []
    
    if type(rev) == str:
        list_ = [text_processing(rev)]
    
    else:
        list_ = [text_processing(i) for i in rev]
    
    return list_


# In[3]:


#create function to change tfidf sparse matrix to dense matrix
def sparse_to_dense(vector):
    return vector.toarray()

