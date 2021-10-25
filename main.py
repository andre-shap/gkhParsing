from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
import re
def information_pointer(region, locality, street, house):
    driver = webdriver.Chrome()
    driver.get('https://www.reformagkh.ru/search/houses-advanced')
    time.sleep(5)
    region_element = driver.find_element(By.CLASS_NAME, 'region')
    region_element.send_keys(region)
    time.sleep(1)
    region_element.send_keys(webdriver.Keys.DOWN)
    region_element.send_keys(webdriver.Keys.ENTER)
    time.sleep(1)

    '''
    district_element=driver.find_element(By.CLASS_NAME, 'district')
    district_element.send_keys(district)
    time.sleep(1)
    district_element.send_keys(webdriver.Keys.DOWN)
    district_element.send_keys(webdriver.Keys.ENTER)
    time.sleep(1)
    '''


    time.sleep(2)
    locality_element=driver.find_element(By.CLASS_NAME, 'settlement')
    if locality == 'None':
        locality_element.send_keys(webdriver.Keys.TAB)
    else:
        locality_element.send_keys(locality)
        time.sleep(1)
        locality_element.send_keys(webdriver.Keys.DOWN)
        locality_element.send_keys(webdriver.Keys.ENTER)
    time.sleep(1)

    street_element=driver.find_element(By.CLASS_NAME, 'street')
    street_element.send_keys(street)
    time.sleep(1)
    street_element.send_keys(webdriver.Keys.DOWN)
    street_element.send_keys(webdriver.Keys.ENTER)
    time.sleep(1)

    house_element=driver.find_element(By.CLASS_NAME, 'house')
    house_element.send_keys(house)
    time.sleep(1)
    house_element.send_keys(webdriver.Keys.DOWN)
    house_element.send_keys(webdriver.Keys.ENTER)
    time.sleep(1)
    # print(btn_element)
    btn_element = driver.find_element(By.TAG_NAME, 'button')
    btn_element.click()
    time.sleep(2)

    time.sleep(5)

def main():
    book=openpyxl.open('Тестовая выборка.xlsx', read_only=True)
    sheet=book.active
    #print(sheet.max_row)
    for row in range(2, sheet.max_row):
        region_broken=str(sheet[row][2].value)
        region_template=re.compile('(?P<region>([A-я]?-?)+)')
        match=re.match(region_template, region_broken)
        region=match.group('region')
        print(region)
        locality=str(sheet[row][4].value)
        print(locality)
        street=str(sheet[row][6].value)
        print(street)
        house=str(sheet[row][7].value)
        block=str(sheet[row][8].value)
        if block=='None:':
            house_stroke=house
        else:
            house_stroke=house+' '+block
            print(house_stroke)

        information_pointer(region, locality, street, house_stroke)
    '''
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
    '''

if __name__=='__main__':

    main()