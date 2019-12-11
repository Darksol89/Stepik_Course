import time
import pyperclip
from selenium import webdriver
from additional_func_stepik import calculation_formula

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome(executable_path='C:\ChromeDriver/chromedriver.exe')
    browser.get(link)

    # Click button and catch alert
    magical_button = browser.find_element_by_css_selector('button.btn')
    magical_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    # Calc math formula
    element_y = browser.find_element_by_xpath('//span[@id="input_value"]')
    element_x = element_y.text
    result_calc = calculation_formula(int(element_x))

    # Input math result to input field
    field_to_input = browser.find_element_by_xpath('//input[@id="answer"]')
    field_to_input.send_keys(result_calc)

    # Click Submit button
    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()

    # Catch answer for Stepik from alert
    alert_answer = browser.switch_to.alert
    answer_text = alert.text
    text_to_clipboard = answer_text.split(': ')[-1]
    pyperclip.copy(text_to_clipboard)

finally:
    time.sleep(10)
    browser.quit()

