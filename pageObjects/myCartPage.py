from selenium.webdriver.common.by import By
from utilities.logger import Logger


class MyCartPage(Logger):

    returnToStore = (By.XPATH, "//*[@id='post-1374']/div/div/div[2]/a")
    deleteItem = (By.CLASS_NAME, "ec_cartitem_delete")
    cartTotal = (By.XPATH, "//*[@id='ec_cart_total']")
    addQuantity = (By.CLASS_NAME, "ec_plus")
    update = (By.CLASS_NAME, "ec_cartitem_update_button")

    def __init__(self, driver):
        self.driver = driver

    def returnToStoreButton(self):
        self.getLogger().info("Ckicing on the \"RETURN TO STORE\" button.")
        return self.driver.find_element(*MyCartPage.returnToStore)

    def deleteItemButton(self):
        self.getLogger().info("Clicking on the \"DELETE ITEM\" button.")
        return self.driver.find_element(*MyCartPage.deleteItem)

    def cartTotalButton(self):
        self.getLogger().info("Clicking on the \"TOTAL PRICE\" in my cart.")
        return self.driver.find_element(*MyCartPage.cartTotal)

    def addQuantityButton(self):
        self.getLogger().info("Clicking on the \"ADD QUANTITY\" button.")
        return self.driver.find_element(*MyCartPage.addQuantity)

    def updateButton(self):
        self.getLogger().info("Clicking on the \"UPDATE\" button.")
        return self.driver.find_element(*MyCartPage.update)