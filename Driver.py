# Define Selenium webdriver settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

executable_path = r"C:\Users\Matt\AppData\Local\Programs\Python\Python37-32\chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)