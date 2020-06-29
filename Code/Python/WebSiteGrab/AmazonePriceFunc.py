import webbrowser, sys, pyperclip, requests, bs4

def getAmazonPrice(productURL):   
    try:
        res = requests.get(productURL)
    except:
        print(res.raise_for_status())

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    try:
        elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    except:
        print("There was an error in the parser!")
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The Price of Automate the boring stuff is: {0}'.format(price))

# Try a webscraper for a fun site xkcd.com