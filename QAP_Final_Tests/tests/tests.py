import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe')

# Тестирование заголовков в окне авторизации
def test_rostelecom_1(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_phone = selenium.find_element(By.ID, "t-btn-tab-phone")

    btn_phone.click()

    btn_mail = selenium.find_element(By.ID, "t-btn-tab-mail")

    btn_mail.click()

    btn_login = selenium.find_element(By.ID, "t-btn-tab-login")

    btn_login.click()

    btn_ls = selenium.find_element(By.ID, "t-btn-tab-ls")

    btn_ls.click()

# Тестирование ссылок на социальные сети
def test_rostelecom_2(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_vkontakte = selenium.find_element(By.XPATH, "oidc_vk")

    btn_vkontakte.click()

    btn_odnoklasn = selenium.find_element(By.XPATH, "oidc_ok")

    btn_odnoklasn.click()

    btn_mail = selenium.find_element(By.ID, "oidc_mail")

    btn_mail.click()

    btn_google = selenium.find_element(By.ID, "oidc_google")

    btn_google.click()

    btn_yandex = selenium.find_element(By.ID, "oidc_ya")

    btn_yandex.click()

# Тестирование ссылок в "footer"
def test_rostelecom_3(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_cookies = selenium.find_element(By.LINK_TEXT, "Cookies")

    btn_cookies.click()

    btn_polconf = selenium.find_element(By.LINK_TEXT, "Политикой конфиденциальности ")

    btn_polconf.click()

    btn_polconf = selenium.find_element(By.LINK_TEXT, " Пользовательским соглашением ")

    btn_polconf.click()


# Авторизации клиента.  Вкладка "Телефон". Позитивный сценарий
def test_rostelecom_4(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-phone")
    btn_exist_acc.click()

    field_phone = selenium.find_element(By.LINK_TEXT, "Мобильный телефон")
    field_phone.clear()
    field_phone.send_keys("+88975773780")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_phone_login.png')
    else:
        raise Exception("login error")

# Авторизации клиента.  Вкладка "Телефон". Негативный сценарий
def test_rostelecom_5(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-phone")
    btn_exist_acc.click()

    field_phone = selenium.find_element(By.LINK_TEXT, "Мобильный телефон")
    field_phone.clear()
    field_phone.send_keys("jgh$%&ffk")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()


    assert Exception("login error")
    assert selenium.current_url != 'https://start.rt.ru/?tab=main'


# Авторизации клиента.  Вкладка "Почта". Позитивный сценарий
def test_rostelecom_6(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-mail")
    btn_exist_acc.click()

    field_mail = selenium.find_element(By.LINK_TEXT, "Электронная почта")
    field_mail.clear()
    field_mail.send_keys("rst@mail.ru")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_mail_login.png')
    else:
        raise Exception("login error")


# Авторизации клиента.  Вкладка "Почта". Негативный сценарий
def test_rostelecom_7(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-mail")
    btn_exist_acc.click()

    field_mail = selenium.find_element(By.LINK_TEXT, "Электронная почта")
    field_mail.clear()
    field_mail.send_keys("757857;%?")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    assert Exception("login error")
    assert selenium.current_url != 'https://start.rt.ru/?tab=main'



# Авторизации клиента.  Вкладка "Логин". Позитивный сценарий
def test_rostelecom_8(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-login")
    btn_exist_acc.click()

    field_login = selenium.find_element(By.LINK_TEXT, "Логин")
    field_login.clear()
    field_login.send_keys("TYJK67JJ8")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_login.png')
    else:
        raise Exception("login error")


# Авторизации клиента.  Вкладка "Логин". Негативный сценарий
def test_rostelecom_9(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-login")
    btn_exist_acc.click()

    field_login = selenium.find_element(By.LINK_TEXT, "Логин")
    field_login.clear()
    field_login.send_keys("_№%:?***(")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()


    assert Exception("login error")
    assert selenium.current_url != 'https://start.rt.ru/?tab=main'


# Авторизации клиента.  Вкладка "Лицевой счет". Позитивный сценарий
def test_rostelecom_10(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-ls")
    btn_exist_acc.click()

    field_ls = selenium.find_element(By.LINK_TEXT, "Лицевой счёт")
    field_ls.clear()
    field_ls.send_keys("896749939578")

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()
    field_pass.send_keys("23eswdfd")


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_ls_login.png')
    else:
        raise Exception("login error")

# Авторизации клиента.  Вкладка "Лицевой счет". Негатитивный сценарий
    @pytest.mark.parametrize("ls", [-5551, 2, 3*20, "hfhjfjh", "#$$#@%"])
    @pytest.mark.parametrize("pass", ["23eswdfd"])
    def test_multiply_params(x, y):
        print("x: {0}, y: {1}".format(x, y))
        assert True
def test_rostelecom_11(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_exist_acc = selenium.find_element(By.ID, "t-btn-tab-ls")
    btn_exist_acc.click()

    field_ls = selenium.find_element(By.LINK_TEXT, "Лицевой счёт")
    field_ls.clear()

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()


    btn_submit = selenium.find_element(By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium "
                                                 "rt-btn--rounded login-form__login-btn")
    btn_submit.click()

    assert Exception("login error")
    assert selenium.current_url != 'https://start.rt.ru/?tab=main'

# Главная страница сайта. Регистрация. Заголовки
def test_rostelecom_12(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_registr = selenium.find_element(By.ID, "kc-register")
    btn_registr.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_registr_link.png')
    else:
        raise Exception("link error")


# Регистрация клиента.  Поля ввода "Имя" и "Фамилия".
def russian_chars_30():
    return 'абвгдеёжзийклмнопрстуфхцчш'

def russian_chars_1():
    return 'а'

def russian_chars_40():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def latin_chars():
    return 'ryytuilfkjfjht'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

def email():
    return 'rst@mail.ru'

def phone():
    return '896749939578'

@pytest.fixture(autouse=True)

    @pytest.mark.parametrize("name", [russian_chars_30(), russian_chars_1(), russian_chars_40(),
                                      latin_chars(), special_chars()])
    @pytest.mark.parametrize("pass", ["23eswdfd"])
    def test_multiply_params(x, y):
        print("x: {0}, y: {1}".format(x, y))
        assert True

def test_rostelecom_13(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_registr = selenium.find_element(By.ID, "kc-register")
    btn_registr.click()

    field_name = selenium.find_element(By.NAME, "firstName")
    field_name.clear()

    field_lastName = selenium.find_element(By.NAME, "lastName")
    field_lastName.clear()

    field_pass = selenium.find_element(By.XPATH, "/html/body/div[1]/main/section[2]/div/div/"
                                                 "div/form/div[2]/div/span[2]")
    field_pass.clear()


    btn_registr = selenium.find_element(By.NAME, "registr")
    btn_registr.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_registr.png')
    else:
        raise Exception("registration error")


# Регистрация клиента.  Поля ввода "E-mail или мобильный телефон"

def test_rostelecom_14(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_registr = selenium.find_element(By.ID, "kc-register")
    btn_registr.click()

    field_email = selenium.find_element(By.LINK_TEXT, "E-mail или мобильный телефон")
    field_email.clear()
    field_email.send_keys(email())
    field_email.send_keys(phone())

    btn_registr = selenium.find_element(By.NAME, "registr")
    btn_registr.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_emph.png')
    else:
        raise Exception("email or phone error")

# Регистрация клиента. Поле ввода "Пароль". Позитивный сценарий.
def test_rostelecom_15(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_registr = selenium.find_element(By.ID, "kc-register")
    btn_registr.click()

    field_passw = selenium.find_element(By.LINK_TEXT, "E-mail или мобильный телефон")
    field_passw.clear()
    field_passw.send_keys("23eswdfd")

    btn_registr = selenium.find_element(By.NAME, "registr")
    btn_registr.click()

    if selenium.current_url == 'https://start.rt.ru/?tab=main':
        selenium.save_screenshot('result_passw.png')
    else:
        raise Exception("password error")


# Регистрация клиента. Поле ввода "Пароль". Негативный сценарий.
def test_rostelecom_15(selenium):

    selenium.get("https://b2c.passport.rt.ru/")

    btn_registr = selenium.find_element(By.ID, "kc-register")
    btn_registr.click()

    field_passw = selenium.find_element(By.LINK_TEXT, "E-mail или мобильный телефон")
    field_passw.clear()
    field_passw.send_keys("87667-5")

    btn_registr = selenium.find_element(By.NAME, "registr")
    btn_registr.click()

    assert Exception("password error")
    assert selenium.current_url != 'https://start.rt.ru/?tab=main'

    