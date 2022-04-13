import datetime
import aos_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

#s = Service(executable_path='../chromedriver.exe')
#driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome(options=options)

# Fixture method - to open web browser
def setup():
    # Make a full screen
    driver.maximize_window()
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)
    # navigating to the advantageonlineshopping website
    driver.get(locators.aos_url)
    # Checking that we're on the correct URL address ,and we're seeing correct title
    if driver.current_url == locators.aos_url and driver.title == ' Advantage Shopping':
        print(f'We\'re at homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- {driver.title}')
    else:
        print(f'We\'re not at the homepage. Check your code!')
        # driver.close()
        # driver.quit()


def teardown():
    if driver is not None:

        print(f'-------------------')
        print(f'Hurray.Test is done successfully')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

    else:
        print(f'unable to close and quit')


def create_new_account():
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(3)
        if driver.current_url == 'https://advantageonlineshopping.com/#/register':
            driver.find_element(By.XPATH, "//input[@name= 'usernameRegisterPage']").send_keys(locators.new_username)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'emailRegisterPage']").send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'passwordRegisterPage']").send_keys(locators.new_password)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'confirm_passwordRegisterPage']").send_keys(
                locators.new_password)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'first_nameRegisterPage']").send_keys(locators.firstname)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'last_nameRegisterPage']").send_keys(locators.lastname)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'phone_numberRegisterPage']").send_keys(locators.phone)
            sleep(0.25)
            Select(
                driver.find_element(By.XPATH, "//select[@name = 'countryListboxRegisterPage']")).select_by_visible_text(
                'Canada')
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'cityRegisterPage']").send_keys(locators.city)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'addressRegisterPage']").send_keys(locators.address)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'state_/_province_/_regionRegisterPage']").send_keys(
                locators.province)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'postal_codeRegisterPage']").send_keys(locators.postal_code)
            sleep(0.25)
            # driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').click()
            driver.find_element(By.XPATH, '//input[@name="i_agree"]').click()
            sleep(0.25)
            driver.find_element(By.XPATH, '//button[@id="register_btnundefined"]').click()
            # driver.find_element(By.XPATH, '//*[@id="registerPage"]/article/sec-form/div[2]/sec-sender').click()
            sleep(5)


def validate_new_account():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        if driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/span').text == locators.new_username:
            sleep(1)
            print(f'username :{locators.new_username} is displayed')
        else:
            print(f'something went wrong:')
            sleep(3)


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'logged out successfully at :{datetime.datetime.now()}')
        sleep(1)
    else:
        print(f' not able to logged out.something went wrong')


def log_in():
    sleep(3)
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(3)

        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(3)

        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(3)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)

        if driver.find_element(By.ID, 'signInResultMessage').text == "Incorrect user name or password.":
            print("user don't exist")
        else:
            print(f'logged in successfully to the New account with username: {locators.new_username}')
        sleep(3)


def checkout_shoppingcart():
    driver.get(locators.aos_product_url)
    if driver.current_url == locators.aos_product_url:
        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)
        driver.find_element(By.ID, 'checkOutPopUp').click()
        sleep(1)
        if driver.find_element(By.XPATH, '//label[contains(text(), locators.fullname )]'):
            print(f'fullname is displayed')
        driver.find_element(By.ID, 'next_btn').click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'safepay_username']").send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'safepay_password']").send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.XPATH, '//button[@id="pay_now_btn_SAFEPAY"]').click()
        sleep(1)


def validate_order():
    if driver.find_element(By.ID, 'orderPaymentSuccess'):
        print(f'Thank you for buying with Advantage')
        locators.tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
        print(locators.tracking_number)
        locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
        print(locators.order_number)
        if driver.find_element(By.XPATH, '//label[contains(text(), locators.fullname )]'):
            print(f'fullname is displayed')
        if driver.find_element(By.XPATH, '//label[contains(text(), locators.phone )]'):
            print(f'phone number is displayed')
    else:
        print(f' Thank you for buying with Advantage message is not .something went wrong')


def validate_order_page():
    driver.get(locators.aos_myorders_url)
    if driver.current_url == locators.aos_myorders_url:
        if driver.find_element(By.XPATH, '//label[contains(text(), locators.order_number )]'):
            print(f'orderNumber is good')


def delete_order_page():
    driver.find_element(By.XPATH, '//a[contains(text(),"REMOVE")]').click()

    sleep(2)
    driver.find_element(By.ID, 'confBtn_1').click()
    sleep(1)
    print(f'Order has been deleted')


def delete_user_account():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//label[contains(text(), locators.fullname )]'):
        print(f'fullname is displayed')
    else:
        print(f'fullname is not displayed  .something went wrong')
        sleep(1)

    driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[6]/button').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
    sleep(3)


def validate_homepage_texts_links():
    if driver.current_url == locators.aos_url:
        if driver.find_element(By.ID, 'speakersTxt').text == "SPEAKERS":
            print(f'Speakers text is displayed')
        else:
            print(f'Speakers text is not  displayed')
            sleep(2)

        if driver.find_element(By.ID, 'tabletsTxt').text == "TABLETS":
            print(f'Tablets text is displayed')
        else:
            print(f'Tablets text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'headphonesTxt').text == "HEADPHONES":
            print(f'Headphones text is displayed')
        else:
            print(f'Headphones text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'laptopsTxt').text == "LAPTOPS":
            print(f'Laptops text is displayed')
        else:
            print(f'Laptops text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'miceTxt').text == "MICE":
            print(f'Mice title is displayed')
        else:
            print(f'Mice title is not displayed')
            sleep(2)

        try:
            driver.find_element(By.XPATH, "//a[text() = 'SPECIAL OFFER']").click()
            sleep(2)
            print(f'Special offer link is clickable')
        except WebDriverException:
            print(f'unable to click')
        try:
            driver.find_element(By.XPATH, "//a[text() = 'POPULAR ITEMS']").click()
            sleep(2)
            print(f'Popular item link is clickable')
        except WebDriverException:
            print(f'unable to click')
        try:
            driver.find_element(By.XPATH, "//a[text() = 'CONTACT US']").click()
            sleep(2)
            print(f'Contact us link is clickable')
        except WebDriverException:
            print(f'unable to click')

    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
        sleep(1)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text(
            'HP Chromebook 14 G1(ES)')
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'emailContactUs']").send_keys(locators.email)
        sleep(1)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys('this is a test')
        sleep(1)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)
    if driver.find_element(By.XPATH, '//p[contains(text(), "Thank you for contacting Advantage support")]'):
        print(f'Thank you message for contact form is displayed')

        try:
            driver.find_element(By.XPATH, "//a[text() = ' CONTINUE SHOPPING ']").click()
            sleep(3)
            print(f'Continue Shopping link is clickable')
        except WebDriverException:
            print(f'unable to click')
            sleep(3)

    try:
        sitelogo = driver.find_element(By.CLASS_NAME, 'logo')
        if sitelogo.is_displayed():
            print('Logo is displayed')

        sleep(3)
    except WebDriverException as ex:
        print(ex.msg)

    try:
        facebooklink = driver.find_element(By.NAME, 'follow_facebook')
        if facebooklink.is_displayed():
            print('Facebook link is displayed')
            facebooklink.click()

        sleep(3)
        print(f'Facebook link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    try:
        twitterlink = driver.find_element(By.NAME, 'follow_twitter')
        if twitterlink.is_displayed():
            print('Twitter link is displayed')
            twitterlink.click()

        sleep(3)
        print(f'Twitter link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    try:
        linkedinlink = driver.find_element(By.NAME, 'follow_linkedin')
        if linkedinlink.is_displayed():
            print('Linkedin link is displayed')
            linkedinlink.click()

        sleep(3)
        print(f'Linkedin link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    driver.switch_to.window(driver.window_handles[3])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    sleep(1)

# Lab 3
# setup()
# validate_homepage_texts_links()
# create_new_account()
# validate_new_account()
# log_out()
# log_in()
# validate_new_account()
# checkout_shoppingcart()
# validate_order()
# log_out()
# log_in()
# validate_order_page()
# delete_order_page()
# delete_user_account()
# log_out()
# log_in()
# teardown()
