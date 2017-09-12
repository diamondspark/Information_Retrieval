from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def dropStopWords(text):
    text = re.sub("[^a-zA-Z]",' ',text)
    text = text.replace(' x ','')
##    text = text.replace('&#x20','')
    word_list = text.split(' ')
    filtered_words= word_list
##    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    filtered_words =[x for x in filtered_words if x!='']
    return (" ".join(filtered_words))
