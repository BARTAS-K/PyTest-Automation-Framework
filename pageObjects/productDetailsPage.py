from selenium.webdriver.common.by import By


class ProductDetailsPage:

    signIn = (By.XPATH, "//*[@id='login-from-side-menu']/div[6]/button")
    email = (By.XPATH, "//*[@id='ec_account_login_email_widget']")
    password = (By.XPATH, "//*[@id='ec_account_login_password_widget']")
    allItems = (By.XPATH, "//*[@id='menu3']")

    def __init__(self, driver):
        self.driver = driver

    def signInButton(self):
        return self.driver.find_element(*ProductDetailsPage.signIn)

    def emailField(self):
        return self.driver.find_element(*ProductDetailsPage.email)

    def passwordField(self):
        return self.driver.find_element(*ProductDetailsPage.password)

    def allItemsButton(self):
        return self.driver.find_element(*ProductDetailsPage.allItems)