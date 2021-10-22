from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def information_pointer(region, district, locality, street, house):
    driver = webdriver.Chrome()
    driver.get('https://www.reformagkh.ru/search/houses-advanced')
    time.sleep(5)

    region_element = driver.find_element(By.CLASS_NAME, 'region')
    region_element.send_keys(region)
    time.sleep(1)
    offer=driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li[@class='ui-menu-item']//div")
    offer[0].click()
    for i in range(len(offer)):
        offer.pop()
    time.sleep(2)


    district_element=driver.find_element(By.CLASS_NAME, 'district')
    district_element.send_keys(district)
    time.sleep(1)
    offer = driver.find_elements(By.XPATH, "//ul[@id='ui-id-89']//li[@class='ui-menu-item']//div")
    time.sleep(1)
    offer[0].click()
    for i in range(len(offer)):
        offer.pop()
    time.sleep(2)
    locality_element=driver.find_element(By.CLASS_NAME, 'settlement')
    locality_element.send_keys(locality)
    time.sleep(1)
    offer = driver.find_elements(By.XPATH, "//ul[@id='ui-id-89']//li[@class='ui-menu-item']//div")
    time.sleep(1)
    offer[0].click()
    for i in range(len(offer)):
        offer.pop()
    time.sleep(2)
    street_element=driver.find_element(By.CLASS_NAME, 'street')
    street_element.send_keys(street)
    time.sleep(1)
    offer = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1999']//li[@class='ui-menu-item']//div")
    offer[0].click()
    for i in range(len(offer)):
        offer.pop()
    time.sleep(2)
    house_element=driver.find_element(By.CLASS_NAME, 'house')
    house_element.send_keys(house)
    time.sleep(1)
    for i in range(len(offer)):
        offer.pop()
    offer = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1992']//li[@class='ui-menu-item']//div")
    offer[0].click()
    for i in range(len(offer)):
        offer.pop()
    time.sleep(2)
    # print(btn_element)
    btn_element = driver.find_element(By.TAG_NAME, 'button')
    btn_element.click()
    time.sleep(2)

    driver.implicitly_wait(5)
def main():
    print("Введите регион (обязательно):")
    region=str(input())
    print("Введите район (необязательно):")
    district=str(input())
    print("Введите населённый пункт (обязательно):")
    locality=str(input())
    print("Введите улицу (необязательно):")
    street=str(input())
    print("Введите номер дома (необязательно):")
    house=int(input())
    information_pointer(region, district, locality, street, house)


if __name__=='__main__':
    main()