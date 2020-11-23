from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")


driver.get("https://auto.am/")
print(driver.title)


driver.maximize_window()
print("123")


element = driver.find_element_by_id("select2-filter-make-container")
drp = Select(element)
drp.select_by_visible_text('Mercedes-Benz')
#drp.select_by_index(2)

