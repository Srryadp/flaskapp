import requests
from bs4 import BeautifulSoup

def scrape_books():
    
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    books = []
    page = 1
    
    while True:
    
        response = requests.get(base_url.format(page))
    
        if response.status_code != 200:
    
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
    
        book_list = soup.select('article.product_pod')
        
        if not book_list:
    
            break
        
        for book in book_list:
    
            title = book.h3.a['title']
            price = book.select_one('.price_color').text
            availability = book.select_one('.availability').text.strip()
            image_url = book.find('img')['src']
            image_url = 'http://books.toscrape.com/' + image_url.replace('../../', '')
            books.append({
                'title': title,
                'price': price,
                'availability': availability,
                'image_url': image_url
            })
        
        page += 1
    
    return books
