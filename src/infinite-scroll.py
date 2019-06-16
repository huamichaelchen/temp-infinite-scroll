import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup as bs

binary = FirefoxBinary('/usr/lib/firefox')
#browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Firefox()

browser.get("https://scrollmagic.io/examples/advanced/infinite_scrolling.html")

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")

match = False
while(match == False):
    lastCount = lenOfPage
    '''
      Play around with the sleep time depending on your internet speed. 
      For instance, the default site we are testing in here seems to be really infinite... But if you use 1 seconds or even smaller number, it will race to the end
      before it load the content, then you would find some outputs in the ../output folder.
    '''
    time.sleep(1)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

print("===> Scroll ends....")

source_data = browser.page_source
source_data_file = open('../output/source_data_file.txt', 'w')
source_data_file.write(source_data)
source_data_file.close()

bs_data = bs(source_data, features='html.parser')
bs_data_file = open('../output/bs_data_file.txt', 'w')
bs_data_file.write(str(bs_data))
bs_data_file.close()
