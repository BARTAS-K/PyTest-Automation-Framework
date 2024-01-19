from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage:

    shoesImage = (By.XPATH, "//*[@id='ec_product_image_effect_4481370']")
    greyJeansImage = (By.XPATH, "//*[@id='ec_product_image_effect_4281370']/a")
    popUpClose = (By.XPATH, "//*[@id='popmake-4406']/button")
    blueTshirt = (By.XPATH, "//*[@id='ec_product_image_effect_3481370']/a")

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