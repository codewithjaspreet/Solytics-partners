import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--start-maximized") 

driver = webdriver.Chrome( options=chrome_options)



def extract():
    

  


    try:
        # Open LinkedIn in Chrome
        driver.get("https://sso.agc.gov.sg/Act/TSFA2002?ProvIds=Sc1-#Sc1-")




        wait  =    WebDriverWait(driver, 5)

        #  //td[@class ="sHdr"]
        # //td[@class ="SbodyRefs"]
        # //td[@class ="scHdr"]

        # //td[@class ="tailSTxt"]

        f_title = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='sHdr']")))

        s_title = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='SbodyRefs']")))

        header =   wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='scHdr']")))


        tables = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='tailSTxt']")))

        
        print("-----------")
        print(f_title.text)
        print("-----------")


        print("-----------")
        print(s_title.text)
        print("-----------")


        print("-----------")
        print(header.text)
        print("-----------")


        print("-----------")

        for i in tables:
                
                 print(i.text)
    
                 print("\n")
    
                 
    

        print("-----------")


     

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        
        driver.close()


if __name__ == "__main__":

    extract()
      
