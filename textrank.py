# Credits to Usman Malik for his TextRank Algorithm
import nltk
import re
import clipboard
from scraper import get_article
from wikipedia_cleaner import clean_wikipedia_text

article_link = clipboard.get_clipboard()
article_text = get_article(article_link)

if 'wikipedia' in article_link:
    article_text = clean_wikipedia_text(article_text)

nltk.download('stopwords')

# Formatted for weightings
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  

# Tokenizing our text
sentence_list = nltk.sent_tokenize(article_text)  

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
            
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    
sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

import heapq  
summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary)  
