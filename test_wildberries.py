import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def setup_module():
    # Настройка одного раза перед всеми тестами
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) #Устанавливаем неявное ожидание на 10 секунд(ожидание непоявившихся элементов)
    yield driver
    driver.quit() # Закрытие браузера после всех тестов


def test_google_search(setup_module):
    href = "https://www.wildberries.ru/catalog/21195420/detail.aspx"
    setup_module.get("https://www.wildberries.ru/")#переходим на главную страницу wildberries
    search_input = setup_module.find_element(By.CSS_SELECTOR, "input[type='search']")#находим строку поиска
    search_input.send_keys("чесалка для кошек",Keys.ENTER)#отправляем данные в строку поиска
    assert setup_module.find_element(By.CSS_SELECTOR, f"a[href='{href}']")#проверяем существование элемента с указанным выше href
