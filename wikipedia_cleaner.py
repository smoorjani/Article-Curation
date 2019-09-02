import re

############## WIKIPEDIA USE ONLY #################
def clean_wikipedia_text(article_text):
    # Remove wikipedia exponents
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    
    # Removing double spaces from double citations
    article_text = re.sub(r'\s+', ' ', article_text)
    return article_Text
