from selenium import webdriver

cd = 'C:\\Users\\Riddhi\\Desktop\\chromedriver_win32\\chromedriver.exe'
# open google
driver = webdriver.Chrome(cd)

user_h = input("Enter the user handle of the profile: ")
url = 'https://www.instagram.com/'
url_p = url + user_h

# open the profile
driver.get(url_p)

try:
    image = driver.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
    image = driver.find_element_by_xpath('//img[@class="be6sR"]')

img_link = image.get_attribute('src')

path = "D:\\" + user_h + ".jpg"

import urllib.request

urllib.request.urlretrieve(img_link, path)

print("The profile pic has been downloaded at: " + path)