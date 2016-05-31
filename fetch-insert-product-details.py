#####################Author#############
#####################Melkis#################
import requests
import pymysql
from bs4 import BeautifulSoup

#conneting mysql database
db = pymysql.connect( host = 'localhost', user = 'root', passwd = 'almighty', db='melkis')
cursor = db.cursor()

#Amazon url containing the list of mobile phones to extract product_name, price, product_condition and offers
url = "http://www.amazon.com/s/ref=lp_2407747011_nr_p_n_feature_keywords_2?fst=as%3Aoff&rh=n%3A2335752011%2Cn%3A!2335753011%2Cn%3A7072561011%2Cn%3A2407747011%2Cp_n_feature_keywords_six_browse-bin%3A6787331011&bbn=2407747011&ie=UTF8&qid=1464610104&rnid=6787328011"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
lis_tags = soup.findAll("li", {"class" : "s-result-item celwidget "})

for li_tag in lis_tags:
	title_div = li_tag.find("div", {"class" : "a-row a-spacing-mini"})
	title_subdiv = title_div.find("div", {"class" : "a-row a-spacing-none"})
	title_tag = title_subdiv.find("a", {"class" : "a-link-normal s-access-detail-page a-text-normal"})
	spec_tag = li_tag.find("a", {"class" : "a-size-small a-link-normal a-text-normal"})

	product_name = title_tag.get('title')
	price = spec_tag.contents[0].text
	product_condition = spec_tag.contents[2]
	offers = spec_tag.contents[4].text
	
	print ("product_name = " + product_name)
	print ("price = " + price)
	print ("product_condition = " + product_condition)
	print ("offers = " + offers)

	#insert each row into table in mysql database
	sql = "insert into melkis.amazon(product_name, price, product_condition, offers) values(%s,%s,%s,%s)"
	cursor.execute( sql, (product_name, price, product_condition, offers))

cursor.close()
db.commit()   
#make sure the database saves the changes!
db.close()
print ("The data is inserted into table in mysql database!")
