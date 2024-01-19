from selenium.webdriver.common.by import By


class LoginPage:

    singIn = (By.XPATH, "//*[@id='display-account-login-form-start']/div[7]/button")
    popUp2 = (By.XPATH, "//*[@id='popmake-4393']/button")
    passwordMark = (By.XPATH, "//*[@id='display-account-login-form-start']/div[5]/div")
    untranslated = (By.XPATH, "//*[@id='post-1375']/div/div[3]/div[2]")

    def __init__(self, driver):
        self.driver = driver

    def singInButton(self):
        return self.driver.find_element(*LoginPage.singIn)

    def popUp2CloseButton(self):
        return self.driver.find_element(*LoginPage.popUp2)

    def passwordMarkButton(self):
        return self.driver.find_element(*LoginPage.passwordMark)

    def untranslatedLink(self):
        return self.driver.find_element(*LoginPage.untranslated)