# Mars-Web-Scraping
# Mission to Mars


In this project I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
Skills Used: 
•	MongoDB
•	Flask
•	Python: BeautifulSoup, Pandas, and Requests/Splinter in a Jupyter Notebook
•	Web design: HTML, CSS, Bootstrap

The following outlines what I did:

I completed scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.  See the Jupyter Notebook file called `mission_to_mars.ipynb` which I used to complete all of my scraping and analysis tasks. The following outlines what you need to scrape.

My web scraper performed the following actions: 
* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables.

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).  Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable. 

* Visited the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page. It then saved the tweet text for the weather report as a variable called `mars_weather`.

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Used Pandas to convert the data to a HTML table string.

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and obtained high resolution images for each of Mar's hemispheres. The web scraper clicked each of the links to the hemispheres in order to find the image url to the full resolution image.  Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the variable keys.  Appended the dictionary with the image url string and the hemisphere title to a list. This list contained one dictionary for each hemisphere.

## Deployed using MongoDB and Flask Application

Used MongoDB with Flask templating and created a new HTML page that displayed all of the information that was scraped from the URLs above.

* Converting your Jupyter notebook into a Python script with a function called `scrape` that executed all of mye scraping code from above and returned one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that imported my python script and called my `scrape` function.

  * Storee the return value in Mongo as a Python dictionary.

* Created a root route `/` that queried my Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file (`index.html`) that took the Mars data dictionary and displayed all of the data in the appropriate HTML elements. 

See a screenshot of my project below: 



![](https://raw.githubusercontent.com/robeaseab/Mars-Web-Scraping/master/Screenshot%20Mars%20Scrape.jpg)
