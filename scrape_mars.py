from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    #find news
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('div', class_="content_title")
    news_title = titles[0].text.strip()
    print(news_title)

    #top image
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    top_img = soup.find('img', class_="fancybox-image")
    top_img['src']
