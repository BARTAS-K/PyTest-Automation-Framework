import time
from pageObjects.myCartPage import MyCartPage
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from utilities.baseClass import BaseClass


class Tests(BaseClass):

    def test_bug6(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).hotItemImageButton().click()
        self.page(ProductDetailsPage).loadingIconButton(ProductDetailsPage.loadingIcon1).click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug11(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).mySpaceButton().click()
        self.page(ProductDetailsPage).loadingIconButton(ProductDetailsPage.loadingIcon2).click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug15(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).emailField().send_keys("bob@bob.us")
        self.page(ProductDetailsPage).passwordField().send_keys("Thisisbob")
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(MyAccountPage).loadingIcon3Button().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)
