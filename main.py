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
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

driver = webdriver.Chrome( options=chrome_options)


#targeted individiuals data --- 
# -- rest can depend upon the requirement
def extract():
    

    my_data = [];


    try:
        # Open LinkedIn in Chrome
        driver.get("https://sso.agc.gov.sg/Act/TSFA2002?ProvIds=Sc1-#Sc1-")




        wait  =    WebDriverWait(driver, 5)

        data = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='sProvP1']")))

        for i in data:

             print(i.text)
             my_data.append(i.text)

        return my_data

 
            




    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the task is completed
       while True:
           pass
        #driver.close()



def make_dataframe(l1 ):

    
    rows = zip(l1)

    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['data_extracted'])  
        writer.writerows(rows)



if __name__ == "__main__":

    l1 = extract()
    make_dataframe(l1)
    while True:
        pass    
