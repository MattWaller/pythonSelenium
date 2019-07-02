import time
from datetime import datetime, timedelta
import os
import QBO_Creds

# define file suffixes

SuffixOne = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d_')
SuffixTwo = datetime.strftime(datetime.now(), '%m-%d-%Y')

# define exe script variables

bCAD = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\CAD_TRX.exe"
bUSD = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\USD_TRX.exe"
bGBP = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\GBP_TRX.exe"
bEUR = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\EUR_TRX.exe"
bRUB = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\RUB_TRX.exe"
bMYR = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\MyScripts\AutoIt\MYR_TRX.exe"


# determine if the file exists

CAD = r"G:\My Drive\PaypalCSVs\CAD\CAD_Transactions_" + SuffixTwo + ".csv"
CADexist = os.path.isfile(CAD)


EUR = r"G:\My Drive\PaypalCSVs\EUR\EUR_Transactions_" + SuffixTwo + ".csv"
EURexist = os.path.isfile(EUR)


GBP = r"G:\My Drive\PaypalCSVs\GBP\GBP_Transactions_"+ SuffixTwo + ".csv"
GBPexist = os.path.isfile(GBP)


USD = r"G:\My Drive\PaypalCSVs\USD\USD_Transactions_" + SuffixTwo + ".csv"
USDexist = os.path.isfile(USD)


RUB = r"G:\My Drive\PaypalCSVs\RUB\RUB_Transactions_"+ SuffixTwo + ".csv"
RUBexist = os.path.isfile(RUB)


MYR = r"G:\My Drive\PaypalCSVs\MYR\MYR_Transactions_" + SuffixTwo + ".csv"
MYRexist = os.path.isfile(MYR)


PHP = r"G:\My Drive\PaypalCSVs\PHP\PHP_Transactions_" + SuffixTwo + ".csv"
PHPexist = os.path.isfile(PHP)


# Only run script if flag == true (one of the files above must exist in order to run script)
flag = False

if CADexist == True:
	flag = True 

elif USDexist == True:
	flag = True
elif GBPexist == True:
	flag = True
elif EURexist == True:
	flag = True
elif RUBexist == True:
	flag = True
elif MYRexist == True:
	flag = True
elif PHPexist == True:
	flag = True


# Start the Selenium webscript
try:
	if flag == True:
		
		# Pass through Driver preferences
		from Driver import *
		
		# set username and password variables
		username = QBO_Creds.login['consumer_username']
		password = QBO_Creds.login['consumer_secret']


		currenturl = 'https://c5.qbo.intuit.com/qbo5/login?&useNeo=true&region=CA'

		driver.get(currenturl)


		# login to QuickBooks Online
		driver.find_element_by_id('ius-userid').send_keys(username)
		time.sleep(1)
		driver.find_element_by_id('ius-password').send_keys(password)
		time.sleep(1)
		driver.find_element_by_id('ius-sign-in-submit-btn').click()

		time.sleep(5)


		#Go to Companies accounting ID Page [Accountant Requirement] --- this is not required for individuals who do not have an accounting account with Quickbooks Online -- Skip this step
		driver.get('https://c5.qbo.intuit.com/app/switchCompany?companyId=')#<-- Remove this parenthesis && CompanyID goes here')

		time.sleep(5)


		# navigate to bank upload location
		driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		time.sleep(5)


		# If Canadian file exists in Google Drive run the uploading script

		try:
			if CADexist:
					time.sleep(5)
					

					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload CAD File
					os.system(bCAD)

					time.sleep(5)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1040 PayPal CAD')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as d:
			raise d

		# If American file exists in Google Drive run the uploading script

		try:
			if USDexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload USD File
					os.system(bUSD)

					time.sleep(5)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1045 PayPal USD')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as e:
			raise e

		# If Euro file exists in Google Drive run the uploading script
		
		try:
			if EURexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload EUR File
					os.system(bEUR)

					time.sleep(3)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1050 PayPal EUR')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as e:
			raise e

		# If GBP file exists in Google Drive run the uploading script
		try:
			if GBPexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload GBP File
					os.system(bGBP)

					time.sleep(3)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1055 PayPal GBP')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as e:
			raise e

		# If RUB file exists in Google Drive run the uploading script
		try:
			if RUBexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload RUB File
					os.system(bRUB)

					time.sleep(3)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1060 PayPal RUB')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as e:
			raise e

		# If MYR file exists in Google Drive run the uploading script
		try:
			if MYRexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload MYR File
					os.system(bMYR)	

					time.sleep(3)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1065 PayPal MYR')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as e:
			raise e
		
		# If PHP file exists in Google Drive run the uploading script
		try:
			if PHPexist:
					time.sleep(5)
					# Validating if the Browse button exists on the webpage or if we are having server lag, refresh the page
					value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()
					if value != "Browse":
						while value != "Browse":
							time.sleep(90)
							driver.get('https://c5.qbo.intuit.com/app/bankfileupload')
							time.sleep(20)
							value = driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').text.strip()

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Browse")]').click()

					time.sleep(5)

					#To upload PHP File
					os.system(bPHP)

					time.sleep(3)
					#select next
					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()
					time.sleep(3)

					#select gl account
					driver.find_element_by_xpath('//*[@class="dijitReset dijitInputInner"][@placeholder="Select Account"]').send_keys('1070 PayPal PHP')
					time.sleep(2)

					
			

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()



					time.sleep(2)
					#select Date format -- Navigating JavaScript webpage without html list objects (selecting parent directory of element)
					dmenu = driver.find_element_by_xpath('//*[@type="hidden"][@value="dd-MM-yyyy"]/..')
					dmenu.click()
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.send_keys('M')
					time.sleep(1)
					dmenu.click()
					time.sleep(1)

					
					#select Amount format -- Navigating JavaScript webpage without html list objects (selecting child directory of element)
					amenu = driver.find_element_by_xpath('//*[@class="amountField inlineBlock"]//*[@data-qbo-bind="value: amountField, options: mapColumnOptions"]')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.send_keys('C')
					time.sleep(1)
					amenu.click()
					time.sleep(1)
			


					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Next")]').click()	
					time.sleep(2)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Yes")]').click()

					time.sleep(3)

					driver.find_element_by_xpath('//*[@type="button"][contains(text(),"Let")][contains(text(),"go!")]').click()
					time.sleep(10)

					driver.get('https://c5.qbo.intuit.com/app/bankfileupload')

		except Exception as d:
			raise d

		# exits out of Selenium Driver
		driver.quit()


except Exception as e:
	raise e

#to delete files

rCAD = os.path.isfile(r"G:\My Drive\PaypalCSVs\CAD\CAD_Transactions.csv")
rUSD = os.path.isfile(r"G:\My Drive\PaypalCSVs\USD\USD_Transactions.csv")
rGBP = os.path.isfile(r"G:\My Drive\PaypalCSVs\GBP\GBP_Transactions.csv")
rEUR = os.path.isfile(r"G:\My Drive\PaypalCSVs\EUR\EUR_Transactions.csv")
rRUB = os.path.isfile(r"G:\My Drive\PaypalCSVs\RUB\RUB_Transactions.csv")
rMYR = os.path.isfile(r"G:\My Drive\PaypalCSVs\MYR\MYR_Transactions.csv")
rPHP = os.path.isfile(r"G:\My Drive\PaypalCSVs\PHP\PHP_Transactions.csv")

try:
	if  rCAD:
	 	os.remove(r"G:\My Drive\PaypalCSVs\CAD\CAD_Transactions.csv")
except Exception as e:
	raise e

try:
	if  rUSD:
	 	os.remove(r"G:\My Drive\PaypalCSVs\USD\USD_Transactions.csv")
except Exception as e:
	raise e

try:
	if  rGBP:
	 	os.remove(r"G:\My Drive\PaypalCSVs\GBP\GBP_Transactions.csv")
except Exception as e:
	raise e

try:
	if  rEUR:
	 	os.remove(r"G:\My Drive\PaypalCSVs\EUR\EUR_Transactions.csv")
except Exception as e:
	raise e

try:
	if  rRUB:
	 	os.remove(r"G:\My Drive\PaypalCSVs\RUB\RUB_Transactions.csv")
except Exception as e:
	raise e

try:
	if  rMYR:
	 	os.remove(r"G:\My Drive\PaypalCSVs\MYR\MYR_Transactions.csv")
except Exception as e:
	raise e
try:
	if  rPHP:
	 	os.remove(r"G:\My Drive\PaypalCSVs\PHP\PHP_Transactions.csv")
except Exception as e:
	raise e
exit()
