import pytest

from selenium.webdriver.common.by import By

from main import MyPets


@pytest.fixture
def login_to_my_pets(selenium):
    selenium.implicitly_wait(10)
    selenium.get("https://petfriends.skillfactory.ru/")
    btn_new_user = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("kasatkin.1995@list.ru")

    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("zkemjaac15226")

    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.find_element(By.CSS_SELECTOR, 'html>body>nav>div>ul >li>a').click()
    return MyPets()