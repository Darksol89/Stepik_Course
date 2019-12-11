import math
import pyperclip
from selenium import webdriver

def get_link(link):
    browser = webdriver.Chrome(executable_path='C:\ChromeDriver/chromedriver.exe')
    browser.get(link)

    return browser

# Calculating formula for getting correct answer
def calculation_formula(x):
    return str(math.log(abs(12*math.sin(x))))

def add_to_clipboard(browser):
    # Catch answer number for Stepik
    alert_stepik = browser.switch_to.alert
    alert_text = alert_stepik.text

    text_in_clipboard = alert_text.split(': ')[-1]
    pyperclip.copy(text_in_clipboard)