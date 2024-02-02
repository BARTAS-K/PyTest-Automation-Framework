from selenium.webdriver.common.by import By


class MyAccountPage():

    loadingIcon3 = (By.XPATH, "//*[@id='ec_account_dashboard']/div[2]/div[6]/span")

    def __init__(self, driver):
        self.driver = driver

    def loadingIcon3Button(self):
        return self.driver.find_element(*MyAccountPage.loadingIcon3)