import time
from additional_func_stepik import get_link
from additional_func_stepik import calculation_formula
from additional_func_stepik import add_to_clipboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    # Open Link in browser
    browser = get_link(link)
    # Find price element and text
    price_text = '100'
    # WebDriver wait before price would be equals 100$
    price_wait = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), price_text))

    book_btn = browser.find_element(By.XPATH, ('//button[@id="book"]'))
    book_btn.click()

    # Calculation formula
    element_y = browser.find_element(By.XPATH, ('//span[@id="input_value"]'))
    element_x = element_y.text
    result_calculation = calculation_formula(int(element_x))

    field_to_input = browser.find_element(By.XPATH, ('//input[@id="answer"]'))
    field_to_input.send_keys(result_calculation)

    # Click Submit button
    submit_btn = browser.find_element(By.XPATH, ('//button[@id="solve"]'))
    submit_btn.click()
    submit_btn.get_attribute()

    # Catch right answer from alert
    add_to_clipboard(browser)

finally:
    time.sleep(10)
    browser.quit()


