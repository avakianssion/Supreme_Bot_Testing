from selenium import webdriver
from config import keys
import time
def order (k):
    
    #driver = webdriver.Chrome('./chromedriver')
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="ard-rrmove-brttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    
    #name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    
    #email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    
    #phone number
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])  
    
    #address
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"]) 
    
    #zip code
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"]) 
    
    #card number
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card_number"])
    
    #cvv
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"]) 
    
    #state, add a dictionary like month of the card
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[6]').click()
    
    #exp month
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["month"])).click()
    
    #exp year
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["year"])).click()
    
    #accept terms
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    
    #proces payment button
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

    #time.sleep(30)






if __name__ == "__main__":
    
    driver = webdriver.Chrome('./chromedriver')
    order(keys)
