try:	
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from selenium.common.exceptions import NoSuchElementException
	from ChromeVersion import chrome_browser_version
	import os
	import time
	from random import randint
	import getpass

	#define download path
	downloadPath = "C:\\Users\\" + getpass.getuser() + "\\Downloads\\Download.csv"
	driverName = "\\chromedriver.exe"

	# defining base file directory of chrome drivers
	driver_loc = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\ChromeDriver\\"

	currentPath = driver_loc + chrome_browser_version + driverName 



	executable_path = currentPath
	chrome_options = Options()

	
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("download.default_directory=" + downloadPath)

	driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
	

	

except Exception as e:
	import sys
	import datetime
	from Error_email import Error_email
	scriptname = sys.argv[0]
	timestamp = datetime.datetime.now()
	errorMsg = repr(e)
	Error_email(scriptname,timestamp,errorMsg)
