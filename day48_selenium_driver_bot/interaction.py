# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
#
# chrome_driver_path = "/Users/kylehan/Development/chromedriver"
# options = webdriver.ChromeOptions()
# service = Service(chrome_driver_path)



#------------------------------------selenium website dig testing-------------------------------------------------#
# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(count.text)
#
# all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
# # all_portals.click()
#
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# # driver.quit()





#---------------------------------------selenium form input testing--------------------------------------------------#
# driver.get("https://secure-retreat-92358.herokuapp.com/")
#
# first_name = driver.find_element(by=By.NAME, value="fName")
# first_name.send_keys("Your")
# last_name = driver.find_element(by=By.NAME, value="lName")
# last_name.send_keys("Mom")
# email = driver.find_element(by=By.NAME, value="email")
# email.send_keys("yourmom@gmail.com")
#
# button = driver.find_element(by=By.TAG_NAME, value="button")
# button.click()




#-----------------------------------selenium python site testing---------------------------------------------------#
#driver.get("https://www.python.org/")
#
#
# event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
#
# print(events)



# event_times = driver.find_elements(class_=".event-widget time")
# # event_names = driver.find_elements(class_=".event-widget li a")
# for time in event_times:
#     print(time)


# driver.quit()