This Python script helps to webscrap the Amazon webpage. It fetches all Products information in the page like Product name, price, product_condition and offers. It also inserts those information into MySql database.

This script requires packages following packages:

requests - It is used to make GET request to the given URL of the Amazon webpage showing products.
pymysql - It is used for connecting to MySql and insert the products' details into the specified database tables.
BeautifulSoup - It is used to scrap/parse the HTML response and extract the required information.

How to run the script:
Place this Python script into a directory and navigate to that directory and execute the below command:
"python fetch-insert-product-details.py"
