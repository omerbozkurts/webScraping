from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions
options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('https://www.miuul.com')
time.sleep(3)
driver.title
driver.current_url
driver.quit()

element = driver.find_element(By.XPATH, '//a')
element
element.text
element.get_attribute('innerText')
element.get_attribute('innerHTML')

p_elements = driver.find_elements(By.XPATH, '//p')
p_elements

elem = None
if p_elements:
    elem = p_elements[0]
else:
    print('Element ot found')

print(elem)

btn_elements = driver.find_elements(By.XPATH, "//a[@id='login']")
btn = btn_elements[0]
btn.click()

inputs = driver.find_elements(By.XPATH, "//input[@name='arama']")
input = inputs[0]
input.send_keys("Data Science", Keys.ENTER)





options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get('https://miuul.com/katalog')
time.sleep(10)

a_element = driver.find_elements(By.XPATH,"//a[contains(@href,'biyo')]")[1]
driver.execute_script("arguments[0].scrollIntoView();", a_element)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
a_element.click()

















