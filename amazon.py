from bs4 import BeautifulSoup
import requests
import random
import time

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

def search(product):
    url = f'https://www.amazon.in/s?k={product}'
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    response = requests.get(url,headers=headers)

    while(response.status_code != 200):
        time.sleep(2)
        response = requests.get(url,headers=headers)
        
    soup = BeautifulSoup(response.content,'html.parser')
    products = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vo8l48qglv7yn2w1wwffhqo34k s-latency-cf-section puis-card-border')
    if products:
        for product in products[:10]:
            try:
                name = product.find('span',class_='a-size-medium a-color-base a-text-normal').text.strip()
            except Exception as e:
                name = "N/A"
            try:
                price = product.find('span',class_='a-price-whole').text.strip()
            except Exception as e:
                price = "N/A"
            try:
                stars = product.find('i', {'data-cy': 'reviews-ratings-slot'}).find('span', class_='a-icon-alt').text.strip()
            except Exception as e:
                stars = "N/A"
            try:
                reviews = product.find('span',class_='a-size-base s-underline-text').text.strip()
            except Exception as e:
                reviews = "N/A"
            print(f"Product Name: {name}\nPrice: Rs. {price}\nRating: {stars}\nNumber of Reviews: {reviews}\n")
    else:
        print("Product was not found!")

if __name__ == "__main__":
    product = input("Enter name of product you wish to search: ")
    product = '+'.join(product.split())
    search(product)