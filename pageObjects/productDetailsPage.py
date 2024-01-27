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
    shoppingCartPopUp = (By.XPATH, "//*[@id='ec_cartitem_items_1455847']")
    checkOut = (By.XPATH, "//*[@id='ec_cartwidget-2']/div/div[1]/div/a/div")
    orangeColor = (By.XPATH, "//*[@id='post-6190']/div/section/div[1]/div[3]/form/div[5]/div[2]/ul/li[2]/img")
    selectedColor = (By.XPATH, "//*[@id='post-6190']/div/section/div[1]/div[3]/form/div[5]/div[2]/div[1]/div")
    filterByPrice = (By.XPATH, "//*[@id='ec_pricepointwidget-2']/div/div[3]/a[1]")
    twitter = (By.XPATH, "//*[@id='post-1675']/div/section/div[1]/div[3]/div[2]/div[2]/a/img")
    manufacturer = (By.XPATH, "//*[@id='manufacturer-bug']/a")

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
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.driver.find_element(*ProductDetailsPage.checkOut)
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(button, 120, 55)
        action.click()
        action.perform()

    def checkOutButton(self):
        return self.driver.find_element(*ProductDetailsPage.checkOut)

    def orangeColorButton(self):
        return self.driver.find_element(*ProductDetailsPage.orangeColor)

    def selectedColorButton(self):
        return self.driver.find_element(*ProductDetailsPage.selectedColor)

    def filterByPriceButton(self):
        return self.driver.find_element(*ProductDetailsPage.filterByPrice)

    def twitterButton(self):
        return self.driver.find_element(*ProductDetailsPage.twitter)

    def manufacturerButton(self):
        return self.driver.find_element(*ProductDetailsPage.manufacturer)