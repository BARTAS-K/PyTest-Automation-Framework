from selenium.webdriver.common.by import By
from utilities.logger import Logger


class RegisterPage(Logger):

    forgotPassword = (By.XPATH, "//*[@id='display-account-login-form-start']/div[5]/a")
    retrievePasswordEmail = (By.XPATH, "//*[@id='ec_account_forgot_password_email']")
    retrievePassword = (By.CLASS_NAME, "ec_account_button")

    def __init__(self, driver):
        self.driver = driver

    def forgotPasswordButton(self):
        self.getLogger().info("Clicking on the \"FORGOT PASSWORD\" button.")
        return self.driver.find_element(*RegisterPage.forgotPassword)

    def retrievePasswordEmailField(self):
        self.getLogger().info("Entering email in the \"EMAIL\" field.")
        return self.driver.find_element(*RegisterPage.retrievePasswordEmail)

    def retrievePasswordButton(self):
        self.getLogger().info("Clicking on the \"RETRIEVE PASSWORD\" button.")
        return self.driver.find_element(*RegisterPage.retrievePassword)