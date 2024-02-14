from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities.logger import Logger


class ProductDetailsPage(Logger):

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
    currency = (By.CLASS_NAME, "ec_currency_select")
    eurOption = (By.XPATH, "//*[@id='ec_currency_conversion']/option[2]")
    commentText = (By.XPATH, "//*[@id='comment']")
    commentName = (By.XPATH, "//*[@id='author']")
    commentEmail = (By.XPATH, "//*[@id='email']")
    commentWebsite = (By.XPATH, "//*[@id='url']")
    postComment = (By.XPATH, "//*[@id='submit']")
    signUp = (By.XPATH, "//*[@id='login-from-side-menu']/div[4]/p/a")
    greenColor = (By.XPATH, "//*[@id='post-6192']/div/section/div[1]/div[3]/form/div[5]/div[2]/ul/li[4]/img")
    hotItem = (By.XPATH, "//*[@id='ec_image_product_widget_anchor-bracelet_1_0']/img")
    loadingIcon1 = (By.XPATH, "//*[@id='post-1820']/div/div/div/span")
    mySpace = (By.XPATH, "//*[@id='post-1675']/div/section/div[1]/div[3]/div[2]/div[6]/a/img")
    loadingIcon2 = (By.XPATH, "//*[@id='post-1829']/div/p[1]/span/span")
    orderHistory = (By.XPATH, "//*[@id='ec_loginwidget-5']/a[2]")

    def __init__(self, driver):
        self.driver = driver

    def signInButton(self):
        self.getLogger().info("Clicking on the \"SIGN IN\" button.")
        return self.driver.find_element(*ProductDetailsPage.signIn)

    def emailField(self):
        self.getLogger().info("Entering data in the \"EMAIL\" field.")
        return self.driver.find_element(*ProductDetailsPage.email)

    def passwordField(self):
        self.getLogger().info("Entering data in the \"PASSWORD\" field.")
        return self.driver.find_element(*ProductDetailsPage.password)

    def allItemsButton(self):
        self.getLogger().info("Clicking on the \"ALL ITEMS\" button.")
        return self.driver.find_element(*ProductDetailsPage.allItems)

    def productDescription(self):
        self.getLogger().info("Clicking on the product description.")
        return self.driver.find_element(*ProductDetailsPage.description)

    def shoppingCartHover(self):
        self.getLogger().info("Hovering over the shopping cart.")
        hover = self.driver.find_element(*ProductDetailsPage.shoppingCart)
        self.driver.execute_script("arguments[0].setAttribute('style','display: block;')", hover)

    def shoppingCartPopUpButton(self):
        self.getLogger().info("Clicking on an untranslated characters in the shoping cart.")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.driver.find_element(*ProductDetailsPage.checkOut)
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(button, 120, 55)
        action.click()
        action.perform()

    def checkOutButton(self):
        self.getLogger().info("Clicking on the \"CHECK OUT\" button.")
        return self.driver.find_element(*ProductDetailsPage.checkOut)

    def orangeColorButton(self):
        self.getLogger().info("Clicking on the \"ORANGE\" color option.")
        return self.driver.find_element(*ProductDetailsPage.orangeColor)

    def selectedColorButton(self):
        self.getLogger().info("Clicking on the selected color.")
        return self.driver.find_element(*ProductDetailsPage.selectedColor)

    def filterByPriceButton(self):
        self.getLogger().info("Clicking on \"FILTER BY PRICE\".")
        return self.driver.find_element(*ProductDetailsPage.filterByPrice)

    def twitterButton(self):
        self.getLogger().info("Clicking on the Twitter icon.")
        return self.driver.find_element(*ProductDetailsPage.twitter)

    def manufacturerButton(self):
        self.getLogger().info("Clicking on the \"MANUFACTURER\" button.")
        return self.driver.find_element(*ProductDetailsPage.manufacturer)

    def currencyButton(self):
        self.getLogger().info("Clicking on the \"CURRENCY\" dropdown menu.")
        return self.driver.find_element(*ProductDetailsPage.currency)

    def eurOptionButton(self):
        self.getLogger().info("Clicking on the \"EUR\" option.")
        return self.driver.find_element(*ProductDetailsPage.eurOption)

    def commentTextField(self):
        self.getLogger().info("Entering data in the comment's text field.")
        return self.driver.find_element(*ProductDetailsPage.commentText)

    def commentNameField(self):
        self.getLogger().info("Entering data in the comment's name field.")
        return self.driver.find_element(*ProductDetailsPage.commentName)

    def commentEmailField(self):
        self.getLogger().info("Entering data in the comment's email field.")
        return self.driver.find_element(*ProductDetailsPage.commentEmail)

    def commentWebsiteField(self):
        self.getLogger().info("Entering data in the comment's website field.")
        return self.driver.find_element(*ProductDetailsPage.commentWebsite)

    def postCommentButton(self):
        self.getLogger().info("Clicking on the \"POST COMMENT\" button.")
        return self.driver.find_element(*ProductDetailsPage.postComment)

    def signUpButton(self):
        self.getLogger().info("Clicking on the \"SIGN UP\" button.")
        return self.driver.find_element(*ProductDetailsPage.signUp)

    def greenColorButton(self):
        self.getLogger().info("Clicking on the \"GREEN\" color option.")
        return self.driver.find_element(*ProductDetailsPage.greenColor)

    def hotItemImageButton(self):
        self.getLogger().info("Clicking on the \"HOT ITEM\" image.")
        return self.driver.find_element(*ProductDetailsPage.hotItem)

    def loadingIconButton(self, icon):
        self.getLogger().info("Clicking on the loading icon.")
        return self.driver.find_element(*icon)

    def mySpaceButton(self):
        self.getLogger().info("Clicking on the MySpace icon.")
        return self.driver.find_element(*ProductDetailsPage.mySpace)

    def orderHistoryButton(self):
        self.getLogger().info("Clicking on the \"ORDER HISTORY\" button.")
        return self.driver.find_element(*ProductDetailsPage.orderHistory)