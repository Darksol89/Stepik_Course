import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    # This block going after test finish
    print('\nquit browser..')
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print('preparing some critical data for every test')

class TestMainPage1():
    # Calling fixture in test as test parameter
    def test_guest_should_see_login_link(self, browser):
        print('start test1')
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print('finish test1')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test2')
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print('finish test2')