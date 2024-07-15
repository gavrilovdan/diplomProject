from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25be98d5-4e4c-4412-9b8e-8ddb50bd2be3')
        super().__init__(web_driver, url)


    btn_tab_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    btn_tab_email = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    btn_tab_login = WebElement(xpath='//*[@id="t-btn-tab-login"]')
    btn_tab_ls = WebElement(xpath='//*[@id="t-btn-tab-ls"]')
    input_username = WebElement(xpath='//*[@id="username"]')
    input_password = WebElement(xpath='//*[@id="password"]')
    forgot_password = WebElement(xpath='//*[@id="forgot_password"]')
    btn_enter = WebElement(xpath='//*[@id="kc-login"]')
    help_modal = WebElement(xpath='//*[@id="faq-open"]/a')
    btn_register = WebElement(xpath='//*[@id="kc-register"]')
    eye_btn = WebElement(xpath='//*[@class="rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye"]')
    finish_type_btn = WebElement(xpath='//*[@type="text"][1]')
    btn_usagr = WebElement(xpath='//*[@id="rt-auth-agreement-link"]')
    btn_tink = WebElement(xpath='//*[@id="oidc_tinkoff"]')
    btn_yand = WebElement(xpath='//*[@id="oidc_ya"]')
    btn_vk = WebElement(xpath='//*[@id="oidc_vk"]')
    btn_mail = WebElement(xpath='//*[@id="oidc_mail"]')
    btn_ok = WebElement(xpath='//*[@id="oidc_ok"]')
    btn_help = WebElement(xpath='//*[@id="faq-open"]')
    fio = WebElement(xpath='//*[@id="app"]/main/div[2]/div[2]/div/h3')
    err = WebElement(xpath='//*[@id="form-error-message"]')