from selenium import webdriver
import os
import ast
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup

chromePath = r'D:\chromeSel\chromedriver.exe'

driver = webdriver.Chrome(chromePath)

URL = "https://www.google.com/search?biw=1428&bih=937&tbm=isch&sxsrf=ACYBGNQcrfVJ_dphrOm2piDU_U8YkR1z5g%3A1568393896697&sa=1&ei=qMp7XdGbKoWTwgOA0qygCg&q=potholes+road&oq=potholes+road&gs_l=img.3...0.0..796927...0.0..0.0.0.......0......gws-wiz-img.X0CA6xYDMRU&ved=0ahUKEwjRj9LIos7kAhWFiXAKHQApC6QQ4dUDCAY&uact=5"


def getURLs(URL):
    driver.get(URL)
    page = driver.page_source
    # print(page)

    soup = Soup(page, 'lxml')

    ourURLs = []

    desiredURLs = soup.findAll('div', {'class': 'rg_meta notranslate'})

    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)

    return ourURLs


def save_images(URLs, dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    for i, url in enumerate(URLs):
        savePath = os.path.join(dir, '{:06}.jpg'.format(i))
        try:
            ulib.urlretrieve(url, savePath)
        except:
            print("error")


save_images(getURLs(URL), "dataset")
