from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage:

    shoesImage = (By.XPATH, "//*[@id='ec_product_image_effect_4481370']")
    greyJeansImage = (By.XPATH, "//*[@id='ec_product_image_effect_4281370']/a")
    popUpClose = (By.XPATH, "//*[@id='popmake-4406']/button")
    blueTshirt = (By.XPATH, "//*[@id='ec_product_image_effect_3481370']/a")
    addToCart = (By.XPATH, "//*[@id='ec_add_to_cart_27']")
    viewCart = (By.XPATH, "//*[@id='ec_product_page']/div[2]/a")
    professionalSuitImage = (By.XPATH, "//*[@id='ec_product_image_effect_3981370']/a")

    def __init__(self, driver):
        self.driver = driver

    def shoesImageButton(self):
        return self.driver.find_element(*ProductsPage.shoesImage)

    def popUpCloseButton(self):
        return self.driver.find_element(*ProductsPage.popUpClose)

    def popUpCloseMethod(self, button): #should this be in a different file in utilities?
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(button, 50, 50)
        action.click()
        action.perform()

    def greyJeansImageButton(self):
        return self.driver.find_element(*ProductsPage.greyJeansImage)

    def blueTshirtButton(self):
        return self.driver.find_element(*ProductsPage.blueTshirt)

    def addToCartButton(self):
        return self.driver.find_element(*ProductsPage.addToCart)

    def viewCartButton(self):
        return self.driver.find_element(*ProductsPage.viewCart)

    def professionalSuitImageButton(self):
        return self.driver.find_element(*ProductsPage.professionalSuitImage)
