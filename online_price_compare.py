from selenium import webdriver
cd='C:\\Users\\Riddhi\\Desktop\\chromedriver_win32\\chromedriver.exe'

browser=webdriver.Chrome(cd) #cd is the path to chromedriver.exe


print("Checking on Amazon...........")

# give the product link on amazon
browser.get('https://www.amazon.in/Test-Exclusive-750/dp/B078BN55WZ/ref=sr_1_1?crid=3OEL6DKYVV850&dchild=1&keywords=one%2Bpluse8%2Bpro%2Bmobile&qid=1597315955&sprefix=one%2Caps%2C290&sr=8-1&th=1')
pe=browser.find_element_by_id('priceblock_ourprice')
pr=pe.get_attribute('textContent')
pr=pr[2:]
pl=pr.split(',')

price_a=''
for i in pl:
	price_a+=i

price_a=float(price_a)

print("The price in Amazon is " + str(price_a))


print("Checking on Flipkart...........")

# give the product link on flipkart
browser.get('https://www.flipkart.com/oneplus-8-pro-onyx-black-256-gb/p/itm4dcbd336cdd4f?pid=MOBFU897DEZ4SZ9X&lid=LSTMOBFU897DEZ4SZ9X3XJTWH&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=b0ba3921-ac6d-468a-8282-a92473384b97.MOBFU897DEZ4SZ9X.SEARCH&ppt=sp&ppn=sp&ssid=scq9tf7ek00000001597226823165&qH=5894ab4766000b8e')
pe=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
pr=pe.get_attribute('textContent')


pr=pr[1:]
pl=pr.split(',')

price_f=''
for i in pl:
	price_f+=i

price_f=float(price_f)

print("The price in Flipkart is " + str(price_f))

if (price_a<price_f):
	print("The price is less on Amazon. But from there.")

elif (price_f<price_a):
	print("The price is less on Flipkart. But from there.")

else:
	print(" The price is same on Amazon and Flipkart. You can buy from any of them.")