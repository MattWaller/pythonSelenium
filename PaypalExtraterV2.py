def PayPal(companyName, j, com_len, destinationDrive):
	# wrapped in try to catch if there is an error with the script, in the event there is an error an email will be sent immediately.
	try:
		filePath = 'My_scripts.PayPal.Credentials.' + companyName + '.PP_Creds'
		
		# defining the import location of the files --> imports the file locations of each company from the target folder.
		moduleName = __import__(filePath, fromlist=['object'])
		login = moduleName.login
		import time
		import datetime
		from Driver2v2 import driver, Keys
		from check_xpath_exists import check_exists_by_xpath
		from random import randint
		
		username = login['consumer_username']
		password = login['consumer_secret']

		url = 'https://www.paypal.com/ca/signin'
			

		driver.get(url)

		time.sleep(2)
		# determine which login page is active
		next_field = '//button[@id="btnNext"]'
		next_Shown = check_exists_by_xpath(driver, next_field)

		# login to paypal if there is no next button is shown.
		if next_Shown == False:
			time.sleep(1)
			#selects all text to clear once username is entered
			driver.find_element_by_id('email').send_keys(Keys.CONTROL + 'a')
			time.sleep(1)
			driver.find_element_by_id('email').send_keys(username)
			time.sleep(randint(2,6))
			driver.find_element_by_id('password').send_keys(password)
			time.sleep(randint(1,2))
			driver.find_element_by_id('btnLogin').click()
		else:
		#To Login to PayPal
			time.sleep(1)
			#selects all text to clear once username is entered
			driver.find_element_by_id('email').send_keys(Keys.CONTROL + 'a')
			time.sleep(1)
			driver.find_element_by_id('email').send_keys(username)
			time.sleep(randint(2,6))
			driver.find_element_by_id('btnNext').click()
			time.sleep(randint(2,6))
			driver.find_element_by_id('password').send_keys(password)
			time.sleep(randint(2,6))
			driver.find_element_by_id('btnLogin').click()

		#To Access Report Page
		time.sleep(randint(10,16))
		
		# ensure no auth button is shown -- agrees to terms 
		authButton = '//button[contains(text(),"Agree")]'
		authButton_Shown = check_exists_by_xpath(driver, authButton)
		#clicks the agree to terms button if present
		if authButton_Shown == True:
			driver.find_element_by_xpath(authButton).click()
			time.sleep(2)
		

		# navigate to the reports tab
		driver.find_element_by_xpath('//a[contains(text(),"Reports")]').click()

		

		time.sleep(randint(10,16))



		#element check

		activityExist = '//a[contains(text(),"Activity download")]'
		activityTest = check_exists_by_xpath(driver, activityExist)
		# determine if page is loaded properly, if not, refresh the page.
		if(activityTest == True):
			driver.find_element_by_xpath('//a[contains(text(),"Activity download")]').click()

		if(activityTest == False):
			while(activityTest == False):
				driver.refresh()
				activityTest = check_exists_by_xpath(driver, activityExist)
			

		time.sleep(randint(5,8))


		#date range selection
		driver.find_element_by_xpath('//*[contains(text(),"Date range")][@class="legend"]').click()

		time.sleep(randint(1,3))
		
		#select yesterday
		driver.find_element_by_xpath('//a[contains(text(),"Yesterday")]').click()

		time.sleep(randint(1,3))

		#select create report
		driver.find_element_by_xpath('//*[@id="dlogSubmit"]').click()


		time.sleep(randint(9,12))

		# checking if the file is ready to be downloaded
		value = driver.find_element_by_xpath('//*[@id="pastHistory"]/table/tbody/tr[1]/td[5]').text.strip()

		if value != "Download":
			while value != "Download":
				if value == "Submitted":
						#select create report
						driver.find_element_by_xpath('//*[@id="dlogSubmit"]').click()
				
				time.sleep(randint(60,90))
				# refresh the list if the element on the page is not "Download"
				driver.find_element_by_xpath('//a[@id="refresh_list"]').click()
				time.sleep(randint(10,20))	
				# re-evaluate if the text field is Downloadable or not.
				value = driver.find_element_by_xpath('//*[@id="pastHistory"]/table/tbody/tr[1]/td[5]').text.strip()

		# Element is downloadable, now download the file.
		driver.find_element_by_xpath('//*[@id="download_0"]').click()
		time.sleep(randint(5,9))
		#sign out of Paypal
		driver.get('https://www.paypal.com/bizcomponents/logout')

		
		time.sleep(randint(10,30))
		if(j + 1 == com_len):
			driver.quit()
			



		from datetime import datetime, timedelta
		import csv
		import shutil
		import os.path

		# defining path on google drive
		destinationPath = destinationDrive + ":\\My Drive\\Paypal Data\\" + companyName + "\\" + companyName + "-PP-Transactions.csv"
		
		# checks to see if there is currently a file located in the target path, and deletes it if there is.
		exists = os.path.isfile(destinationPath)
		try:
			if  exists:
			 	os.remove(destinationPath)
		except Exception as e:
			raise e



		FileName = "C:\\Users\\" + getpass.getuser() + "\\Downloads\\Download.csv"

		shutil.move(FileName, destinationPath)
		time.sleep(1)
		
		# exit at the end of the loop
		if(j + 1 == com_len):
			exit()

	except Exception as e:
		import sys
		import datetime
		from Error_email import Error_email
		scriptname = sys.argv[0]
		timestamp = datetime.datetime.now()
		errorMsg = repr(e)
		Error_email(scriptname,timestamp,errorMsg)


# Pass companyPath and destinationPath to Extractor. -- files will be downloaded into users download path then moved to desired destinationPath
def Extracter(companyPath,destinationDrive):

	import csv
	import getpass
	with open(Path,newline='') as ff:
		companies = list(csv.reader(ff))

	j = 0
	com_len = len(companies)
	if( j < com_len):
		while( j < com_len):
			companyName = companies[j][0]
			filePath = 'Companies.' + companyName
			moduleName = __import__(filePath, fromlist=['object'])
			details = moduleName.details
			PayPal(companyName, j, com_len, destinationDrive)
			j = j + 1


if __name__ == "__main__":
	# defining company path
	companyPath = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\Companies\companies.csv"

	# set drive 
	destinationDrive = "G"
	Extracter(companyPath,destinationDrive)
