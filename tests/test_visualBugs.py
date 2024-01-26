import time
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass

class Tests(BaseClass):

    def test_bug2(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).emailField().send_keys("testLogin")
        self.page(ProductDetailsPage).passwordField().send_keys("testPassword")
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(LoginPage).singInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug7(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).greyJeansImageButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug14(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)

    def test_bug21(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(LoginPage).passwordMarkButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug23(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).allItemsButton().click()
        self.page(ProductsPage).blueTshirtButton().click()
        time.sleep(3)