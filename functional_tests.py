from selenium import webdriver

opts = webdriver.FirefoxOptions()
opts.add_argument("--headless") # porque estou executando em um servidor sem GUI
browser = webdriver.Firefox(options=opts)

browser.get('http://localhost:8000')

assert 'Django' in browser.title
