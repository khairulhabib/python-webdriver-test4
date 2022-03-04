import time
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def click_xpath (str): 
    while 1==1:
        try:
            vo_button = browser.find_element_by_xpath (str)
            break
        except:
            pass

    time.sleep (0.2)
    browser.execute_script("arguments[0].click();", vo_button)

def get_focus_xpath (str):
    v_timeout = time.time() + 20
    vo_result = 0
    while True:
        try:
            vo_result = browser.find_element_by_xpath (str)
            break
        except:
            if time.time() > v_timeout:
                break
    return vo_result

def get_marketing():
    print("do marketing")
    click_xpath ('/html/body/div[8]/div/div[4]/div[5]/div/img')


    # airlines marketing:
    click_xpath ('//*[@id="popBtn2"]')
    pax_new_campaign=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="newCampaign"]')))
    click_xpath ('//*[@id="newCampaign"]')
    click_xpath ('//*[@id="campaign-1"]/table/tbody/tr[1]/td[2]')

    time.sleep (2.7)
    click_xpath ('//*[@id="c4Btn"]')

    print('done marketing pax')

    time.sleep (3)

    # select on cargo
    click_xpath ('//*[@id="popBtn2"]')
    cargo_new_campaign=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="newCampaign"]')))
    click_xpath ('//*[@id="newCampaign"]')
    click_xpath ('//*[@id="campaign-1"]/table/tbody/tr[2]/td[2]')
    time.sleep (2.9)
    click_xpath ('//*[@id="c4Btn"]')

    print('done marketing cargo')

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(os.environ.get("AM4_URL"))
    browser.find_element_by_xpath ('//*[@id="flightStatusInflight"]')

    browser.implicitly_wait(2)

    get_marketing()
    
