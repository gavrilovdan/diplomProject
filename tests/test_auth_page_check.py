import pytest
import time
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage
from conftest import chrome_browser_instance
#from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait
import uuid
import os
from conftest import web_browser
from pages.base import WebPage


@pytest.fixture(scope="function")
def auth_page(chrome_browser_instance):
    return AuthPage(chrome_browser_instance)


def test_auth_page_title(auth_page):
    auth_title = WebDriverWait(auth_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/h1"))
    )
    time.sleep(1)
    assert auth_title.text == "Авторизация"


def test_auth_page_all_tabs_text(auth_page):
    phone_tab_text = auth_page.btn_tab_phone.get_text()
    email_tab_text = auth_page.btn_tab_email.get_text()
    login_tab_text = auth_page.btn_tab_login.get_text()
    ls_tab_text = auth_page.btn_tab_ls.get_text()

    assert phone_tab_text == "Телефон"
    assert email_tab_text == "Почта"
    assert login_tab_text == "Логин"
    assert ls_tab_text == "Лицевой счёт"

def test_auth_page_email_test(auth_page):

    auth_page.btn_tab_email.click()
    email_active = auth_page._web_driver.find_element(By.XPATH, '//*[@class="rt-tab rt-tab--small rt-tab--active"]')
    element_color = email_active.value_of_css_property('color')
    expected_color = 'rgba(255, 79, 18, 1)'
    assert element_color == expected_color  # ожидаем что вкладка "почта" перекрашивается в красный цвет
    #web_browser.('screenshots/' + str(uuid.uuid4()) + '.png')


def test_auth_page_login_test(auth_page):

    auth_page.btn_tab_login.click()
    login_active = auth_page._web_driver.find_element(By.XPATH, '//*[@class="rt-tab rt-tab--small rt-tab--active"]')
    element_color = login_active.value_of_css_property('color')
    expected_color = 'rgba(255, 79, 18, 1)'
    assert element_color == expected_color  # ожидаем что вкладка "почта" перекрашивается в красный цвет

def test_auth_page_ls_test(auth_page):

    auth_page.btn_tab_ls.click()
    ls_active = auth_page._web_driver.find_element(By.XPATH, '//*[@class="rt-tab rt-tab--small rt-tab--active"]')
    element_color = ls_active.value_of_css_property('color')
    expected_color = 'rgba(255, 79, 18, 1)'
    assert element_color == expected_color  # ожидаем что вкладка "почта" перекрашивается в красный цвет

def test_auth_page_email_phone_test(auth_page):

    auth_page.btn_tab_email.click()
    auth_page.btn_tab_phone.click()
    phone_active = auth_page._web_driver.find_element(By.XPATH, '//*[@class="rt-tab rt-tab--small rt-tab--active"]')
    element_color = phone_active.value_of_css_property('color')
    expected_color = 'rgba(255, 79, 18, 1)'
    assert element_color == expected_color  # ожидаем что вкладка "почта" перекрашивается в красный цвет
    #web_browser.('screenshots/' + str(uuid.uuid4()) + '.png')

@pytest.mark.xfail
def test_auth_page_eye_btn(auth_page):

    auth_page.input_password.click()
    input_password = auth_page._web_driver.find_element(By.XPATH, '//*[@id="password"]')
    input_password.send_keys("qwethqehw")
    auth_page.eye_btn.click()
    test = auth_page._web_driver.find_element(By.TAG_NAME, 'type').text
    assert test == 'r'
    #assert driver.find_element(By.TAG_NAME, 'type').text != "text"

def test_auth_page_fg_ps_link(auth_page):

    auth_page.forgot_password.click()
    driver = webdriver.Chrome()
    test_url = driver.current_url
    assert test_url != 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=zq5EysVpCvI'

#Добавить фикстуру для пропуска теста с пометкой
def test_auth_page_usagr(auth_page):

    auth_page.btn_usagr.click()
    time.sleep(5)
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    assert test_url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

def test_auth_page_tinkoff(auth_page):

    auth_page.btn_tink.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'cid='
    res = test_url.split(seporator, 1)[0]
    res += 'cid='
    assert res == 'https://id.tinkoff.ru/auth/step?cid='

def test_auth_page_yand(auth_page):

    auth_page.btn_yand.click()
    auth_page.btn_yand.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'Fstate%'
    res = test_url.split(seporator, 1)[0]
    res += 'Fstate%'
    assert res == 'https://passport.yandex.ru/auth/plain?retpath=https%3A%2F%2Foauth.yandex.ru%2Fauthorize%3Fstate%'

def test_auth_page_vk(auth_page):

    auth_page.btn_vk.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'state='
    res = test_url.split(seporator, 1)[0]
    res += 'state='
    assert res == 'https://id.vk.com/auth?return_auth_hash=c2a2b1ca282975937c&redirect_uri=https%3A%2F%2Fb2c.passport.rt.ru%2Fsocial%2Fadapter%2Fvk%2Fauth&redirect_uri_hash=518dc24ec25b6796c1&force_hash=&app_id=6771961&response_type=code&code_challenge=&code_challenge_method=&scope=4194304&state='

def test_auth_page_mail(auth_page):

    auth_page.btn_mail.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'state='
    res = test_url.split(seporator, 1)[0]
    res += 'state='
    assert res == 'https://connect.mail.ru/oauth/authorize?state='

def test_auth_page_yand(auth_page):

    auth_page.btn_ok.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'state%'
    res = test_url.split(seporator, 1)[0]
    res += 'state%'
    assert res == 'https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.redirect=%252Fdk%253Fst.cmd%253DOAuth2Permissions%2526amp%253Bst.scope%253Dlogin%25253Aemail%2526amp%253Bst.response_type%253Dcode%2526amp%253Bst.show_permissions%253Doff%2526amp%253Bst.redirect_uri%253Dhttps%25253A%25252F%25252Fb2c.passport.rt.ru%25252Fsocial%25252Fadapter%25252Fok%25252Fauth%2526amp%253Bst.state%'

def test_auth_page_reg(auth_page):

    auth_page.btn_register.click()
    #chrome_browser_instance = webdriver.Chrome()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'tab_id='
    res = test_url.split(seporator, 1)[0]
    res += 'tab_id='
    assert res == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id='

def test_auth_page_help(auth_page):

    auth_page.btn_help.click()
    test_url = WebPage.get_current_url(auth_page)
    seporator = 'state='
    res = test_url.split(seporator, 1)[0]
    res += 'state='
    assert res == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state='















