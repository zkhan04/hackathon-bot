from bs4 import BeautifulSoup 
import requests

def getRestaurants(cuisine, location):
    # Construct the URL string
    url = f'https://www.zabihah.com/search?k={cuisine}&l={location}'

    # Get HTML content
    html_text = requests.get(url).text

    # Parse HTML content
    soup = BeautifulSoup(html_text, 'html.parser')

    title = soup.find('div', class_ = 'titleBS')
    a = title.find('a')
    print(a.text)