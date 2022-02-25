"""
A simple selenium test example written by python
"""

import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

def click_xpath (str): 
    while 1==1:
        try:
            vo_button = browser.find_element_by_xpath (str)
            break
        except:
            pass

    time.sleep (0.2)
    browser.execute_script("arguments[0].click();", vo_button)

if __name__ == '__main__':
    print("start capture")
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    
    print(curr_clock)
    chrome_options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(os.environ.get("AM4_URL"))

    browser.implicitly_wait(2)

    click_xpath('//*[@id="mapMaint"]')
    v_price_loc = browser.find_element_by_xpath ('//*[@id="fuelMain"]/div/div[1]/span[2]/b')
    v_price_str = v_price_loc.text

    int_price = int(v_price_loc.text.replace(",","").replace(" ","").replace("$",""))

    # auto buy if price less than 700
    if(int_price < 700):
        v_purchase_loc = browser.find_element_by_xpath ('//*[@id="amountInput"]')
        v_purchase_loc.clear()

        v_capacity_loc = browser.find_element_by_xpath('//*[@id="remCapacity"]')
        v_capacity = int(v_capacity_loc.text.replace(',',''))

        if(v_capacity > 0):
            v_purchase_loc.send_keys (v_capacity_loc.text)
            time.sleep(0.5)
            click_xpath('//*[@id="fuelMain"]/div/div[7]/div/button[2]')
            time.sleep(2)
            print("bought fuel " + v_capacity_loc.text + " at price " + v_price_str)

    
    click_xpath('//*[@id="popBtn2"]')
    time.sleep(0.5)
    v_priceco_loc = browser.find_element_by_xpath('//*[@id="co2Main"]/div/div[2]/span[2]/b')
    
    print("current fuel: " + v_price_str + "; CO2:" + v_priceco_loc.text)