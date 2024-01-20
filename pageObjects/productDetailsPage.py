from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductDetailsPage:

    signIn = (By.XPATH, "//*[@id='login-from-side-menu']/div[6]/button")
    email = (By.XPATH, "//*[@id='ec_account_login_email_widget']")
    password = (By.XPATH, "//*[@id='ec_account_login_password_widget']")
    allItems = (By.XPATH, "//*[@id='menu3']")
    description = (By.XPATH, "//*[@id='post-1675']/div/section/div[2]/div/div/p")
    shoppingCart = (By.XPATH, "//*[@id='ec_cartwidget-2']/div/div[1]")
    shoppingCartPopUp = (By.XPATH, "//*[@id='ec_cartitem_items_1452673']")
    checkOut = (By.XPATH, "//*[@id='ec_cartwidget-2']/div/div[1]/div/a/div")

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

    def productDescription(self):
        return self.driver.find_element(*ProductDetailsPage.description)

    def shoppingCartHover(self):
        hover = self.driver.find_element(*ProductDetailsPage.shoppingCart)
        self.driver.execute_script("arguments[0].setAttribute('style','display: block;')", hover)

    def shoppingCartPopUpButton(self):
        return self.driver.find_element(*ProductDetailsPage.shoppingCartPopUp)

    def checkOutButton(self):
        return self.driver.find_element(*ProductDetailsPage.checkOut)
