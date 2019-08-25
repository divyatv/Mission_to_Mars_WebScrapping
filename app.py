from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import json
import scrape_mars
import pandas as pd

# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')
#app = Flask(__name__, template_folder='/templates', static_folder='/static')

# Use PyMongo to establish Mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_page
#collection = db.mars_data
### delete the data if there are any to start clean
#db.collection.delete_many({})

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    #destination_data = db.collection.find_one()
    destination_data = db.collection.find_one({})
    if (destination_data!=None):
        ### Get the table from mongodb and fix it
        dict1=destination_data['mars_dataframe']
        import ast
        x=ast.literal_eval(dict1)
        #print(len(x))
        newdf=pd.DataFrame({})
        for i in x:
            newdf=newdf.append(pd.DataFrame([i]))
        import io
        newdf=newdf.rename(columns={"Mars": " ", "Mars - Earth Comparison": "Dimensions"})
        newdf=newdf.set_index(['Dimensions'])
        str_io=io.StringIO()
        newdf.to_html(buf=str_io, classes='table table-stripped')
        html_str=str_io.getvalue()
    
        # Return template and data
        return render_template("template.html", mars=destination_data, tables=[html_str], titles=newdf.columns.values)
    else:
        return render_template("template.html", mars=None, tables=[None], titles=None)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    ### Convert the dataframe into a dictionary to store in the database.
    mars_dataframe=scrape_mars.mars_facts()
    records=mars_dataframe.to_json(None, orient='records')
    mars_news=scrape_mars.mars_news_title()

    mars_data_dict={
            "fullresolimage": scrape_mars.background_image(),
            "mars_news_title":mars_news[0],
            "mars_news_content": mars_news[1],
            "mars_weather":scrape_mars.mars_weather(),
            "mars_dataframe":records,
            "mars_hemisphere_images":scrape_mars.mars_hemisphere_images()
        }

    db.collection.insert_one(mars_data_dict)

    # Redirect back to home page
    return redirect("/")

@app.route("/hemisphere")
def hemispshere():
  destination_data = db.collection.find_one({})   
  
  return render_template("mars_hemisphere.html", mars=destination_data)

if __name__ == "__main__":
    app.run(debug=True)
