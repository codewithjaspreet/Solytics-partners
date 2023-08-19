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


#targeted 1,2,3rd table --- 
# -- rest can depend upon the requirement how this data has to be presented in any file
# output can be viewed in console 

def extract():
    

    my_data = [];
    other_data = [];


    try:
        # Open LinkedIn in Chrome
        driver.get("https://sso.agc.gov.sg/Act/TSFA2002?ProvIds=Sc1-#Sc1-")




        wait  =    WebDriverWait(driver, 5)

        data = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='sProvP1']")))

        other_data = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='def']")))

        for i in data:

             print(i.text)

             print("\n")

             

             my_data.append(i.text)


        print("-----------")
        print("-----------")
        
        for i in other_data:

             print(i.text)
             print("\n")
             

             other_data.append(i.text)


        make_dataframe(my_data, other_data)

 
            




    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the task is completed
       while True:
           pass
        #driver.close()



def make_dataframe(l1,l2):

    
    data = {'Column1': l1, 'Column2': l2}

    df = pd.DataFrame(data)

    csv_filename = 'data.csv'
    df.to_csv(csv_filename, index=False)

    print("DataFrame saved to CSV:", csv_filename)


if __name__ == "__main__":

    extract()
    while True:
        pass    
