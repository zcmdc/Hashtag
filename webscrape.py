from apify_client import ApifyClient
import requests
import pandas
import re
import TimeStamp
import time
# # Initialize the ApifyClient with your Apify API token
# # Replace '<YOUR_API_TOKEN>' with your token.

client = ApifyClient("apify_api_2VcsUaEbS2waeYt9fxSBz8aM4xNqZR1ZwR04")

actor = client.actor("apify/instagram-hashtag-scraper")

# # Set up the hastag you want to use and how many results you want
run_input = {
  "hashtags": [
    "IUP"
  ],
  "resultsLimit": 10
 }

 #Sets up the fields you want displayed in the ouput

run_output = ["ownerUsername","timestamp","displayUrl"]

run = actor.call(run_input=run_input,max_items=20)
response = client.dataset(run["defaultDatasetId"])

#puts data into dataFrame on panda
dataSetdata = response.list_items(limit=5,fields=run_output).items
df = pandas.DataFrame(dataSetdata)
print(df)


#temp using csv to cut cost on calls for api 

#df = pandas.read_csv(df)


df_sorted = df.sort_values(by="timestamp",ascending=False)
#print(df_sorted)
index = df_sorted.head(1).index[0]




#gets the displayURl from the first item in the DataFrame and downloads the image
picture =df_sorted.loc[index,"displayUrl"]

img_data = requests.get(picture).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
#time.sleep(300)
