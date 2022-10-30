import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def onehot_feature(data):
    one_hot_vectorize = CountVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words = "english", binary=True)
    one_hot = one_hot_vectorize.fit_transform(data)
    df_onehot = pd.DataFrame(one_hot.todense())
    return df_onehot

def bow_feature(data):
    bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words = "english")
    bow = bow_vectorizer.fit_transform(data)
    df_bow = pd.DataFrame(bow.todense())
    return df_bow

def tfidf_feature(data):
    tfidf = TfidfVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words="english")
    tfidf_matrix = tfidf.fit_transform(data)
    df_tfidf = pd.DataFrame(tfidf_matrix.todense())
    return df_tfidf
