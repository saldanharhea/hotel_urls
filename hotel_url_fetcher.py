from bs4 import BeautifulSoup
import requests
import pandas as pd




# BASE URLS
dubai_url= 'https://www.tripadvisor.in/Hotels-g295424-oa0-Dubai_Emirate_of_Dubai-Hotels.html'
sydney_url= 'https://www.tripadvisor.in/Hotels-g255060-oa0-Sydney_New_South_Wales-Hotels.html'
cali_url= 'https://www.tripadvisor.in/Hotels-g28926-oa0-California-Hotels.html'
cape_url = 'https://www.tripadvisor.in/Hotels-g1722390-oa0-Cape_Town_Western_Cape-Hotels.html'
bangkok_url = 'https://www.tripadvisor.in/Hotels-g293916-oa90-Bangkok-Hotels.html'

hotel_list=[]


# ---------------------------------------------------------START---------------------------------------------------------------------
def Processing(url):
	
	page2= requests.get(url)
	soup2 = BeautifulSoup(page2.content, 'html.parser')
	res = soup2.find_all('div',class_='listing_title')


	for x in res:
		hotel_name = x.text
		hotel_url = 'https://www.tripadvisor.in'+x.find('a')['href']
		
		hotel_list.append([hotel_name,hotel_url])
		

# -----------------------------------------------------------END-------------------------------------------------------------------		
		
		
		
		
def Generator(url,pgs,file_name):
	print "Processing "+str(pgs)+" Review Pages"
	page= requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')	
	no_of_pgs = soup.find('a',class_='last').text

	print no_of_pgs



	for x in range(0, (pgs-1)*30,30):
		
		new_val ='-oa'+str(x)
		
		urls=url.replace('-oa0',new_val)
		
		#print urls
		Processing(urls)
	print "Results will be found in "+ file_name		

	
	df = pd.DataFrame(hotel_list)
	df.columns = ['HOTEL_NAME', 'HOTEL_URL']
	df.to_csv(file_name, sep=',', encoding='utf-8')
	

	
	
	
	
#Generator(cali_url,32,'California.csv')
##Generator(sydney_url,8,'Sydney.csv')	
##Generator(dubai_url,19,'Dubai.csv')
#Generator(cape_url,59,'Cape.csv')
Generator(bangkok_url,104,'Bangkok.csv')