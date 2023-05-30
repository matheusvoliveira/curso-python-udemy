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
        option.add_argument('--headless')
        self.driver.get(self.url)
        time.sleep(10)

        # counter = 1
        # max_annoucement = 50
        # # while counter < max_annoucement:
        #self.driver.find_element(By.XPATH,
        #                          f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/'
        #                          f'div[11]/div/div/div/ul/li[{counter}]/div').click()
        # time.sleep(5)

    def click_announcement(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@id="cookie-notice-ok-button"]').click()
        time.sleep(2)
        counter = 1
        max_annoucement = 50
        while counter < max_annoucement:
            self.driver.find_element(By.XPATH,
                                     f'/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/div/div/div/ul/li[{counter}]/div').click()
            counter += 1
            print(counter)
            time.sleep(2)
            # acha a janela recem aberta e feche ela
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])


            self.driver.close()
            self.driver.switch_to.window(handles[0])
            time.sleep(10)
            #self.driver.find_element(By.XPATH,
                                     #'//*[@id="cookie-notice-ok-button"]').click()

        self.driver.quit()


olx_bot = Acess()
olx_bot.open_web()
olx_bot.click_announcement()
