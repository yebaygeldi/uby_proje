from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


class AutomaticView:
	
	def view(ethq_province):
		chrome_options = Options()
		chrome_options.add_experimental_option("detach", True)
		CURRENT_DIR = os.getcwd()
		driver = webdriver.Chrome(f"{CURRENT_DIR}/chromedriver", chrome_options=chrome_options)
		driver.implicitly_wait(0.5)
		driver.get("https://www.google.com/")
		m = driver.find_element(By.NAME, "q")
		m.send_keys(ethq_province + " deprem")
		time.sleep(0.2)
		m.send_keys(Keys.ENTER)

		# driver.quit()