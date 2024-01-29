from selenium.webdriver.common.by import By

class RegisterPage():

    forgotPassword = (By.XPATH, "//*[@id='display-account-login-form-start']/div[5]/a")
    retrievePasswordEmail = (By.XPATH, "//*[@id='ec_account_forgot_password_email']")
    retrievePassword = (By.CLASS_NAME, "ec_account_button")

    def __init__(self, driver):
        self.driver = driver

    def forgotPasswordButton(self):
        return self.driver.find_element(*RegisterPage.forgotPassword)

    def retrievePasswordEmailField(self):
        return self.driver.find_element(*RegisterPage.retrievePasswordEmail)

    def retrievePasswordButton(self):
        return self.driver.find_element(*RegisterPage.retrievePassword)