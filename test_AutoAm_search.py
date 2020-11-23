from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
import time
import unittest

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")


def testStep1():
    driver.get("https://auto.am/")
    print(driver.title)


def testMaximize():
    driver.maximize_window()
    print("123")


def test_auto_am_dropdown():
    make = driver.find_element_by_id("filter-make")
    drp_make = Select(make)
    drp_make.select_by_visible_text("Nissan")
    time.sleep(2)
    model = driver.find_element_by_id("v-model")
    drp_model = Select(model)
    drp_model.select_by_visible_text("Versa")
    time.sleep(2)
    year_gt = driver.find_element_by_name("year[gt]")
    drp_year_gt = Select(year_gt)
    drp_year_gt.select_by_visible_text("2013")
    time.sleep(2)
    year_lt = driver.find_element_by_name("year[lt]")
    drp_year_lt = Select(year_lt)
    drp_year_lt.select_by_visible_text("2017")
    time.sleep(2)
    price_gt = driver.find_element_by_name("usdprice[gt]")
    drp_price_gt = Select(price_gt)
    drp_price_gt.select_by_visible_text("$3000")
    time.sleep(2)
    price_lt = driver.find_element_by_name("usdprice[lt]")
    drp_price_lt = Select(price_lt)
    drp_price_lt.select_by_visible_text("$6000")

    cust = driver.find_element_by_class_name("lever")
    cust.click()
    time.sleep(1)
    search_count = driver.find_element_by_xpath('//*[@id="search-btn"]/span')
    print(search_count.text)
    x = search_count.text
    y = int(x)
    if y > 0:
        search = driver.find_element_by_id("search-btn")
        search.click()
    else:
        print("for this filter no cars found")


def test_auto_am_checkbox():
    time.sleep(1)
    ####Check and uncheck Anhatner bajiny
    driver.find_element_by_xpath("//*[@id='search-tools']/div[2]/p[1]/label").click()
    print("anhatakan")

    Oredering = driver.find_element_by_name("filter-sort")
    drpOrederingPrice = Select(Oredering)
    drpOrederingPrice.select_by_value("price-asc")
