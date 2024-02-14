from selenium.webdriver.common.by import By
from utilities.logger import Logger


class LoginPage(Logger):

    singIn = (By.XPATH, "//*[@id='display-account-login-form-start']/div[7]/button")
    passwordMark = (By.XPATH, "//*[@id='display-account-login-form-start']/div[5]/div")
    untranslated = (By.XPATH, "//*[@id='post-1375']/div/div[3]/div[2]")

    def __init__(self, driver):
        self.driver = driver

    def singInButton(self):
        self.getLogger().info("Clicking on the \"SIGN IN\" button.")
        return self.driver.find_element(*LoginPage.singIn)

    def passwordMarkButton(self):
        self.getLogger().info("Clicking on the password mark.")
        return self.driver.find_element(*LoginPage.passwordMark)

    def untranslatedLink(self):
        self.getLogger().info("Clicking on an untranslated link on the login page.")
        return self.driver.find_element(*LoginPage.untranslated)