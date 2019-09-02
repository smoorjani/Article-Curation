import bs4 as bs  
import urllib.request  




def get_article(site='https://www.brainpickings.org/2016/08/16/friendship/'):
    # Scraping data using urllib and then parsing using beautifulsoup (by paragraph)
    scraped_data = urllib.request.urlopen(site)  
    article = scraped_data.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')

    # Transfer into a string
    article_text = ""
    for p in paragraphs:  
        article_text += p.text

    return article_text
