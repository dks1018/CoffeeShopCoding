try:
    res1 = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/15932759945')
    print(res1)
except:
    res1.raise_for_status()