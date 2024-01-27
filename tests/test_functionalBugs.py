import time
from pageObjects.myCartPage import MyCartPage
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


class Tests(BaseClass):

    def test_bug5(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).addToCartButton().click()
        self.page(ProductsPage).viewCartButton().click()
        self.page(MyCartPage).cartTotalButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug8(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).filterByPriceButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug10(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).twitterButton().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug13(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).addToCartButton().click()
        self.page(ProductsPage).viewCartButton().click()
        self.page(MyCartPage).addQuantityButton().click()
        self.page(MyCartPage).addQuantityButton().click()
        self.page(MyCartPage).updateButton().click()
        time.sleep(4)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug22(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).manufacturerButton().click()
        self.page(HomePage).findBugsButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)