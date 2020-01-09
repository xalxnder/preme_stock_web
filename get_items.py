import requests
import json
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
init()

supreme = requests.get("https://www.supremenewyork.com/shop/all")

# List of links to the items currently in stock
item_links = []
# Details of the items in stock.
item_details = []

filename = 'items.json'

# The Beautiful Soup Object
soup = BeautifulSoup(supreme.content, 'html.parser')
all_items = soup.select('.inner-article')

# Loop over items on the home page.
# If item is in stock, append the link to the list of item_links, above.
for item in all_items:
    link_href = item.find('a').attrs['href']
    if item.text != 'sold out':
        item_links.append(f"https://supremenewyork.com{link_href}")


def get_item_details():
    with open(filename, 'w') as f:
        for link in item_links[:9]:
            new_supreme = requests.get(link)
            more_soup = BeautifulSoup(new_supreme.content, 'html.parser')
            actual_item = more_soup.select('#container')
            for description in actual_item:
                item_name = description.find(id='details').find('h2').text
                color = description.find(id='details').find('p').text
                image = description.find('img')['src']
                # print(Fore.GREEN + f"Item:{item_name}\n Color: {color}\n {link}\n")
                item_details.append(
                    {"Item": item_name, "Color": color, "Link": link, "Image": image})
        json.dump(item_details, f, indent=4)
        print(item_details)


get_item_details()
