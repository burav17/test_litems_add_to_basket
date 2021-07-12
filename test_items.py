# pytest --language=es test_items.py
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector("#login_link")
    btn_add_to_basket = browser.find_elements_by_css_selector(".btn.btn-add-to-basket")
    len_btn_basket = len(btn_add_to_basket)
    assert len_btn_basket > 0, 'Кнопка "Добавить в корзину" найдена!'
