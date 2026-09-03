import allure
from playwright.sync_api import Page, expect

@allure.story('Miscellaneous tests')
@allure.title("Contact Us Form")
def test_contact_us(base_page, contact_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на кнопку 'Contact us'"):
        base_page.contact_link.click()
    with allure.step("Проверить, что отображается 'Get in Touch'"):
        expect(contact_page.contact_header).to_be_visible()
    with allure.step("Заполнить форму с приложенным файлом"):
        contact_page.contact_form_fill("Maxwell", "max@mail.com", "Good Job!", "Great Job You did here, guys")
    with allure.step("Нажать на кнопку 'Submit' и ответить 'ОК' в диалоговом окне"):
        page.on("dialog", lambda dialog: dialog.accept())
        contact_page.submit.click()
    with allure.step("Проверить, что отображается алерт удачной отправки формы"):
        expect(contact_page.success_alert).to_be_visible()
    with allure.step("Нажать на кнопку 'Home'"):
        contact_page.home_button.click()
    with allure.step("Проверить, что открылась домашняя страница"):
        expect(page).to_have_url("https://automationexercise.com/")

@allure.story('Miscellaneous tests')
@allure.title("Verify Test Cases Page")
def test_verify_tests_page(base_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на кнопку 'Test Cases'"):
        base_page.tests_link.click()
    with allure.step("Проверить, что отобразилась страница с тестами"):
        expect(page).to_have_url("https://automationexercise.com/test_cases")

@allure.story('Miscellaneous tests')
@allure.title("Verify Subscription in home page")
def test_subscription(base_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Проверить, что отображается текст 'SUBSCRIPTION' "):
        expect(base_page.subscription_text).to_be_visible()
    with allure.step("Заполнить форму и подписаться"):
        base_page.subscribe('test_email@gmail.com')