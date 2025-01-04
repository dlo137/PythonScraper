from bs4 import BeautifulSoup
import requests
import json 

walmart_url = "https://www.walmart.com/ip/Ovios-L-Shape-Sectional-Sofa-Modern-Upholstered-Modular-Couch-for-Living-Room/5501723952?classType=VARIANT&adsRedirect=true"

# HEADERS is now correctly defined as a dictionary
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}

# Sends a GET request to the walmart_url (returns as an object)
response = requests.get(walmart_url, headers=HEADERS)

# Converts data from url to a string, stores in soup variable
soup = BeautifulSoup(response.text, 'html.parser')

# Finds the first script tag with the id of __NEXT_DATA__
script_tag = soup.find("script", id="__NEXT_DATA__")
data = json.loads(script_tag.string)

# Drills through the parsed JSON & props data to find price of product
print(data['props']['pageProps']['initialData']['data']['product']['priceInfo']['currentPrice']['price'])
