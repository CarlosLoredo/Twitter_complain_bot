from selenium import webdriver

chrome_driver_path = '/home/lobo/PycharmProjects/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://twitter.com/login")

