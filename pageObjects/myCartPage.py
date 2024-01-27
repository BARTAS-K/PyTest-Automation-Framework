from selenium.webdriver.common.by import By

class MyCartPage():

    returnToStore = (By.XPATH, "//*[@id='post-1374']/div/div/div[2]/a")
    deleteItem = (By.CLASS_NAME, "ec_cartitem_delete")
    cartTotal = (By.XPATH, "//*[@id='ec_cart_total']")
    addQuantity = (By.CLASS_NAME, "ec_plus")
    update = (By.CLASS_NAME, "ec_cartitem_update_button")

    def __init__(self, driver):
        self.driver = driver

    def returnToStoreButton(self):
        return self.driver.find_element(*MyCartPage.returnToStore)

    def deleteItemButton(self):
        return self.driver.find_element(*MyCartPage.deleteItem)

    def cartTotalButton(self):
        return self.driver.find_element(*MyCartPage.cartTotal)

    def addQuantityButton(self):
        return self.driver.find_element(*MyCartPage.addQuantity)

    def updateButton(self):
        return self.driver.find_element(*MyCartPage.update)