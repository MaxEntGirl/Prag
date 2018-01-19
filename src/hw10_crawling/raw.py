import nltk
import urllib
import bs4
from bs4 import BeautifulSoup

def get_text(url):
    #TODO returns the list of clean paragraphs (no HTML markup) from the given URL

    list_text = []
    urlData = urllib.request.urlopen(url)
    html = urlData.read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    for paragraph in soup.find_all('p'):
        list_text.append(paragraph.get_text())
    return list_text

def make_text(raw):
    #TODO tokenize the stripped raw text and return an NLTK text object

    text = nltk.word_tokenize(raw)
    new_text = nltk.Text(text)
    return new_text

def stem_porter(tokens):
    #TODO returns list of stemmed tokens (use PorterStemmer)

    porter = nltk.PorterStemmer()
    stemmed = [porter.stem(t) for t in tokens]
    return stemmed

def stem_lancaster(tokens):
    #TODO returns list of stemmed tokens (use Lancaster Stemmer)

    lancaster = nltk.LancasterStemmer()
    steammed = [lancaster.stem(t) for t in tokens]
    return steammed

def lower(text):
    #TODO takes as input an NLTK text object "text" and returns list of lower case tokens

    list_token = []
    for token in text:
        list_token.append(token.lower())
    return list_token

def lemmatize(tokens):
    #TODO returns list of lemmas (use WordNetLemmatizer)

    wnl = nltk.WordNetLemmatizer()
    lemmatized = [wnl.lemmatize(t) for t in tokens]
    return lemmatized

def content(tokens):
    #return list of tokens without stopwords

    content = [x for x in tokens if x not in nltk.corpus.stopwords.words('english')]
    return content



    

