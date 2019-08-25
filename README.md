# Mission_to_Mars_WebScrapping

Requirements:
============
1) Mongod must be up and running.
mongodb data can be seen in figure: MONGO_DB_Load_details.png
2) Start app.py -> if the mongodb is empty -> the landing page will render empty.

3) If the collection in mongodb is empty - you will see an empty page. Figure: Initial_landing_page_mondb_empty.png
Please click on 'Scrape new data' button on the page to load the DB.

4) Scrape new data - will call scrape_data.py-which will pull data from different websites and render a landing page.Figure: Landing_page.jpg

5) Clicking on 'Mars hemisphere' link on the landing page will take you to the page where
all the four figures are rendered from the website. Figure:mars_hemisphere_page.png

6) template.html and mars_hemisphere.html are placed in /templates dir.

7) static/stylesheet1.css  and bootstrap style sheets have been used for this assignment.
