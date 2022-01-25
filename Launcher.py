from selenium import webdriver
import chromedriver_binary
import Engine
'''
if using a different chromedriver from shoestore environment,
then comment import chromedriver_binary
and also comment webdriver = webdriver.Chrome()
And uncomment 
chromedriver_path = 'thepathofyourchromedriver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
'''

webdriver = webdriver.Chrome()

#chromedriver_path = 'thepathofyourchromedriver' 
#webdriver = webdriver.Chrome(executable_path=chromedriver_path)

Engine.init(webdriver)
Engine.update(webdriver)

webdriver.close()
