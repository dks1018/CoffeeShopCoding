import webbrowser, sys, pyperclip, requests, bs4

# # sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# # # Check if command line args were passed
# # if len(sys.argv) > 1:
# #     # ['mapit.py', '870', 'Valencia', 'St.'] -? '870 Valencia St.'
# #     address = ''.join(sys.argv[1:])
# # else:
# #     address = pyperclip.paste()
    
# # webbrowser.open('https://www.google.com/maps/place/' + address)

# # make  a request to download the file
# try:
#     res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# # Check the Status code 401 symbolizes an error 200 means everything went okay
#     res.status_code
# # below shows how many characters are in the entire play brought in from the file above
#     print(len(res.text))
# # print first 500 letters
#     print(res.text[:500])
# # Raise for status shows any errors and doesnt show anything for success
#     print(res.raise_for_status())
# except:
#     print("An Error has occurs!")
# # Below shows a fake webpage to show the raise for status error

# try:
#     badRes = requests.get('https://automatetheboringstuff.com/mnhujnbvghjnbvgh')
# except:
#     print(badRes.raise_for_status())

# # open the remwo and juliet file and write binary
# playFile = open('RomeoAndJuliet.txt', 'wb')
# # download the text from the file in 100k increments
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)

# #end of file close the file
# print("This is the end of the program.")
# playFile.close()


# download the price information off of amazon webpage
try:
    res1 = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
    # webbrowser.open('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
except:
    print(res1.raise_for_status())

soup = bs4.BeautifulSoup(res1.text,'html.parser')
elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')

print(elems)
print(elems[0].text.strip())


res1 = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
soup = bs4.BeautifulSoup(res1.text,'html.parser')
elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')

print(elems)
