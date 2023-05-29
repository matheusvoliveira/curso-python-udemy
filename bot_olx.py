from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import json
import pyautogui

class Acess:

    def __init__(self):
        self.url = 'https://www.olx.com.br/brasil?pe=750&ps=650&q=xbox+one&sf=1&opst=2'
        self.driver = webdriver.Edge()
    def open_web(self):
       option = Options()
       option.headless = True
       self.driver.get(self.url)
       #time.sleep(10)
       pop_up = self.driver.find_element(By.XPATH,
                                    '//*[@id="cookie-notice-ok-button"]').click()


    def click_announcement(self):
        counter = 1
        max_annoucement = 50
        while counter < max_annoucement:
            self.driver.find_element(By.XPATH,
                                           f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/'
                                           f'div[11]/div/div/div/ul/li[{counter}]/div').click()
            counter += 1
            print(counter)

        driver.quit()

olx_bot = Acess()
olx_bot.open_web()
olx_bot.click_announcement()