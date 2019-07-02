import time
import datetime
from bs4 import BeautifulSoup 
import PP_Creds
from Driver import *

username = PP_Creds.login['consumer_username']
password = PP_Creds.login['consumer_secret']

url = 'https://www.paypal.com/ca/signin'
	

driver.get(url)



#To Login to PayPal

driver.find_element_by_id('email').send_keys(username)
time.sleep(2)
driver.find_element_by_id('btnNext').click()
time.sleep(2)
driver.find_element_by_id('password').send_keys(password)
time.sleep(2)
driver.find_element_by_id('btnLogin').click()

#To Access Report Page
time.sleep(12)

reportURL = 'https://business.paypal.com/merchantdata/reportHome'

driver.get(reportURL)

time.sleep(10)




#to activity download
try: 
	driver.find_element_by_xpath('//*[@id="dlogNav"]').click()
except Exception as d:
	raise d

try: 
	time.sleep(15)
	driver.find_element_by_xpath('//*[@id="dlogNav"]').click()
except Exception as f:
	raise f

time.sleep(5)


#date range selection
driver.find_element_by_xpath('//*[contains(@id, "react-datepicker-dropdown")]/button').click()

time.sleep(1)
#select yesterday

driver.find_element_by_xpath('//*[contains(@id, "react-datepicker-dropdown")]/ul/li[3]/a').click()

time.sleep(1)

#select create report

driver.find_element_by_xpath('//*[@id="dlogSubmit"]').click()


time.sleep(10)
value = driver.find_element_by_xpath('//*[@id="pastHistory"]/table/tbody/tr[1]/td[5]').text.strip()

if value != "Download":
	while value != "Download":
		time.sleep(90)
		driver.refresh()
		time.sleep(15)
		driver.find_element_by_xpath('//*[@id="dlogNav"]').click()
		time.sleep(15)			
		value = driver.find_element_by_xpath('//*[@id="pastHistory"]/table/tbody/tr[1]/td[5]').text.strip()

driver.find_element_by_xpath('//*[@id="download_0"]').click()

#sign out of Paypal
driver.find_element_by_xpath('//*[@id="merchant-header-main-wrapper-internal"]/div[1]/div/div[2]/div/a[3]').click()

time.sleep(1)
driver.quit()

# To relocate the file from OS to Google Drive

from datetime import datetime, timedelta
import xlrd
import csv
import shutil
import os.path

exists = os.path.isfile(r'G:\My Drive\'OLD_CSV.CSV')
try:
	if  exists:
	 	os.remove(r'G:\My Drive\'OLD_CSV.CSV')
except Exception as e:
	raise e

# Identifies PayPal Default FileName
FileName = r"C:\Users\Matt\Downloads\Download.CSV"

shutil.move(FileName, r'G:\My Drive\'OLD_CSV.CSV')

