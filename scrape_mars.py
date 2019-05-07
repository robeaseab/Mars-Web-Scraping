from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    #find latest news information
    browser = init_browser()
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('div', class_="content_title")
    news_title = titles[0].text.strip()
    print(news_title)
    p_texts = soup.find_all('div', class_="article_teaser_body")
    news_p = p_texts[0].text.strip()
    print(news_p)
    dates = soup.find_all('div', class_="list_date")
    news_date = dates[0].text.strip()
    print(news_date)

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

if __name__ == "__main__":
    scrape()