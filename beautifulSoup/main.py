from bs4 import BeautifulSoup

html = '''
    
    <!DOCTYPE html>
        <html>
        <head>
            <title>Example HTML</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p id='paragraph'>A simple HTML page for testing web scraping with BeautifulSoup.</p>
            <a class = 'link' href='www.miuul.com' target ='blank' aria-label='Miuul (0pens Miuul Page)'>Click</a>
            <ul>
                <li class='list-item'>item 1</li>
                <li class='list-item'>item 2</li>
            <ul>
            <li>Outsider 2</li>
        </body>
        </html>

'''

soup = BeautifulSoup(html, 'html.parser')

title = soup.title
type(title)
title.text
title.string

print(soup.prettify())

soup.ul
soup.li

soup.a
soup.find('a',attrs={'class':"link"})

soup.find_all('li')

li_elements = soup.find_all('li',attrs={'class':'list-item'})
li_elements
li_elements[-1]



import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.example.com')
result.status_code
html = result.content
soup = BeautifulSoup(html,'html.parser')
soup.find('h1')




































