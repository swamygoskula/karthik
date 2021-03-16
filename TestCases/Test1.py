from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.close()