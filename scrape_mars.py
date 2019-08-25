from bs4 import BeautifulSoup
import requests
from splinter import Browser


def mars_news_title():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://mars.nasa.gov/#news_and_events'

    baseurl='https://mars.nasa.gov'
        
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # with open("mars_news.html", "w", encoding='utf-8') as file:
    #     file.write(str(soup))
        
    # with open("mars_news.html", "r", encoding='utf-8') as file:
    #     soup=file.read()
        
    soup = BeautifulSoup(html, 'html.parser')
        
    latest_news_mars = soup.find('ul', class_='item_list list_view')
    # print(latest_news_mars)
    #news_title=latest_news_mars.find('div', {'class':'list_image'}).find('img')['alt']
    
    new_title_changed_page=latest_news_mars.find('h3', {'class':'title'}).find('a')['href']
    news_p=latest_news_mars.find('h3', {'class':'title'}).find('a').get_text()
       
    next_url=baseurl + new_title_changed_page
    print(next_url)
    ################### taking the content #######################
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    browser.visit(next_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_news_content=soup.find('div', {'class':'wysiwyg_content'}).find('p').get_text()
    #.get_text()

    return_list=[mars_news_content,news_p]
    return(return_list)



def background_image():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
            
    mars_featured_picture=soup.find('article')        

    mars_featured_picture_jpg=mars_featured_picture.get('style')
    url=mars_featured_picture_jpg.split("(")
    url1=url[1].split(");")
    
    import re
    image_url=url1[0].replace("'", "")
    #print(image_url)
    ### JPL Mars Space Images - Featured Image
    ## Build the url for mars image
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url
    #print("featured_image_url for mars=",featured_image_url)

    return (featured_image_url)

def mars_weather():
        #### Mars weather
    #https://twitter.com/marswxreport?lang=en
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    import requests
    from splinter.exceptions import ElementDoesNotExist
       
    mars_weather=soup.find_all('p', class_='TweetTextSize')
    mars_weather=mars_weather[0].get_text()
    import re
    mars_weather=re.sub("InSight", " ",mars_weather)
    mars_weather=re.sub("hPapic.twitter.com/MhPPOHJg3m", " ",mars_weather)
    return(mars_weather)


def mars_facts():
        ### Mars Facts - fetch mars facts as a table.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://space-facts.com/mars/'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_facts=soup.find(id='text-2')
  # print(mars_facts)
    import pandas as pd
    import numpy 
    # type(mars_facts)
    mars_dataframe = pd.read_html(mars_facts.prettify())[0]
    #mars_dataframe=mars_dataframe.drop(columns=['Earth'])
    return(mars_dataframe.head(15))

def mars_hemisphere_images():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #with open("mars_cerberus_hemisphere.html", "w", encoding='utf-8') as file:
        #file.write(str(soup))
    mars_ch=soup.find_all('a', class_="itemLink")    
    base_url_image='https://astrogeology.usgs.gov'
  
  #### I could use a for loop but had to deliver the cup cake by today so all the drama below:
    cerberus=mars_ch[0]
    cerberus_url=cerberus.find('img')['src']
    
    schiaparelli=mars_ch[2]
    schiaparelli_url=schiaparelli.find('img')['src']
    
    syrtis_major=mars_ch[4]
    syrtis_major_url=syrtis_major.find('img')['src']
    
    valles_marineris=mars_ch[6]
    valles_marineris_url=valles_marineris.find('img')['src']

    cerberus=base_url_image+cerberus_url
    schiaparelli=base_url_image+schiaparelli_url
    syrtis_major=base_url_image+syrtis_major_url
    valles_marineris=base_url_image+valles_marineris_url

    mars_hemisphere= [cerberus,schiaparelli,syrtis_major, valles_marineris]
     
    return(mars_hemisphere)



  