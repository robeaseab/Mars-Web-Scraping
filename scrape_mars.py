from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time



def init_browser():
    #Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    #Mars News
    #define path & set up browser
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
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
    mars_news = {"news_title": news_title, "news_p": news_p, "news_date":news_date}
    print(mars_news)
    #JPL Mars Space Images - Featured Image
    #define path & set up browser
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    #navigate to top image
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    #set up beautiful soup for new page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #extract top image url
    top_img = soup.find('img', class_="fancybox-image")
    top_img['src']
    top_img_url = 'https://www.jpl.nasa.gov' + top_img["src"]
    print(top_img_url)
    #Mars Weather
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    # Retrieve page with the requests module
    response = requests.get(url)    
    #create soup object
    soup = BeautifulSoup(response.text, 'html.parser')
    # Examine the results
    # print(soup.prettify())
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()
    print(mars_weather)
    #Mars Facts
    # URL of page to be scraped
    url = 'https://space-facts.com/mars/'
    # Retrieve page with the requests module
    response = requests.get(url)    
    #create soup object
    soup = BeautifulSoup(response.text, 'html.parser')
    # Examine the results
    # print(soup.prettify())
    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    tables = pd.read_html(url)
    tables
    # Use Pandas to convert the data to a HTML table string.
    mars_df = tables[0]
    mars_df
    html_table=mars_df.to_html(na_rep = " ",index = False, header=False)
    #html_table = html_table.replace('\n','')
    #html_table = html_table.replace("'",' ')
    print(html_table)
    #Mars Hemispheres
    #define path & set up browser
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(2)
    # products = soup.find('div', class_="product-section")
    items = soup.find_all('div', class_="item")

    titles = []
    img_urls = []

    hemisphere_image_urls = []


    for i in items:
            #scrape title
            img_title = i.find('h3').get_text()
            title = img_title.rsplit(' ', 1)[0]
            titles.append(title)
            
            #scrape hemisphere url
            detail = i.find('a')['href']
            detail_url = 'https://astrogeology.usgs.gov' + detail
            
            #got to detail_url
            browser.visit(detail_url)
            time.sleep(1)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            
            #scrape img_url
            downloads = soup.find('div', class_="downloads")
            ul = downloads.find('ul')
            li = ul.find_all('li')
            img = li[0]
            img_url = img.find('a')['href']
            img_urls.append(img_url)
            
            hemisphere_image_urls.append({"title": title, "img_url": img_url})

            #go back to original url
            browser.visit(url)

    print(hemisphere_image_urls)
    scrape_dict = {"mars_news": mars_news,  "top_img_url": top_img_url, "mars_weather": mars_weather, "html_table": html_table, "hemisphere_image_urls":hemisphere_image_urls}

    print(scrape_dict)
    return scrape_dict
