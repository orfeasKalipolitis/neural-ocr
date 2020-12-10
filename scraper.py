import urllib
from bs4 import BeautifulSoup as soup
import requests
import webbrowser
import os
import time
import sys
import wget

# TODO: Use a configuration file instead of hardcoding these values
DL_FOLDER = 'downloadedFonts'
lastCall = 0
wt = 0.1

print('We are about to download all fonts from 1001fonts.com :)')

# Create DL folder in case it doesn't exist
try:
    os.mkdir(DL_FOLDER)
    print('DL folder created')
except FileExistsError:
    print('DL folder already exists')

for i in range(1, 322, 1):
    url = 'https://www.1001fonts.com/handwritten-fonts.html?page=' + str(i)
    
    # get response from 1001fonst
    try:
        now = time.time()
        if (now - lastCall) < wt:
            print('Sleeping for ' + str(wt - (now - lastCall)) + ' seconds')
            time.sleep(wt - (now - lastCall))
        print('Getting url: ' + url + '\n')
        response = requests.get(url)
        lastCall = time.time()
    except requests.exceptions.RequestException as e:
        print('\n1001fonts is not answering the request')
        print(str(type(e)))
        print('Exiting now')
        sys.exit(1)
    except:
        print('\n1001fonts is not answering, we have no clue why')
        print('Exiting now')
        sys.exit(1)

    # use beautiful soup to process the results page
    web_soup = soup(response.text, 'html.parser')

    # download the fonts from the links foudn on the page
    for dlLink in web_soup.find_all(class_='obtrusive'):
        url2download = 'https:' + dlLink['href']
        try:
            wget.download(url2download, DL_FOLDER)
            print('\n')
        except:
            print('Had a problem with page: ' + str(i))
            print('URL was: ' + url2download)
            print('Trying to continue')
            continue

    
print('Done downloading all fonts from the website :)')   