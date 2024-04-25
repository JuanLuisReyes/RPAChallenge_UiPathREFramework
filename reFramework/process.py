from reFramework.getMaestro import *
import reFramework.globalVariable as globalVariables
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    print("Processing transaction: " + str(globalVariables.transactionNumber))

    if globalVariables.transactionNumber == 0:
        start_button = bot.find_element("//button[contains(text(), 'Start')]", By.XPATH)
        start_button.click()

    first_name = bot.find_element("//input[@ng-reflect-name='labelFirstName']", By.XPATH)
    first_name.send_keys(globalVariables.transactionItem['First Name'].iloc[globalVariables.transactionNumber])
    
    last_name = bot.find_element("//input[@ng-reflect-name='labelLastName']", By.XPATH)
    last_name.send_keys(globalVariables.transactionItem['Last Name '].iloc[globalVariables.transactionNumber])
    
    company_name = bot.find_element("//input[@ng-reflect-name='labelCompanyName']", By.XPATH)
    company_name.send_keys(globalVariables.transactionItem['Company Name'].iloc[globalVariables.transactionNumber])
    
    role_in_company = bot.find_element("//input[@ng-reflect-name='labelRole']", By.XPATH)
    role_in_company.send_keys(globalVariables.transactionItem['Role in Company'].iloc[globalVariables.transactionNumber])
    
    address = bot.find_element("//input[@ng-reflect-name='labelAddress']", By.XPATH)
    address.send_keys(globalVariables.transactionItem['Address'].iloc[globalVariables.transactionNumber])
    
    email = bot.find_element("//input[@ng-reflect-name='labelEmail']", By.XPATH)
    email.send_keys(globalVariables.transactionItem['Email'].iloc[globalVariables.transactionNumber])
   
    phone_Number = bot.find_element("//input[@ng-reflect-name='labelPhone']", By.XPATH)
    phone_Number.send_keys(str(globalVariables.transactionItem['Phone Number'].iloc[globalVariables.transactionNumber]))
    
    submit_button = bot.find_element("//input[@type='submit']", By.XPATH)
    submit_button.click()

    print("Transaction proccessed correctly")

if __name__ == '__main__':
    main()