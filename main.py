import requests
from urllib.parse import urlparse
import os
import argparse
from dotenv import load_dotenv


def shorten_link(token, url):
    payload = {
        "long_url": url,
    }
    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks", 
        json=payload, 
        headers=headers
    )
    response.raise_for_status()
  
    return response.json()['link']


def count_clicks(token, link):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_url = urlparse(link)

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary",
        headers=headers
    )
    response.raise_for_status()
  
    return f'Кол-во переходов по ссылке: {response.json()["total_clicks"]}'


def is_bitlink(token, url):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_url = urlparse(url)

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}",
        headers=headers,
    )
        
    return response.ok
        
     
def main():
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    
    try:
        if is_bitlink(bitly_token, args.url):
            print(count_clicks(bitly_token, args.url))
        else:
            print(shorten_link(bitly_token, args.url))
    except requests.exceptions.HTTPError as error:
        print(error)
    

if __name__ == '__main__':
    main()