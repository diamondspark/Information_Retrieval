import sklearn
from utils_Clever_Heart_DL import dropStopWords
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB


def loadOutputDF():
    from Clever_Heart_DL import output_df

    output_df=output_df.drop(91)
    df= output_df

    for i in range(0,len(output_df)):
        df.iat[i,1]=dropStopWords(output_df.iat[i,1])

    df.to_csv('100.csv')
    return df

##df= loadOutputDF()
df = pd.read_csv('gt.csv')
clean_train_reviews=[]
clean_test_reviews=[]

for i in range(0,75):
    clean_train_reviews.append(df['repo'][i])
for i in range(76,99):
    clean_test_reviews.append(df['repo'][i])
    
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 
train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

### Random Forest
##clf = RandomForestClassifier(n_estimators = 100) 
##clf = clf.fit( train_data_features, df["hernia"][0:75] )


#Naive Bayes
clf = MultinomialNB()
clf = clf.fit(train_data_features, df["pleural effusion"][0:75])



result = clf.predict(test_data_features)
output = pd.DataFrame( data={"id":df["repo"][76:99], "pleural effusion":result} )
output.to_csv( "Bag_of_Words_model.csv")
