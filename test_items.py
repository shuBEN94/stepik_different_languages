from selenium.webdriver.common.by import By


def test_add_to_basket_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert len(add_to_basket_button) > 0, 'button not found'

