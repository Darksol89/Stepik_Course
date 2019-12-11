import time

from additional_func_stepik import get_link
from additional_func_stepik import calculation_formula
from additional_func_stepik import add_to_clipboard

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = get_link(link)

    # Click to trollface button
    troll_button = browser.find_element_by_css_selector('button.trollface')
    troll_button.click()

    # Switch tab in browser
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    # Calculation formula and input result
    element_y = browser.find_element_by_xpath('//span[@id="input_value"]')
    element_x = element_y.text
    result_calc = calculation_formula(int(element_x))

    field_to_input = browser.find_element_by_xpath('//input[@id="answer"]')
    field_to_input.send_keys(result_calc)

    # Click Submit button
    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()

    # Copy to Clipboard
    add_to_clipboard(browser)

finally:
    time.sleep(10)
    browser.quit()

