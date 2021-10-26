from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
import re
from selenium.webdriver.firefox.service import Service
def information_pointer(region, locality, street, house, count=0):

    driver=webdriver.Chrome()
    # Возможность использования браузера Firefox
    # option=webdriver.FirefoxOptions()
    # s=Service('geckodriver.exe')
    # option.set_preference('dom.webdriver.enabled', False)
    # driver = webdriver.Firefox(options=option, service=s)

    #Первая попытка войти на страницу с расширенным поиском, со sleep в 20 секунд, для возможности ввести captcha
    driver.get('https://www.reformagkh.ru/search/houses-advanced')
    time.sleep(20)

    #Вторая попытка войти на страницу с расширенным поиском (иммется для избежания captcha)
    driver.get('https://www.reformagkh.ru/search/houses-advanced')
    time.sleep(5)
    val = dict()
    values_dict[count] = val
    try:
        # Работа с элементом region
        region_element = driver.find_element(By.CLASS_NAME, 'region')
        region_element.send_keys(region)
        time.sleep(2)
        # Выбираем первый элемент из предложенного списка
        region_element.send_keys(webdriver.Keys.DOWN)
        time.sleep(2)
        region_element.send_keys(webdriver.Keys.ENTER)
        time.sleep(2)

        # Работа с районом дома (в тестовой выборке нет данного пункта, поэтому заккоментированно)
        '''
        district_element=driver.find_element(By.CLASS_NAME, 'district')
        district_element.send_keys(district)
        time.sleep(1)
        district_element.send_keys(webdriver.Keys.DOWN)
        district_element.send_keys(webdriver.Keys.ENTER)
        time.sleep(1)
        '''

        #Работа с городом дома
        time.sleep(2)
        locality_element=driver.find_element(By.CLASS_NAME, 'settlement')
        #Если город не указан в тестовой выборке, то нажимаем TAB, если указан - берем первый элемент из предложенного списка
        if locality == 'None':
            locality_element.send_keys(webdriver.Keys.TAB)
        else:
            locality_element.send_keys(locality)
            time.sleep(2)
            locality_element.send_keys(webdriver.Keys.DOWN)
            time.sleep(2)
            locality_element.send_keys(webdriver.Keys.ENTER)
        time.sleep(2)

        # Работа с улицей дома
        street_element=driver.find_element(By.CLASS_NAME, 'street')
        street_element.send_keys(street)
        time.sleep(2)
        street_element.send_keys(webdriver.Keys.DOWN)
        time.sleep(2)
        street_element.send_keys(webdriver.Keys.ENTER)
        time.sleep(2)

        # Работа с номером дома
        house_element=driver.find_element(By.CLASS_NAME, 'house')
        house_element.send_keys(house)
        time.sleep(2)
        house_element.send_keys(webdriver.Keys.DOWN)
        time.sleep(2)
        house_element.send_keys(webdriver.Keys.ENTER)
        time.sleep(2)


        #После указания всех данных нажимаем НАЙТИ
        btn_element = driver.find_element(By.TAG_NAME, 'button')
        time.sleep(2)
        btn_element.click()
    except:
        val['error']='Search_error'
        print('Ошибка при наборе данных для поиска')
        print(values_dict)
    try:
        # Нажимаем на последнюю из предложенных ссылок после поиска
        #link_element=driver.find_element(By.ID, 'back')
        press_element=driver.find_elements(By.XPATH, '//td/a')
        press_element[len(press_element)-1].click()
        #print(press_element.text)

        # Находим кнопку ПАСПОРТ и нажимаем на нее
        passport_element=driver.find_elements(By.TAG_NAME, 'span')
        for ele in passport_element:
            print(ele.text)
            if ele.text=="ПАСПОРТ":
                ele.click()
                print("Нашел паспорт")
                break
        # Парсинг необходимой информации

        #Год ввода в эксплуатацию
        commissioning_year_element=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[4]/td[2]').text
        #commissioning_year_element=driver.find_element(By.XPATH, "//td[contains(text(), 'Год ввода')]/following-sibling::td").text
        print('Год ввода в эксплуатацию: ', commissioning_year_element)
        val['Год ввода в эксплуатацию']=commissioning_year_element

        #Количество этажей
        floor_number=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[9]/td[2]').text
        print('Количество этажей: ', floor_number)
        # Последнее изменение анкеты
        profile_change=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[1]/td[2]').text
        print('Последнее изменение анкеты: ', profile_change)
        val['Последнее изменение анкеты']=profile_change
        # Серия, тип постройки здания
        series_type=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[8]/td[2]').text
        print('Серия, тип постройки здания: ', series_type)
        val['Серия, тип постройки здания']=series_type
        # Тип дома
        building_type=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[5]/td[2]').text
        print('Тип дома: ', building_type)
        val['Тип дома']=building_type
        #На сайте не нашел элемент показывающий степень аварийности дома
        #accident_rate=driver.find_element(By.XPATH, '').text
        # Кадастровый номер
        cadastral_number=driver.find_element(By.XPATH, '//*[@id="profile-house-style"]/tbody/tr[25]/td[2]').text
        print('Кадастровый номер: ', cadastral_number)
        val['Кадастровый номер']=cadastral_number
        # Нажимаем на кнопку "Структурные элементы"
        structural_elements_btn=driver.find_element(By.XPATH, '//*[@id="constructive-tab"]')
        time.sleep(5)
        structural_elements_btn.click()
        time.sleep(2)
        # Тип перекрытий
        floor_type=driver.find_element(By.XPATH, '//*[@id="house-passport-constructive"]/tbody/tr[5]/td[2]').text
        print('Тип перекрытий', floor_type)
        val['Тип перекрытий']=floor_type
        # Материал несущих стен
        bearing_material=driver.find_element(By.XPATH, '//*[@id="house-passport-constructive"]/tbody/tr[6]/td[2]').text
        print('Материал несущих стен', bearing_material)
        val['Материал несущих стен']=bearing_material
        time.sleep(5)
        print(values_dict)
    # Если ссылка после поиска не найдены, выводим сообщение "Не нашел ссылку"
    except:
        val['error']='Link_error'
        print('Не нашел ссылку')
        print(values_dict)

    time.sleep(5)

def main():


    # Чтение тестовой выборки
    book=openpyxl.open('Тестовая выборка.xlsx', read_only=True)
    sheet=book.active
    count = 1
    for row in range(2, sheet.max_row):

        # Чтение региона (убираем последнее слово, потому что оно мешает поиску)
        region_broken=str(sheet[row][2].value)
        region_template=re.compile('(?P<region>([A-я]?-?)+)')
        match=re.match(region_template, region_broken)
        region=match.group('region')
        print(region)
        # Чтение название города
        locality=str(sheet[row][4].value)
        print(locality)
        locality_type=str(sheet[row][3].value)
        # Если не указан тип населенного пунтка, то используем только его название
        if locality_type=='None':
            locality_stroke=locality
        # Если указан тип, то ставим его перед названием (улучшает поиск)
        else:
            locality_stroke=locality_type+' '+locality
        # Чтение названия улицы
        street=str(sheet[row][6].value)
        print(street)
        street_type=str(sheet[row][5].value)
        # Если не указан тип улицы, то используем ее название
        if street_type=='None':
            street_stroke=street
        # Если указан тип, то ставим его перед названием (улучшает поиск)
        else:
            street_stroke=street_type+' '+street
        # Чтение номера дома
        house=str(sheet[row][7].value)
        block=str(sheet[row][8].value)
        # Если указан блок дома, то добавляем его в конец, если не указан - опускаем
        if block=='None':
            house_stroke=house
        else:
            house_stroke=house+' '+block
            print(house_stroke)
        # Вызов функции парсинга для каждой строки из текстовой выборки
        adr=region+' '+locality_stroke+' '+street_stroke+' '+house_stroke

        information_pointer(region, locality_stroke, street_stroke, house_stroke,count)
        count+=1
    # Возможность работы "вручную", без использования тестовой выборки.
    # Требуется закомметировать часть кода, отвечающую за работу с выборкой
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
    values_dict = dict()
    main()